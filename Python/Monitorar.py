import psutil
import os
from datetime import datetime
import time

LOG_DIR = r"C:\Users\exatt\OneDrive\Documentos\Monitor"
LOG_FILE = os.path.join(LOG_DIR, "gc44826_log.txt")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Dicionário para armazenar o número de bytes enviados por conexão
connection_data = {}

# Limite mínimo de bytes para considerar um possível envio de print
BYTE_THRESHOLD = 50000

# Estado anterior do processo GetScreen
previous_state = None


def log_event(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log:
        log.write(f"{timestamp} - {event}\n")


def find_getscreen_process():
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if process.info['name'] and 'getscreen' in process.info['name'].lower():
            return process.info['pid']
    return None


def monitor_connections(pid):
    global connection_data

    try:
        process = psutil.Process(pid)
        connections = process.connections()
        for conn in connections:
            if conn.status == psutil.CONN_ESTABLISHED:
                conn_key = (conn.raddr.ip, conn.raddr.port)
                # Obtém o número de bytes enviados
                net_io = psutil.net_io_counters(pernic=True)
                sent_bytes = net_io.get("Ethernet", psutil.net_io_counters()).bytes_sent

                # Compara com o valor anterior
                if conn_key in connection_data:
                    diff = sent_bytes - connection_data[conn_key]
                    if diff >= BYTE_THRESHOLD:
                        log_event(f"GetScreen enviou {diff} bytes para {conn.raddr}")
                
                # Atualiza o registro
                connection_data[conn_key] = sent_bytes

    except psutil.AccessDenied:
        log_event("Acesso negado ao processo")
    except psutil.NoSuchProcess:
        log_event("Processo GetScreen não encontrado")


def main():
    global previous_state

    print("Iniciando monitoramento do GetScreen...")
    first_run = True

    while True:
        pid = find_getscreen_process()
        current_state = pid is not None

        if first_run or current_state != previous_state:
            if current_state:
                log_event("GetScreen detectado em execução")
            else:
                log_event("GetScreen não encontrado")
            first_run = False

        if current_state:
            monitor_connections(pid)

        previous_state = current_state
        time.sleep(1)


if __name__ == "__main__":
    main()

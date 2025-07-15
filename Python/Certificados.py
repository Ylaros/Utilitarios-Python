import os
import subprocess
import pandas as pd

def listar_certificados():
    # Comando para listar os certificados no repositório especificado
    comando = 'certutil -store -user My'
    
    # Executa o comando e captura a saída
    resultado = subprocess.run(comando, capture_output=True, text=True, shell=True)
    
    # Verifica se o comando foi executado com sucesso
    if resultado.returncode == 0:
        certificados = resultado.stdout.splitlines()

        # Converte o resultado em um DataFrame para salvar em Excel
        df = pd.DataFrame(certificados, columns=["Certificados"])

        # Salva o resultado em um arquivo Excel
        df.to_excel('certificados_digitais.xlsx', index=False)
        print("Certificados salvos no arquivo 'certificados_digitais.xlsx'")
    else:
        print("Erro ao listar certificados:\n")
        print(resultado.stderr)

if __name__ == "__main__":
    listar_certificados()

import os
import win32print
import win32api

def imprimir_pdfs(pasta):
    # Verifica se a pasta existe
    if not os.path.exists(pasta):
        print(f"A pasta {pasta} não existe.")
        return

    # Lista os arquivos na pasta
    arquivos = [f for f in os.listdir(pasta) if f.lower().endswith('.pdf')]

    if not arquivos:
        print("Nenhum arquivo PDF encontrado na pasta.")
        return

    # Configura a impressora padrão
    impressora = win32print.GetDefaultPrinter()
    print(f"Usando a impressora: {impressora}")

    # Imprime cada arquivo PDF
    for arquivo in arquivos:
        caminho_completo = os.path.join(pasta, arquivo)
        print(f"Imprimindo: {caminho_completo}")
        try:
            win32api.ShellExecute(
                0,                   # Handle da janela (0 para usar a janela padrão)
                "print",             # Ação para imprimir
                caminho_completo,    # Caminho do arquivo PDF
                None,                # Parâmetros adicionais
                ".",                 # Diretório de trabalho
                0                    # Flag para exibição da janela (0 = oculta)
            )
        except Exception as e:
            print(f"Erro ao imprimir {caminho_completo}: {e}")

# Caminho da pasta
pasta_pdf = r"C:\Users\exatt\OneDrive\Área de Trabalho\Nova pasta"

# Executa a função
imprimir_pdfs(pasta_pdf)



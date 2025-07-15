import os
import shutil
import re

# Caminhos
pasta_origem = r"C:\Users\exatt\OneDrive\Área de Trabalho\SAUL E ALBU - OFX\SAUL E ALBU - OFX"
pasta_destino = os.path.join(pasta_origem, "Ofx Renomeado")
os.makedirs(pasta_destino, exist_ok=True)

# Mapeamento de códigos de bancos para nomes
codigo_banco_nome = {
    "001": "Banco do Brasil S.A.",
    "237": "Banco Bradesco S.A.",
    "341": "Itaú Unibanco S.A.",
    "748": "Sicredi"
    # Adicione outros conforme necessário
}

# Função para limpar strings para uso em nomes de arquivos
def limpar(texto):
    return re.sub(r'[<>:"/\\|?*]', '-', texto.strip())

# Função para extrair conteúdo de uma tag OFX (SGML)
def extrair_tag(conteudo, tag):
    match = re.search(f"<{tag}>([^\r\n<]+)", conteudo, re.IGNORECASE)
    return match.group(1).strip() if match else "NE"

# Função para gerar nome único evitando sobrescrita
def gerar_nome_unico(diretorio, nome_base, extensao):
    contador = 1
    nome_completo = f"{nome_base}.{extensao}"
    while os.path.exists(os.path.join(diretorio, nome_completo)):
        nome_completo = f"{nome_base} ({contador}).{extensao}"
        contador += 1
    return nome_completo

# Processamento dos arquivos
for nome_arquivo in os.listdir(pasta_origem):
    if nome_arquivo.lower().endswith(".ofx"):
        caminho_arquivo = os.path.join(pasta_origem, nome_arquivo)

        try:
            with open(caminho_arquivo, 'r', encoding='latin-1') as f:
                conteudo = f.read()
        except Exception as e:
            print(f"Erro ao abrir {nome_arquivo}: {e}")
            continue

        # Extrair dados relevantes
        bankid = extrair_tag(conteudo, "BANKID")
        acctid = extrair_tag(conteudo, "ACCTID")
        dtstart = extrair_tag(conteudo, "DTSTART")
        dtend = extrair_tag(conteudo, "DTEND")

        nome_banco = codigo_banco_nome.get(bankid, "NE")

        # Gerar nome do novo arquivo
        nome_base = f"{limpar(nome_banco)}_{limpar(acctid)}_{limpar(dtstart)}_{limpar(dtend)}"
        nome_final = gerar_nome_unico(pasta_destino, nome_base, "ofx")
        caminho_destino = os.path.join(pasta_destino, nome_final)

        try:
            shutil.copy2(caminho_arquivo, caminho_destino)
            print(f"Arquivo renomeado: {nome_final}")
        except Exception as e:
            print(f"Erro ao copiar {nome_arquivo}: {e}")

print("Todos os arquivos foram processados com sucesso!")

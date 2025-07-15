# 🛠️ Utilitários Python

Este repositório reúne scripts Python práticos e aplicáveis ao dia a dia de ambientes contábeis, fiscais e administrativos. São ferramentas desenvolvidas para auxiliar tarefas como impressão em lote, renomeação de arquivos OFX, monitoramento de segurança e manipulação de certificados digitais.

---

## 📦 Scripts incluídos

### `Certificados.py`
> 📜 **Função:** Lista todos os certificados digitais do repositório de usuário do Windows e exporta para um arquivo Excel.

- Utiliza o comando `certutil` via subprocess
- Gera um `certificados_digitais.xlsx` com os dados capturados

---

### `imprimir.py`
> 🖨️ **Função:** Imprime todos os arquivos PDF de uma pasta específica usando a impressora padrão do sistema.

- Usa `win32print` e `win32api`
- Imprime silenciosamente os arquivos PDF um a um

---

### `Monitorar.py`
> 🛡️ **Função:** Monitora um processo (no caso, o *GetScreen* como exemplo) e registra qualquer envio de dados suspeito (acima de 50KB) via rede.

- Detecta início/fim da execução do processo
- Registra logs de atividades suspeitas (como prints sendo enviados)
- Salva log em `gc44826_log.txt` (pasta configurável)

---

### `OFXRENAME.py`
> 🏦 **Função:** Renomeia arquivos `.ofx` de extratos bancários com base em dados internos como banco, conta, período. Útil para arquivos indeterminados

- Extrai informações diretamente do conteúdo SGML do arquivo
- Nome final no formato: `Banco_Conta_DataInicio_DataFim.ofx`
- Garante nomes únicos para evitar sobrescrita
- Organiza em subpasta chamada `Ofx Renomeado`

---

## 🧩 Tecnologias Utilizadas

- Python 3.x
- `pandas`, `psutil`, `win32api`, `shutil`, `re`, `subprocess`
- Windows (todos os scripts são voltados para esse ambiente)

---

## ⚙️ Requisitos

• Ter o Python 3.x instalado (preferencialmente via https://www.anaconda.com/ ou via pip)

• Instalar as bibliotecas necessárias com o comando:

pip install pandas psutil pywin32 openpyxl

• Scripts como imprimir.py e Certificados.py exigem execução com permissões administrativas para pleno funcionamento (especialmente em redes corporativas ou com controle de segurança).


## 📎 Observações

- Nenhum script expõe informações confidenciais ou dados sensíveis.
- Os caminhos de pastas podem (e devem) ser ajustados conforme o ambiente local de uso.
- Todos os scripts foram testados em **ambiente Windows 10/11** com privilégios administrativos.

## ✍️ Autor

**Aloyr Rezende**  
🔗 [LinkedIn](https://www.linkedin.com/in/aloyr-rezende)

## 📜 Licença

Uso livre para fins **educacionais, internos ou corporativos**, com atribuição.  
Melhorias e *pull requests* são bem-vindos!

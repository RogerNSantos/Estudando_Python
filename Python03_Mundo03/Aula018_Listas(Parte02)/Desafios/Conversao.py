import tabula
import pandas as pd

# Caminho para o arquivo PDF
caminho_pdf = r"C:\Users\rogerio.santos\Desktop\Protocolo\Protocolo.pdf"

# Local onde o arquivo Excel será salvo
caminho_excel = r"C:\Users\rogerio.santos\Desktop\Protocolo\ConversaoProtocolo.xlsx"

# Extrair tabelas do PDF
tabelas = tabula.read_pdf("protocolos.pdf", pages='all', multiple_tables=True)

# Converter a tabela para DataFrame do pandas
df = pd.concat(tabelas)

# Salvar DataFrame como Excel
df.to_excel(caminho_excel, index=False)

print("Conversão concluída. O arquivo Excel foi salvo em:", caminho_excel)

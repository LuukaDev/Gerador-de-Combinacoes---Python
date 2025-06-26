import pandas as pd
import yagmail as yag
import random
from datetime import datetime as dt


estoque_df = pd.read_csv('Produtos_Case.csv')
tvs_df = estoque_df[estoque_df['Categoria'] == 'TV']
home_theaters_df = estoque_df[estoque_df['Categoria'] == 'HomeTheater']
caixas_som_df = estoque_df[estoque_df['Categoria'] == 'CaixaDeSom']

# Lista para armazenar combos prontos
combos_prontos = []

# Gera combinações de produtos com mesma potência
for _, tv in tvs_df.iterrows():
    for _, home in home_theaters_df.iterrows():
        for _, caixa in caixas_som_df.iterrows():
            if tv['PotenciaW'] == home['PotenciaW'] == caixa['PotenciaW']:
                combo_id = random.randint(10000, 99999)
                total_itens = 3 

                combos_prontos.append({
                    'IDCombo': combo_id,
                    'PotenciaTotal': tv['PotenciaW'],
                    'IDsProdutos': f"{tv['Id']},{home['Id']},{caixa['Id']}",
                    'DescricaoProdutos': f"{tv['Produto']},{home['Produto']},{caixa['Produto']}",
                    'QuantidadeItens': total_itens
                })


df_combos = pd.DataFrame(combos_prontos)
df_combos.to_csv('Combos_Eletronicos.csv', index=False)
# Informações do relatório
quantidade_combos = len(combos_prontos)
data_relatorio = dt.now().strftime('%d/%m/%Y')
nome_arquivo_pdf = "RelatorioCombos.pdf"

# Comentado para evitar execução direta
"""
yag_smtp = yag.SMTP(user="seuemail@gmail.com", password="suasenha")
assunto = "Relatório Semanal - Combos de Eletrônicos"
mensagem = f\"\"\"Olá equipe de vendas,

Segue anexo o relatório semanal com os combos de produtos eletrônicos montados automaticamente.

📅 Data: {data_relatorio}  
📦 Combos Montados: {quantidade_combos}

Atenciosamente,  
Equipe de Operações - Loja TechCenter
\"\"\"

yag_smtp.send(to="vendas@loja.com", subject=assunto, contents=mensagem, attachments="Combos_Eletronicos.csv")
"""

print("Relatório de combos gerado com sucesso!")
print(f"Total de combos montados: {quantidade_combos}")

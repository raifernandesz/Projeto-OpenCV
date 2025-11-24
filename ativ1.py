
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# crie um grafico de barras barplot ou semelhante mostrando as vendas por regiao
# Exercico 1 - Vendas por Região

# dados = {
#     "Região": ["Sul", "Sudeste", "Centro-Oeste", "Nordeste", "Norte"],
#     "Vendas": [35000, 52000, 27000, 31000, 18000]
# }


# df = pd.DataFrame(dados)
# plt.figure(figsize=(10, 6))
# sns.barplot(x = "Região", y = "Vendas",  data = df)
# plt.title("Vendas por Região")
# plt.xlabel("Região")
# plt.ylabel("Vendas (R$)")   
# plt.show()


# EXERCICO 2 - SATISFACAO DOS CLIENTES, SETOR ATENDIMENTO
# dados = {
#     "Cliente": ["Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe", "Gabriela", "Heitor"],
#     "Satisfação": [8.5, 6.0, 9.0, 7.5, 8.0, 5.5, 9.5, 7.0],
#     "Categoria": ["Premium", "Básico", "Premium", "Básico", "Premium", "Básico", "Premium", "Básico"]
# }
# df = pd.DataFrame(dados)
# plt.figure(figsize=(10, 6))
# sns.boxplot(x="Categoria", y="Satisfação", data=df)
# plt.title("Satisfação dos Clientes por Categoria")
# plt.xlabel("Categoria do Cliente")
# plt.ylabel("Nível de Satisfação")
# plt.show()


# EXERCICO 3 - PRODUTIVIDADE DA EQUIPE, SETOR RECURSOS HUMANOS 
# NO TITULO DO GRAFICO COLOQUE: PRODUTIVIDADE DA EQUIPE VS HORAS SEMANAIS TRABALHADAS PORQUE É RELAÇÃO DOS 2 
# # COLOCAR scatterplot PORQUE MOSTRA RELAÇÃO ENTRE 2 VARIÁVEIS
# dados = {
#     "Funcionário": ["Alice", "Bruno", "Carlos", "Diana", "Eduardo", "Fernanda", "Gustavo", "Helena"],
#     "Produtividade": [82, 74, 90, 65, 77, 88, 93, 70],
#     "Horas_Semanais": [40, 36, 42, 30, 38, 44, 45, 35]
# }
# df = pd.DataFrame(dados)
# plt.figure(figsize=(10,6))
# sns.scatterplot(x="Horas_Semanais", y="Produtividade", data=df, s=100)
# plt.title("Produtividade da Equipe vs Horas Semanais Trabalhadas")
# plt.xlabel("Horas Semanais Trabalhadas")
# plt.ylabel("Produtividade (%)")
# plt.show()



# EXERCICIO 4 - LUCRO MENSAL, SETOR FINANCEIRO 
# O DEPARTAMENTO FINANCEIRO QUER OBSERVAR O LUCRO DA EMPRESA AO LONGO DOS MESES 

# dados = {
#     "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
#     "Lucro": [12000, 15000, 17000, 14000, 16000, 18000, 22000, 21000, 19000, 23000, 25000, 24000]
# }
# DF = pd.DataFrame(dados)
# plt.figure(figsize=(12, 6))
# sns.lineplot(x="Mês", y="Lucro", data=DF, marker="o")
# plt.title("Lucro Mensal da Empresa")
# plt.xlabel("Mês")
# plt.ylabel("Lucro (R$)")
# plt.show()


# EXERCICIO 5 - USO DE APLICATIVOS , SETOR DE TECNOLOGIA DA INFORMAÇÃO
#  O TIME DA TECNOLOGIA QUER SABER QUANTO TEMPO OS USUARIOS PASSAM EM CADA APLICATIVO


# dados = {
#     "Aplicativo": ["Instagram", "TikTok", "WhatsApp", "YouTube", "X (Twitter)"],
#     "Minutos por dia": [95, 110, 80, 120, 60]
# }
# df = pd.DataFrame(dados)
# plt.figure(figsize=(10, 6))
# sns.barplot(x="Aplicativo", y="Minutos por dia", data=df, palette="viridis")
# plt.title("Uso de Aplicativos por Usuário")
# plt.title(" uso de Aplicativos por Usuário")
# plt.xlabel ("Aplicativo") 
# plt.ylabel("Minutos por dia")
# plt.show()

# EXERCICIO 6 - IDADE DOS FUNCIONARIOS , SETOR RECURSOS HUMANOS 
# O RH QUER ENTENDER A FAIXA ETARIA DOS FUNCIONARIOS EM DIFERENTE SETORES 

# dados = {
#     "Setor": ["Financeiro", "Comercial", "TI", "RH", "Marketing", "Comercial", "TI", "Financeiro", "Marketing", "RH"],
#     "Idade": [34, 29, 25, 41, 28, 33, 26, 38, 31, 45]
# }
# DF = pd.DataFrame(dados)
# plt.figure(figsize=(10, 6))
# sns.violinplot(x="Setor", y="Idade", data=DF, palette="Set2")
# plt.title("Distribuição de Idade dos Funcionários por Setor")
# plt.xlabel("Setor")
# plt.ylabel("Idade")
# plt.show()


# EXERCICIO 7 - ANALISE DE CUSTOS E RECEIRA, SETOR ESTRATEGICO 
# A DIRETORIA QUER ENTENDER A DIFERENÇA ENTRE CUSTOS E RECEITAS EM DIFERENTES PRODUTOS 

# dados = {
#     "Produto": ["Notebook", "Celular", "Tablet", "Fone", "Monitor"],
#     "Custo": [2500, 1800, 1200, 200, 900],
#     "Receita": [3200, 2300, 1700, 350, 1200]
# }
# DF = pd.DataFrame(dados)
# plt.figure(figsize=(10, 6))
# sns.barplot(x="Produto", y="value", hue="variable", data=pd.melt(DF, ["Produto"]))
# plt.title("Análise de Custos e Receitas por Produto")
# plt.xlabel("Produto")
# plt.ylabel("Receita (R$)")
# plt.show()
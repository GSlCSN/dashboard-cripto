import requests
import pandas as pd
import matplotlib.pyplot as plt

# busca o preço ATUAL das 3 moedas em BRL numa única requisição
response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=brl")

# converte a resposta de JSON pra dicionário Python
dados = response.json()

# busca o histórico dos últimos 7 dias de cada moeda separadamente
# cada requisição retorna uma lista de pares [timestamp, preco]
historico_atualizado_bitcoin = requests.get("https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=brl&days=7")
historico_atualizado_ethereum = requests.get("https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=brl&days=7")
historico_atualizado_solana = requests.get("https://api.coingecko.com/api/v3/coins/solana/market_chart?vs_currency=brl&days=7")

# converte cada resposta de JSON pra dicionário Python
dados_historico_bitcoin = historico_atualizado_bitcoin.json()
dados_historico_ethereum = historico_atualizado_ethereum.json()
dados_historico_solana = historico_atualizado_solana.json()

# pega só a lista de preços de cada dicionário — ignora market_caps e volumes
preco_bitcoin = dados_historico_bitcoin["prices"]
preco_ethereum = dados_historico_ethereum["prices"]
preco_solana = dados_historico_solana["prices"]

# transforma cada lista de pares [timestamp, preco] num DataFrame com 2 colunas
df_bitcoin = pd.DataFrame(preco_bitcoin, columns=["timestamp", "preco"])
df_ethereum = pd.DataFrame(preco_ethereum, columns=["timestamp", "preco"])
df_solana = pd.DataFrame(preco_solana, columns=["timestamp", "preco"])

# converte o timestamp de milissegundos pra data legível
# unit="ms" diz pro pandas que o número tá em milissegundos
df_bitcoin["timestamp"] = pd.to_datetime(df_bitcoin["timestamp"], unit="ms")
df_ethereum["timestamp"] = pd.to_datetime(df_ethereum["timestamp"], unit="ms")
df_solana["timestamp"] = pd.to_datetime(df_solana["timestamp"], unit="ms")

# cria 3 gráficos empilhados verticalmente (3 linhas, 1 coluna)
# fig é a tela inteira, ax1/ax2/ax3 são os gráficos individuais
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))

# plota o Bitcoin no primeiro gráfico
ax1.plot(df_bitcoin["timestamp"], df_bitcoin["preco"], color="yellow")
ax1.set_title("Bitcoin")
ax1.set_ylabel("Preço")

# plota o Ethereum no segundo gráfico
ax2.plot(df_ethereum["timestamp"], df_ethereum["preco"], color="green")
ax2.set_title("Ethereum")
ax2.set_ylabel("Preço")

# plota a Solana no terceiro gráfico
ax3.plot(df_solana["timestamp"], df_solana["preco"], color="pink")
ax3.set_title("Solana")
ax3.set_ylabel("Preço")

# título geral que aparece em cima de todos os gráficos
fig.suptitle("Preço das Criptomoedas (BRL) - Últimos 7 dias")

ax3.set_xlabel("Data")

# salva o gráfico em arquivo PNG antes de mostrar
# depois do show() o gráfico é limpo da memória
plt.savefig("preco_moeas.png")

# ajusta o espaçamento entre os gráficos automaticamente
# evita que títulos e datas fiquem sobrepostos
plt.tight_layout()

plt.show()
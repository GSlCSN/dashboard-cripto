import requests
import pandas as pd
import matplotlib.pyplot as plt

response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=brl")

dados = response.json()

historico_atualizado_bitcoin = requests.get("https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=brl&days=7")
historico_atualizado_ethereum = requests.get("https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=brl&days=7")
historico_atualizado_solana = requests.get("https://api.coingecko.com/api/v3/coins/solana/market_chart?vs_currency=brl&days=7")

dados_historico_bitcoin = historico_atualizado_bitcoin.json()
dados_historico_ethereum = historico_atualizado_ethereum.json()
dados_historico_solana = historico_atualizado_solana.json()

preco_bitcoin = dados_historico_bitcoin["prices"]
preco_ethereum = dados_historico_ethereum["prices"]
preco_solana = dados_historico_solana["prices"]

df_bitcoin = pd.DataFrame(preco_bitcoin, columns=["timestamp", "preco"])
df_ethereum = pd.DataFrame(preco_ethereum, columns=["timestamp", "preco"])
df_solana = pd.DataFrame(preco_solana, columns=["timestamp", "preco"])

df_bitcoin["timestamp"] = pd.to_datetime(df_bitcoin["timestamp"], unit="ms")
df_ethereum["timestamp"] = pd.to_datetime(df_ethereum["timestamp"], unit="ms")
df_solana["timestamp"] = pd.to_datetime(df_solana["timestamp"], unit="ms")

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))

ax1.plot(df_bitcoin["timestamp"], df_bitcoin["preco"], color="yellow")
ax1.set_title("Bitcoin")
ax1.set_ylabel("Preço")

ax2.plot(df_ethereum["timestamp"], df_ethereum["preco"], color="green")
ax2.set_title("Ethereum")
ax2.set_ylabel("Preço")

ax3.plot(df_solana["timestamp"], df_solana["preco"], color="pink")
ax3.set_title("Solana")
ax3.set_ylabel("Preço")

plt.legend()

plt.suptitle("Preço das Criptomoedas (BRL) - Últimos 7 dias")

plt.ylabel("Preço")
plt.xlabel("Data")

plt.legend()

plt.savefig("preco_moeas.png")

plt.tight_layout()

plt.show()
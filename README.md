# Dashboard de Criptomoedas

## Sobre o projeto
Dashboard que busca dados reais de criptomoedas via API e gera gráficos do histórico de preços dos últimos 7 dias em BRL.

## O que o projeto faz
- Busca o preço atual de Bitcoin, Ethereum e Solana em tempo real
- Busca o histórico de preços dos últimos 7 dias de cada moeda
- Gera 3 gráficos empilhados com a variação de preço de cada moeda
- Exporta o gráfico em PNG automaticamente

## Tecnologias
- Python 3.12
- requests
- pandas
- matplotlib

## API utilizada
CoinGecko API — gratuita, sem necessidade de autenticação

## Como rodar
pip install requests pandas matplotlib
python main.py

## Resultado
Gráfico gerado automaticamente com a variação de preço das 3 moedas nos últimos 7 dias, cada uma na sua própria escala para melhor visualização.
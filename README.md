
# Projeto de Variação de preço e disponibilidade - Intellibrand/ Ascential

O projeto realiza a busca de dados em diversos arquivos json, para calcular, em primeiro momento, as 10 maiores variações de preço entre o preço ofertado por redes varejistas e o preço recomendado pelo fabricante.
Em segunda fase, o projeto irá realizar a contagem dos 10 produtos com maior indisponibilidade.




## Cálculos

### Price Variation

Para calcular a metrica de variação de preço, realizei a consulta em todos os arquivos que contivessem a chave priceVariation
```Python
jsons = file_reader(os.path.join(CONFIG.FILES_PATH, file), 'priceVariation', ['idRetailerSKU','priceVariation'])
```
O metodo file_reader recebe como seus parametros o caminho do arquivo, a chave de consulta e as colunas que devem ser extraidas.

Após realizar a consulta pelos arquivos é gerado um Dataframe Pandas com os dados encontrados. 

Foi realizado um tratamento para termos a variação em valores absolutos e depois ordenames de maneira decrescente para encontrarmos os maiores valores.

```Python
df_formated = raw_df[['idRetailerSKU', 'absolutePriceVariation', 'priceVariation']].sort_values(
            by='absolutePriceVariation',
            ascending=False)
```

Em seguida realizamos a iteração sobre o dataframe para coletar os 10 primeiros itens distintos

Por fim, o arquivo com os resultados é salvo na pasta processed_data na raiz do projeto.

### Availability

Para calcular a metrica de disponibilidade, realizei a consulta em todos os arquivos que contivessem a chave available
```Python
jsons = file_reader(os.path.join(CONFIG.FILES_PATH, file), 'available', ['idRetailerSKU','available'])
```

Após realizar a consulta pelos arquivos é gerado um Dataframe Pandas com os dados encontrados. 

Foi realizado um tratamento para agrupar os dados por idRetailerSKU com a contagem de todos os Falses para cada SKU

```Python
raw_df = raw_df.groupby(['idRetailerSKU'], as_index=False)['available'].apply(lambda x: (~x).sum())
raw_df = raw_df.rename(columns={'available': 'countFalse'})
raw_df = raw_df.sort_values(by='countFalse', ascending=False)
```

Em seguida realizamos a iteração sobre o dataframe para coletar os 10 primeiros itens distintos

Por fim, o arquivo com os resultados é salvo na pasta processed_data na raiz do projeto.
## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/davi-griff/ascential-project.git
```

Entre no diretório do projeto

```bash
  cd ascential-project
```

Instale as dependências

```bash
  pip install -r requirements.txt
```

Copie o arquivo .env.example para .env e edite o arquivo .env com as propriedades corretas

```bash
FILES_PATH=/caminho/para/os/dados
ENCODING=latin
```

OBS: O ENCODING pode ser mantido como latin

Rode o projeto com

```bash
python3 runtime.py
```

## OBS:

Para fins de analise os dados processados se encontram na pasta processed_data deste repositorio
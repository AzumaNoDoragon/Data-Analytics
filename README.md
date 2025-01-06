# Análise de Indicadores Econômicos e Sociais

Este projeto utiliza **Python** e as bibliotecas **Matplotlib** e **Pandas** para explorar e visualizar relações entre indicadores econômicos e sociais, como PIB per capita, satisfação com a vida, taxa de desemprego, investimento total e sensação de segurança ao caminhar à noite.
Os dados Foram baixados em:
Better Life Index no site da OCDE (https://data-explorer.oecd.org/vis?tenant=archive&df[ds]=DisseminateArchiveDMZ&df[id]=DF_BLI&df[ag]=OECD&dq=...&to[TIME]=false);
E as estatísticas sobre o PIB per capita no site do FMI (https://www.imf.org/en/Publications/WEO/weo-database/2024/October/download-entire-database).

**Este projeto foi desenvolvido para fins de aprendizado e exploração de visualizações de dados interativos em Python.**

## Estrutura do Projeto

### Arquivos Utilizados
- **`oecd_bli.csv`**: Contém dados da OCDE relacionados a satisfação com a vida e sensação de segurança.
- **`gdp_per_capita.csv`**: Inclui dados econômicos, como PIB per capita, taxa de desemprego e investimento total.

### Funções Principais
- **`prepare_country_stats()`**: Realiza a limpeza e integração dos dados de ambas as fontes (OCDE e dados econômicos), gerando um dataframe consolidado.
- **Visualização**: Gera gráficos de dispersão para analisar as correlações entre os indicadores.

## Visualizações Geradas

O projeto cria uma figura com 6 gráficos de dispersão:

1. **PIB per capita x Satisfação com a Vida**
2. **Taxa de Desemprego x Satisfação com a Vida**
3. **Investimento Total x Satisfação com a Vida**
4. **PIB per capita x Sensação de Segurança ao Caminhar à Noite (Mulheres)**
5. **Taxa de Desemprego x Sensação de Segurança ao Caminhar à Noite (Mulheres)**
6. **Investimento Total x Sensação de Segurança ao Caminhar à Noite (Mulheres)**

Cada gráfico inclui:
- Anotações dos nomes dos países para facilitar a identificação.
- Cores distintas para diferenciar os conjuntos de dados.

## Dependências

As bibliotecas necessárias para executar o projeto são:

- **Matplotlib**: Para geração de gráficos.
- **Pandas**: Para manipulação e análise de dados.

Instale as dependências executando o script install_libraries.cmd

## Como Executar

1. Certifique-se de que os arquivos `oecd_bli.csv` e `gdp_per_capita.csv` estão na mesma pasta do script.
2. Execute o script que instala as bibliotecas (caso já estejam instaladas, pule para a próxima etapa).
3. Execute o script run_script.vbs
4. Visualize os gráficos gerados em uma janela interativa do Matplotlib.
5. É possivel utilizar zoom e movimentar cada uma das janelas geradas, para melhor visualização.

## Exemplos de Uso

Este projeto pode ser utilizado para:

- Analisar o impacto do PIB per capita na satisfação com a vida.
- Identificar relações entre indicadores econômicos e segurança percebida.
- Explorar políticas públicas em diferentes países com base em dados quantitativos.

### Minirrelatórios
Para contextualizar e facilitar o entendimento com cada gráfico, fica aqui uma explicação direta de cada gráfico plotado

![Data Analytics](https://github.com/user-attachments/assets/d12ad8c7-68ea-4ecb-a87a-3c6361148e99)

1. **Relação entre PIB per capita e Satisfação com a Vida (Gráfico Azul):**  
   Este gráfico mostra uma correlação positiva entre o PIB per capita e a satisfação com a vida. À medida que o PIB per capita aumenta, a satisfação com a vida também tende a crescer. Isso sugere que economias mais prósperas podem oferecer melhores condições de vida, refletindo-se na felicidade da população.

2. **Relação entre Taxa de Desemprego e Satisfação com a Vida (Gráfico Vermelho):**  
   Aqui, observa-se uma correlação negativa: quanto maior a taxa de desemprego, menor tende a ser a satisfação com a vida. Este resultado destaca o impacto do desemprego na qualidade de vida e no bem-estar emocional das pessoas.

3. **Relação entre Investimento Total e Satisfação com a Vida (Gráfico Verde):**  
   O gráfico revela uma relação moderada entre o percentual de investimento total em relação ao PIB e a satisfação com a vida. Embora não seja uma relação linear clara, níveis mais altos de investimento parecem estar associados a uma maior satisfação.

4. **Relação entre PIB per capita e Segurança ao Caminhar à Noite ('%' Feminino) (Gráfico Roxo):**  
   Este gráfico sugere uma correlação positiva: países com maior PIB per capita tendem a ter uma maior percepção de segurança ao caminhar à noite entre mulheres. Isso pode indicar que economias mais fortes investem mais em infraestrutura e segurança pública.

5. **Relação entre Taxa de Desemprego e Segurança ao Caminhar à Noite ('%' Feminino) (Gráfico Laranja):**  
   A relação entre a taxa de desemprego e a percepção de segurança ao caminhar à noite entre mulheres parece ser negativa. Regiões com altas taxas de desemprego geralmente apresentam menor sensação de segurança, possivelmente devido a condições sociais adversas.

6. **Relação entre Investimento Total e Segurança ao Caminhar à Noite ('%' Feminino) (Gráfico Marrom):**  
   Este gráfico sugere uma correlação positiva entre o investimento total e a percepção de segurança ao caminhar à noite entre mulheres. Isso pode indicar que investimentos direcionados promovem melhorias na segurança pública e no bem-estar geral.


import matplotlib.pyplot as plt
import pandas as pd

def prepare_country_stats(oecd_bli, gdp_per_capita):
    y1 = oecd_bli[(oecd_bli['Indicator'] == 'Life satisfaction') & (oecd_bli['INEQUALITY'] == 'TOT')]
    y2 = oecd_bli[(oecd_bli['Indicator'] == 'Feeling safe walking alone at night') & (oecd_bli['INEQUALITY'] == 'WMN')]

    oecdLife = y1[['Country', 'OBS_VALUE']].rename(columns={'OBS_VALUE': 'Life satisfaction'})
    oecdSafe = y2[['Country', 'OBS_VALUE']].rename(columns={'OBS_VALUE': 'Feeling safe'})

    x1 = gdp_per_capita[(gdp_per_capita['Subject Descriptor'] == 'Gross domestic product per capita, constant prices') 
                        & (gdp_per_capita['WEO Subject Code'] == 'NGDPRPPPPC')]
    x2 = gdp_per_capita[(gdp_per_capita['Subject Descriptor'] == 'Unemployment rate')] 
    x3 = gdp_per_capita[(gdp_per_capita['Subject Descriptor'] == 'Total investment')]
    
    gdpPib = x1[['Country', '2024']].rename(columns={'2024': 'GDP per capita'})
    gdpUneploy = x2[['Country', '2024']].rename(columns={'2024': 'Unemployment rate'})
    gdpInvestment = x3[['Country', '2024']].rename(columns={'2024': 'Total investment'})

    country_stats = pd.merge(oecdLife, gdpPib, on="Country")
    country_stats = pd.merge(country_stats, gdpUneploy, on="Country")
    country_stats = pd.merge(country_stats, gdpInvestment, on="Country")
    country_stats = pd.merge(country_stats, oecdSafe, on="Country")

    return country_stats

oecd_bli = pd.read_csv("oecd_bli.csv")
gdp_per_capita = pd.read_csv("gdp_per_capita.csv", delimiter = ';')

country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)

fig, axs = plt.subplots(3, 2, figsize=(12, 9))

# organizar lifeSatisfaction_gdp
country_stats['GDP per capita'] = country_stats['GDP per capita'].apply(lambda x: float(str(x).replace(',', '')))
country_stats['Life satisfaction'] = country_stats['Life satisfaction'].apply(lambda x: float(str(x).replace(',', '')))
country_stats['Unemployment rate'] = country_stats['Unemployment rate'].apply(lambda x: float(str(x).replace('.', '')))
country_stats['Total investment'] = country_stats['Total investment'].apply(lambda x: float(str(x).replace(',', '')))
country_stats['Feeling safe'] = country_stats['Feeling safe'].apply(lambda x: float(str(x).replace(',', '')))
country_stats = country_stats.sort_values(by=['GDP per capita', 'Life satisfaction', 'Unemployment rate', 
                                              'Total investment', 'Feeling safe'], ascending=[True, True, True, True, True])

# 1º subplot
# Plotar lifeSatisfaction_gdp
axs[0, 0].scatter(country_stats["GDP per capita"], country_stats["Life satisfaction"], color='blue')
axs[0, 0].set_title("Relação entre PIB per capita e Satisfação com a Vida (GDP)")
axs[0, 0].set_xlabel("PIB per capita")
axs[0, 0].set_ylabel("Satisfação com a Vida")

for i, row in country_stats.iterrows():
    axs[0, 0].annotate(
        row['Country'],
        (row["GDP per capita"], row["Life satisfaction"]),
        textcoords="offset points",
        xytext=(3, 3),
        ha='left',
        fontsize=7,
        alpha=0.8
    )

# 2º subplot
# Plotar lifeSatisfaction_unemployment
axs[0, 1].scatter(country_stats["Unemployment rate"], country_stats["Life satisfaction"], color='red')
axs[0, 1].set_title("Relação entre Taxa de Desemprego e Satisfação com a Vida")
axs[0, 1].set_xlabel("Taxa de Desemprego")
axs[0, 1].set_ylabel("Satisfação com a Vida")

for i, row in country_stats.iterrows():
    axs[0, 1].annotate(
        row['Country'],
        (row["Unemployment rate"], row["Life satisfaction"]),
        textcoords="offset points",
        xytext=(3, 3),
        ha='left',
        fontsize=7,
        alpha=0.8
    )

# 3º subplot
# Plotar lifeSatisfaction_investment
axs[1, 0].scatter(country_stats["Total investment"], country_stats["Life satisfaction"], color='green')
axs[1, 0].set_title("Relação entre Investimento Total e Satisfação com a Vida")
axs[1, 0].set_xlabel("Investimento Total ('%' sobre GPD per capita)")
axs[1, 0].set_ylabel("Satisfação com a Vida")

for i, row in country_stats.iterrows():
    axs[1, 0].annotate(
        row['Country'],
        (row["Total investment"], row["Life satisfaction"]),
        textcoords="offset points",
        xytext=(3, 3),
        ha='left',
        fontsize=7,
        alpha=0.8
    )

# 4º subplot
# Plotar feelingSafe_gdp
axs[1, 1].scatter(country_stats["GDP per capita"], country_stats["Feeling safe"], color='purple')
axs[1, 1].set_title("Relação entre PIB per capita e Segurança ao Caminhar à Noite ('%' Feminino)")
axs[1, 1].set_xlabel("PIB per capita")
axs[1, 1].set_ylabel("Segurança ao Caminhar à Noite")

for i, row in country_stats.iterrows():
    axs[1, 1].annotate(
        row['Country'],
        (row["GDP per capita"], row["Feeling safe"]),
        textcoords="offset points",
        xytext=(3, 3),
        ha='left',
        fontsize=7,
        alpha=0.8
    )

# 5º subplot
# Plotar feelingSafe_unemployment
axs[2, 0].scatter(country_stats["Unemployment rate"], country_stats["Feeling safe"], color='orange')
axs[2, 0].set_title("Relação entre Taxa de Desemprego e Segurança ao Caminhar à Noite ('%' Feminino)")
axs[2, 0].set_xlabel("Taxa de Desemprego")
axs[2, 0].set_ylabel("Segurança ao Caminhar à Noite")

for i, row in country_stats.iterrows():
    axs[2, 0].annotate(
        row['Country'],
        (row["Unemployment rate"], row["Feeling safe"]),
        textcoords="offset points",
        xytext=(3, 3),
        ha='left',
        fontsize=7,
        alpha=0.8
    )

# 6º subplot
# Plotar feelingSafe_investment
axs[2, 1].scatter(country_stats["Total investment"], country_stats["Feeling safe"], color='brown')
axs[2, 1].set_title("Relação entre Investimento Total e Segurança ao Caminhar à Noite ('%' Feminino)")
axs[2, 1].set_xlabel("Investimento Total")
axs[2, 1].set_ylabel("Segurança ao Caminhar à Noite")

for i, row in country_stats.iterrows():
    axs[2, 1].annotate(
        row['Country'],
        (row["Total investment"], row["Feeling safe"]),
        textcoords="offset points",
        xytext=(3, 3),
        ha='left',
        fontsize=7,
        alpha=0.8
    )

plt.tight_layout()
plt.show()
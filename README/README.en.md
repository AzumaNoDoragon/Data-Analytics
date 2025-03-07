# Analysis of Economic and Social Indicators

This project uses **Python** and the **Matplotlib** and **Pandas** libraries to explore and visualize relationships between economic and social indicators, such as GDP per capita, life satisfaction, unemployment rate, total investment, and the sense of safety when walking at night.

The data was downloaded from:
Better Life Index on the OECD website (https://data-explorer.oecd.org/vis?tenant=archive&df[ds]=DisseminateArchiveDMZ&df[id]=DF_BLI&df[ag]=OECD&dq=...&to[TIME]=false);
And GDP per capita statistics from the IMF website (https://www.imf.org/en/Publications/WEO/weo-database/2024/October/download-entire-database).

**This project was developed for learning purposes and exploring interactive data visualizations in Python.**

## Project Structure

### Files Used
- **`oecd_bli.csv`**: Contains data from the OECD related to life satisfaction and sense of safety.
- **`gdp_per_capita.csv`**: Includes economic data, such as GDP per capita, unemployment rate, and total investment.

### Main Functions
- **`prepare_country_stats()`**: Cleans and integrates the data from both sources (OECD and economic data), generating a consolidated dataframe.
- **Visualization**: Generates scatter plots to analyze the correlations between indicators.

## Generated Visualizations

The project creates a figure with 6 scatter plots:

1. **GDP per capita vs Life Satisfaction**
2. **Unemployment Rate vs Life Satisfaction**
3. **Total Investment vs Life Satisfaction**
4. **GDP per capita vs Sense of Safety when Walking at Night (Female)**
5. **Unemployment Rate vs Sense of Safety when Walking at Night (Female)**
6. **Total Investment vs Sense of Safety when Walking at Night (Female)**

Each plot includes:
- Annotations of country names for easier identification.
- Distinct colors to differentiate the data sets.

## Dependencies

The libraries required to run the project are:

- **Matplotlib**: For generating plots.
- **Pandas**: For data manipulation and analysis.

Install the dependencies by running the `install_libraries.cmd` script.

## How to Run

1. Ensure that the files `oecd_bli.csv` and `gdp_per_capita.csv` are in the same folder as the script.
2. Run the script that installs the libraries (skip this step if the libraries are already installed).
3. Run the `run_script.vbs` script.
4. View the generated plots in an interactive Matplotlib window.
5. It is possible to zoom in and move each of the generated windows for better visualization.

## Usage Examples

This project can be used to:

- Analyze the impact of GDP per capita on life satisfaction.
- Identify relationships between economic indicators and perceived safety.
- Explore public policies in different countries based on quantitative data.

### Mini-reports
To contextualize and facilitate understanding with each plot, here is a direct explanation of each plotted chart:

![Data Analytics](https://github.com/user-attachments/assets/d12ad8c7-68ea-4ecb-a87a-3c6361148e99)

1. **Relationship between GDP per capita and Life Satisfaction (Blue Plot):**  
   This plot shows a positive correlation between GDP per capita and life satisfaction. As GDP per capita increases, life satisfaction tends to grow as well. This suggests that wealthier economies may offer better living conditions, which reflects on the population's happiness.

2. **Relationship between Unemployment Rate and Life Satisfaction (Red Plot):**  
   Here, a negative correlation is observed: as the unemployment rate increases, life satisfaction tends to decrease. This result highlights the impact of unemployment on quality of life and emotional well-being.

3. **Relationship between Total Investment and Life Satisfaction (Green Plot):**  
   The plot reveals a moderate relationship between the percentage of total investment in relation to GDP and life satisfaction. While not a clear linear relationship, higher investment levels seem to be associated with greater satisfaction.

4. **Relationship between GDP per capita and Safety when Walking at Night ('% Female') (Purple Plot):**  
   This plot suggests a positive correlation: countries with higher GDP per capita tend to have a greater perception of safety when walking at night among women. This may indicate that stronger economies invest more in infrastructure and public safety.

5. **Relationship between Unemployment Rate and Safety when Walking at Night ('% Female') (Orange Plot):**  
   The relationship between the unemployment rate and the perception of safety when walking at night among women appears to be negative. Regions with high unemployment rates tend to have lower feelings of safety, possibly due to adverse social conditions.

6. **Relationship between Total Investment and Safety when Walking at Night ('% Female') (Brown Plot):**  
   This plot suggests a positive correlation between total investment and the perception of safety when walking at night among women. This could indicate that targeted investments improve public safety and overall well-being.

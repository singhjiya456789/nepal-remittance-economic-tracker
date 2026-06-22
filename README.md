# Nepal Remittance Economic Tracker

## Overview

As a Nepali, I have always heard about how much the country earns from
remittances. I wanted to understand the real numbers — how much, how fast
it grew, and what major events shaped it.

This project analyzes Nepal's remittance inflow from 1993 to 2024 using
real World Bank data, SQL window functions, Python, and data visualization
— built as a portfolio project to demonstrate end-to-end data analysis skills.

---

## Data Source

The data was obtained from the World Bank's World Development Indicators
database. It covers two indicators for Nepal: personal remittances received
in current US dollars, and remittances as a percentage of GDP, spanning
32 years from 1993 to 2024.

- Source: [World Bank Open Data](https://data.worldbank.org)
- Indicators: `BX.TRF.PWKR.CD.DT` and `BX.TRF.PWKR.DT.GD.ZS`

---

## Tech Stack

- **Database:** MySQL
- **SQL Client:** MySQL Workbench
- **Language:** Python
- **Libraries:** SQLAlchemy, Pandas, Matplotlib

---

## Project Structure

## Project Structure

```
nepal-remittance-economic-tracker/
│
├── data/
│   └── remittance_by_year.csv        # Raw data from World Bank
│
├── sql/
│   ├── create_load.sql                # CREATE TABLE + INSERT statements
│   └── window_functions.sql           # RANK, LAG, Running Total, CTE queries
│
├── analysis.py                        # Python: MySQL connection + visualizations
│
├── visuals/
│   ├── remittance_trend.png          # Line chart: remittance growth over time
│   ├── remittance_pct_gdp.png        # Bar chart: remittance as % of GDP
│   └── yoy_change.png                # Bar chart: year-over-year % change
│
└── README.md
```

---

## Key Findings

1. **Nepal's remittances grew 205x over three decades** — from $54.8 million
   in 1993 to $11.25 billion in 2024, making it one of the fastest-growing
   remittance economies in the world.

2. **2002 saw a 361% single-year surge** — remittances jumped from $147M to
   $678M in one year, likely driven by a post-conflict migration boom as
   Nepalis left during the Maoist insurgency period.

3. **The 2015 earthquake year showed rising remittances** — contrary to
   expectations, remittances increased to $6.73B in 2015, suggesting Nepali
   migrants abroad sent more money home during the crisis. This matches the
   well-documented "shock-absorber" effect of remittances in developing economies.

4. **Nepal crossed 10% of GDP dependency around 2002** — and has never
   dropped below it since, reaching a peak of 27.6% in 2015.

5. **Cumulative remittances since 1993 total over $121 billion** — exceeding
   Nepal's current annual GDP several times over.

6. **62% of all years (20 out of 32) showed greater than 10% annual growth**
   — confirmed through SQL window function analysis using LAG() and CTE.

---

## Visualizations

### Remittance Growth Over Time

![Remittance Trend](visuals/remittance_trend.png)

### Remittance as % of GDP

![% of GDP](visuals/remittance_pct_gdp.png)

### Year-over-Year % Change

![YoY Change](visuals/yoy_change.png)

---

## How to Run

1. **Clone the repository**

```bash
git clone https://github.com/singhjiya456789/nepal-remittance-economic-tracker
cd nepal-remittance-economic-tracker
```

2. **Set up the MySQL database**
   - Open MySQL Workbench
   - Run `sql/01_create_and_load.sql` to create and populate the table

3. **Install Python dependencies**

```bash
pip install sqlalchemy pymysql pandas matplotlib
```

4. **Update your credentials in `analysis.py`**

```python
engine = create_engine("mysql+pymysql://your_username:your_password@localhost/jiya")
```

5. **Run the analysis**

```bash
python analysis.py
```

Charts will be saved automatically to the `visuals/` folder.

---

## Author

**Jiya Singh**

- 🎓 Computer Engineering Student | Purwanchal University, Nepal
- 💡 Aspiring Data Scientist
- GitHub: [singhjiya456789](https://github.com/singhjiya456789)

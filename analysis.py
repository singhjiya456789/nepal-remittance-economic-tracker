from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

engine = create_engine("mysql+pymysql://root:123456@localhost/jiya")

query = "SELECT * FROM remittance_by_year ORDER BY yr;"
df = pd.read_sql(query, engine)

print(df)


plt.figure(figsize=(12, 6))
plt.plot(df['yr'], df['remittance_usd'] / 1e9, marker='o', color='#2c7fb8', linewidth=2)

plt.title('Nepal Remittance Inflow (1993–2024)', fontsize=14, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Remittance (Billion US$)')
plt.grid(True, alpha=0.3)
plt.annotate('2015 Earthquake',          
             xy=(2015, 6.73),            
             xytext=(2010, 9),  
             arrowprops=dict(arrowstyle='->', color='gray'),  # draws the arrow connecting them
             fontsize=9)

plt.annotate('2020 COVID-19',
             xy= (2020,8.11),
             xytext=(2022,6),
             arrowprops=dict(arrowstyle='->', color='gray'),
             fontsize=9)

plt.savefig('visuals/remittance_trend.png', dpi=300, bbox_inches='tight')
plt.show()

plt.figure(figsize=(12, 6))
plt.bar(df['yr'], df['pct_gdp'], color='#d95f02')

plt.title('Nepal: Remittances as % of GDP (1993–2024)', fontsize=14, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('% of GDP')
plt.grid(True, axis='y', alpha=0.3)

plt.axhline(y=10, color='gray', linestyle='--', linewidth=1)
plt.text(1994, 10.5, 'World Bank "high dependency" threshold (~10%)', fontsize=8, color='gray')

plt.savefig('visuals/remittance_pct_gdp.png', dpi=300, bbox_inches='tight')
plt.show()



df['yoy_change'] = df['remittance_usd'].pct_change() * 100

plt.figure(figsize=(12, 6))
colors = ['green' if x >= 0 else 'red' for x in df['yoy_change']]
plt.bar(df['yr'], df['yoy_change'], color=colors)

plt.title('Nepal Remittance: Year-over-Year % Change (1994–2024)', fontsize=14, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('% Change from Previous Year')
plt.axhline(y=0, color='black', linewidth=0.8)
plt.grid(True, axis='y', alpha=0.3)

plt.savefig('visuals/yoy_change.png', dpi=300, bbox_inches='tight')
plt.show()


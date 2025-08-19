# Forex-Exchange-Rates-Dashboard-Analysis
Problem Statement
Foreign exchange rate fluctuations directly affect international trade, investments, and risk management. Businesses need clear insights on which currencies are appreciating, depreciating, or highly volatile in order to make informed decisions.
Approach
1. Data Collection & Preparation
- Used a real dataset (daily_forex_rates.csv) with daily rates across multiple currencies from Kaggle
- Cleaned and transformed data using Pandas (date formatting, normalization, calculations).
2. Dashboard Development (2 versions)
- Forex.py → Interactive file-upload version for ad-hoc analysis.
- forexup.py → Cached, production-ready dashboard pulling data from local source.
- Built with Streamlit + Plotly to allow exploration of:
  * Trend analysis (time series)
  * Gainers & losers (% change)
  * Volatility ranking (std dev)
  * Heatmaps for comparative analysis
3. Business Insight Extraction
- Calculated % changes, highest/lowest values, volatility ranks.
- Created a management-style PowerPoint report summarizing findings.
Key Insights
- Top Gainers: BTC (+203.9%), CHF (+62.6%), Gold (+52.3%) → safe havens & crypto performed strongly.
- Top Losers: VEF, ARS, SDG, LBP, VES → currencies hit by hyperinflation/devaluation.
- Volatility Leaders: VEF, VES, LBP, SLL → unstable economies pose the highest FX risk.
- Business Implication:
  * Hedge exposure to volatile currencies.
  * Consider safe-haven assets during market uncertainty.
  * Inform global payment & investment strategies.
<img width="1783" height="719" alt="Screenshot 2025-08-19 151419" src="https://github.com/user-attachments/assets/734011fb-a8ef-4da8-9723-898a11302531" />
<img width="1770" height="646" alt="Screenshot 2025-08-19 151432" src="https://github.com/user-attachments/assets/c3f7242b-6a83-459c-9607-0a15fc26ce0b" />
<img width="1790" height="667" alt="Screenshot 2025-08-19 151444" src="https://github.com/user-attachments/assets/4a69e2a2-fa6a-414d-82d3-94e4c4400147" />
<img width="1783" height="695" alt="Screenshot 2025-08-19 151455" src="https://github.com/user-attachments/assets/a877fa9e-06de-4262-b556-11ddf739d0d2" />
<img width="1740" height="639" alt="Screenshot 2025-08-19 151506" src="https://github.com/user-attachments/assets/371b662b-5f58-4895-8bfe-4278ce75f906" />


Delivered a professional, end-to-end analytics solution: - Interactive dashboards for live exploration. - Written report + PowerPoint for management decisions. - Showcased business impact of analytics in finance &amp; risk management.

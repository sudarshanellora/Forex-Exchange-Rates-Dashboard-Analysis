# Forex-Exchange-Rates-Dashboard-Analysis
Problem Statement
Foreign exchange rate fluctuations directly affect international trade, investments, and risk management. Businesses need clear insights on which currencies are appreciating, depreciating, or highly volatile in order to make informed decisions.
Approach
1. Data Collection & Preparation
- Used a real dataset (daily_forex_rates.csv) with daily rates across multiple currencies.
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


Delivered a professional, end-to-end analytics solution: - Interactive dashboards for live exploration. - Written report + PowerPoint for management decisions. - Showcased business impact of analytics in finance &amp; risk management.

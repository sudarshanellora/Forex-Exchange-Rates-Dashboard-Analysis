import pandas as pd

# Load your dataset (adjust path if needed)
df = pd.read_csv("daily_forex_rates.csv")

# Ensure date column is parsed correctly
df['date'] = pd.to_datetime(df['date'], dayfirst=True)

# Quick check
print(df.head())



# df is your filtered dataframe (date-filtered)
summary = (
    df.groupby("currency")
      .apply(lambda x: (x["exchange_rate"].iloc[-1] - x["exchange_rate"].iloc[0]) / x["exchange_rate"].iloc[0] * 100)
      .reset_index(name="percent_change")
)
top5_up = summary.sort_values("percent_change", ascending=False).head(5)
top5_down = summary.sort_values("percent_change").head(5)
print("Top 5 gainers\n", top5_up)
print("Top 5 losers\n", top5_down)


vol = (
    df.groupby("currency")["exchange_rate"]
      .std()
      .reset_index(name="volatility")
      .sort_values("volatility", ascending=False)
)

print("Top 10 most volatile currencies:\n", vol.head(10))
high_low = df.groupby("currency")["exchange_rate"].agg(["min", "max"]).reset_index()
print("Currencies with highest max rates:\n", high_low.sort_values("max", ascending=False).head(10))
print("\nCurrencies with lowest min rates:\n", high_low.sort_values("min").head(10))


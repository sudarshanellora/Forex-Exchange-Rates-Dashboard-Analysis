import streamlit as st
import pandas as pd
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

# ===============================
# Page Config
# ===============================
st.set_page_config(page_title="Forex Exchange Rates Since 2004", page_icon=":bar_chart:", layout="wide")
st.title("💱 Forex Exchange Rates Since 2004")
st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)

# ===============================
# Load Data
# ===============================
@st.cache_data
def load_data():
    df = pd.read_csv("daily_forex_rates.csv", encoding="ISO-8859-1")
    df.columns = df.columns.str.lower()
    df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y", dayfirst=True)
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("❌ daily_forex_rates.csv not found. Please upload or place the file in the working directory.")
    st.stop()

# ===============================
# Sidebar Filters
# ===============================
st.sidebar.header("Filters")

# Date filter
startDate = df["date"].min()
endDate = df["date"].max()
date_range = st.sidebar.date_input("Select Date Range", [startDate, endDate])

if len(date_range) == 2:
    date1, date2 = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    df = df[(df["date"] >= date1) & (df["date"] <= date2)].copy()

# Currency filter
currency = st.sidebar.multiselect("Pick your Currency", df["currency"].unique())
if currency:
    df = df[df["currency"].isin(currency)]

# Base Currency filter
base_currency = st.sidebar.multiselect(
    "Pick the Base Currency",
    options=df["base_currency"].unique(),
    default=df["base_currency"].unique()
)
if base_currency:
    df = df[df["base_currency"].isin(base_currency)]

# ===============================
# Dashboard Visualizations
# ===============================
if df.empty:
    st.warning("⚠ No data available for the selected filters.")
    st.stop()

# --- Trend Over Time ---
st.subheader("📈 Exchange Rate Trend Over Time")
fig1 = px.line(df, x="date", y="exchange_rate", color="currency",
               labels={"exchange_rate": "Exchange Rate", "currency": "Currency"},
               hover_data=["currency_name"])
st.plotly_chart(fig1, use_container_width=True)

# --- High & Low ---
st.subheader("🔼🔽 Highest & Lowest Exchange Rates")
high_low = df.groupby("currency")["exchange_rate"].agg(["min", "max"]).reset_index()
fig2 = px.bar(high_low, x="currency", y="max", color="currency", title="Maximum Exchange Rate")
st.plotly_chart(fig2, use_container_width=True)

# --- % Change ---
st.subheader("📊 Overall % Change in Selected Period")
summary = (
    df.groupby("currency")
    .apply(lambda x: (x["exchange_rate"].iloc[-1] - x["exchange_rate"].iloc[0]) / x["exchange_rate"].iloc[0] * 100)
    .reset_index(name="percent_change")
)
fig3 = px.bar(summary, x="currency", y="percent_change", color="percent_change",
              color_continuous_scale="RdBu", labels={"percent_change": "% Change"})
st.plotly_chart(fig3, use_container_width=True)

# --- Volatility ---
st.subheader("📉 Currency Volatility Ranking (Std. Dev.)")
volatility_summary = (
    df.groupby("currency")["exchange_rate"]
    .std()
    .reset_index(name="volatility")
    .sort_values(by="volatility", ascending=False)
)
fig4 = px.bar(volatility_summary, x="currency", y="volatility", color="volatility",
              color_continuous_scale="Viridis", labels={"volatility": "Std. Dev. of Exchange Rate"})
st.plotly_chart(fig4, use_container_width=True)

# --- Heatmap ---
st.subheader("🌡 Heatmap of Exchange Rates")
heatmap_data = df.pivot_table(index="date", columns="currency", values="exchange_rate")
fig5 = px.imshow(heatmap_data.T, aspect="auto", color_continuous_scale="Viridis",
                 labels=dict(x="Date", y="Currency", color="Exchange Rate"))
st.plotly_chart(fig5, use_container_width=True)

# --- Footer ---
st.markdown("---")
st.markdown("👨‍💻 Dashboard developed by **Sudarshan E**")


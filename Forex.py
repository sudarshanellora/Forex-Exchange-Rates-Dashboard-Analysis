import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Forex Exchange Rates Since 2004", page_icon=":bar_chart:",layout="wide")
st.title(" :bar_chart: Forex Exchange Rates Since 2004")
st.markdown('<style>div.block-container{padding-top:3rem;}</style>',unsafe_allow_html=True)

#Input
fl = st.file_uploader(":file_folder: Upload a file",type=(["csv","txt","xlsx","xls"]))
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename, encoding = "ISO-8859-1")
else:
    os.chdir(r"F:\Forex_exchange\archive")
    df = pd.read_csv("daily_forex_rates.csv", encoding = "ISO-8859-1")

# Normalize column names to lowercase (avoids case mismatch issues)
df.columns = df.columns.str.lower()

#date
col1, col2 = st.columns(2)

# Convert date column correctly
df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y", dayfirst=True)

# Getting the min and max date 
startDate = df["date"].min()
endDate = df["date"].max()

with col1:
    date1 = pd.to_datetime(st.date_input("Start date", startDate))

with col2:
    date2 = pd.to_datetime(st.date_input("End date", endDate))

# Filter based on date selection
df = df[(df["date"] >= date1) & (df["date"] <= date2)].copy()



#Currency filter
st.sidebar.header("Choose your filter: ")
currency = st.sidebar.multiselect("Pick your currency", df["currency"].unique())
if not currency:
    df2 = df.copy()
else:
    df2 = df[df["currency"].isin(currency)]


# Sidebar multiselect for Base Currency
base_currency = st.sidebar.multiselect(
    "Pick the Base Currency",
    options=df2["base_currency"].unique(),
    default=df2["base_currency"].unique()  # Pre-selects the only available currency
)

# If no selection, fallback to all available currencies
if len(base_currency) == 0:
    df3 = df2.copy()
else:
    df3 = df2[df2["base_currency"].isin(base_currency)]


# ===============================
# Data Visualizations
# ===============================

st.subheader("Exchange Rate Trend Over Time")
fig1 = px.line(
    df3,
    x="date",
    y="exchange_rate",
    color="currency",
    title="Exchange Rate Trend",
    labels={"exchange_rate": "Exchange Rate", "currency": "Currency"},
    hover_data=["currency_name"]
)
st.plotly_chart(fig1, use_container_width=True)

# ---------------------------------
st.subheader("Highest & Lowest Exchange Rates in Selected Period")
high_low = df3.groupby("currency")["exchange_rate"].agg(["min", "max"]).reset_index()
fig2 = px.bar(
    high_low,
    x="currency",
    y="max",
    color="currency",
    title="Maximum Exchange Rate by Currency",
    labels={"max": "Max Exchange Rate"}
)
st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------
st.subheader("Daily % Change Heatmap")
df3["pct_change"] = df3.groupby("currency")["exchange_rate"].pct_change() * 100
fig3 = px.density_heatmap(
    df3,
    x="date",
    y="currency",
    z="pct_change",
    color_continuous_scale="RdBu",
    title="Daily % Change Heatmap"
)
st.plotly_chart(fig3, use_container_width=True)

# ---------------------------------
st.subheader("Overall % Change in Selected Period")
summary = (
    df3.groupby("currency")
    .apply(lambda x: (x["exchange_rate"].iloc[-1] - x["exchange_rate"].iloc[0]) / x["exchange_rate"].iloc[0] * 100)
    .reset_index(name="percent_change")
)
fig4 = px.bar(
    summary,
    x="currency",
    y="percent_change",
    color="percent_change",
    color_continuous_scale="RdBu",
    title="Overall % Change in Selected Period",
    labels={"percent_change": "% Change"}
)
st.plotly_chart(fig4, use_container_width=True)

# ---------------------------------

st.subheader("Currency Volatility Ranking (Std. Dev.)")

# Calculate volatility as standard deviation of exchange rates
volatility_summary = (
    df3.groupby("currency")["exchange_rate"]
    .std()
    .reset_index(name="volatility")
    .sort_values(by="volatility", ascending=False)
)

fig_volatility = px.bar(
    volatility_summary,
    x="currency",
    y="volatility",
    color="volatility",
    color_continuous_scale="Viridis",
    title="Currency Volatility Ranking",
    labels={"volatility": "Standard Deviation of Exchange Rate"}
)

st.plotly_chart(fig_volatility, use_container_width=True)
st.subheader("Heatmap of Exchange Rates")

# Prepare data for heatmap
heatmap_data = df3.pivot_table(
    index="date",
    columns="currency",
    values="exchange_rate"
).reset_index()

heatmap_long = heatmap_data.melt(
    id_vars="date",
    var_name="currency",
    value_name="exchange_rate"
)

# Create heatmap
fig_heatmap = px.density_heatmap(
    heatmap_long,
    x="currency",
    y="date",
    z="exchange_rate",
    color_continuous_scale="Viridis",
    title="Exchange Rate Heatmap",
    labels={"exchange_rate": "Rate"}
)

st.plotly_chart(fig_heatmap, use_container_width=True)


st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        right: 0;
        padding: 10px;
        font-size: 12px;
        color: grey;
        background: white;
        opacity: 0.8;
    }
    </style>
    <div class="footer">Author: Sudarshan Ellora</div>
    """,
    unsafe_allow_html=True
)


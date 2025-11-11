import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Profit Lattice Demo", layout="wide")
st.title("📊 Profit Lattice – Demo Dashboard")
st.caption("Educational demo: no trading or personal data.")

# Simulated dataset
np.random.seed(42)
dates = pd.date_range(end=pd.Timestamp.now(), periods=240, freq="H")
df = pd.DataFrame({
    "timestamp": dates,
    "price": np.cumsum(np.random.randn(len(dates))) + 100,
    "volume": np.random.rand(len(dates)) * 1000
}).set_index("timestamp")

st.line_chart(df["price"])
st.bar_chart(df["volume"])

st.subheader("Simulated Metrics")
st.write({
    "Volatility_%": round(df["price"].pct_change().std()*100, 2),
    "Avg_Volume": round(df["volume"].mean(), 2),
    "Data_Points": len(df)
})

st.info("🚀 For learning purposes only. No signals or execution.")

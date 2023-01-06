import streamlit as st
import pandas as pd
import matplotlib.pylab as plt

st.title("BigMac Index")


@st.cache
def load_data():
    """
    Helper function to load data
    """
    data = pd.read_csv("./data/big_mac.csv")
    return data.assign(date=lambda d: pd.to_datetime(d["date"]))


df = load_data()

countries = st.sidebar.multiselect("Select Countries", df["name"].unique())

varname = st.sidebar.selectbox("Select Column", ("local_price", "dollar_price"))

subset_df = df.loc[lambda d: d["name"].isin(countries)]

for name in countries:
    plotset = subset_df.loc[lambda d: d["name"] == name]
    plt.plot(plotset["date"], plotset[varname], label=name)
plt.legend()
st.pyplot(plt)

if st.sidebar.checkbox("Show Raw Data"):
    st.markdown("### Raw Data")
    st.write(subset_df)

import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "Miesiąc": ["Styczeń","Luty","Marzec","Kwiecień"],
    "Sprzedaż": [1000,1200,900,1500],
    "Koszty": [800,900,1000,950]
})

df["Zysk"] = df["Sprzedaż"] - df["Koszty"]

st.set_page_config(
    page_title="Aplikacja finansowa",
    layout="wide",
)
st.title("Aplikacja Finansowa")
st.write("Zaawansowany program dla księgowości")

#Side bar
st.sidebar.header("Preferences")
showTable = st.sidebar.checkbox("Show data table",value=False)
selectedColumn = st.sidebar.selectbox(
    "Wybierz kolumnę do wykresu",
    ["Sprzedaż", "Koszty", "Zysk"]
)

#kafelki
col1,col2,col3 = st.columns(3)
with col1:
    col1_value = df["Sprzedaż"].sum()
    st.metric("Łączna sprzedaż",f"{col1_value} zł")
with col2:
    col2_value = df["Koszty"].sum()
    st.metric("Łączne Koszty",f"{col2_value} zł")
with col3:
    col3_value = df["Zysk"].sum()
    st.metric("Łączny Zysk",f"{col3_value} zł")

#tabelka
if showTable:
    st.subheader("Data Table")
    st.dataframe(df, use_container_width=True)

#wykres liniowy
st.subheader("Wykres Liniowy")
st.write("Do wyboru z menu")
st.line_chart(df, x="Miesiąc", y=selectedColumn)

#file uploader
upload_file = st.sidebar.file_uploader("Upload your file",type=['.xlsx','.csv'])

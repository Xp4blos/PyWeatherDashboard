import pandas as pd
import streamlit as st
from google.protobuf import timestamp


def paramsMapping(pl):
    params = {
        "Wilgotność":"humidity",
        "Ciśnienie":"pressure",
        "Prędkość Wiatru":"wind_speed"
    }

    value = params[pl]
    return value


def render_dashboard(filepath):
    df= pd.read_excel(filepath)

    st.set_page_config(layout="wide", page_title="Aplikacja Pogodowa")


    ##Side bar
    st.sidebar.header("Konfiguracja")
    selected_column = st.sidebar.selectbox(
        "Wybierz kolumnę do wykresu",
        ["Wilgotność", "Ciśnienie", "Prędkość Wiatru"]
    )

    show_table = st.sidebar.checkbox("Pokaż tabelę",False)



    last_row = df.iloc[-1]
    st.title("Panel Pogodowy")
    st.divider()
    st.subheader("Aktualne informacje")

    col1,col2,col3,col4 = st.columns(4)


    with col1:
        if "temp" in last_row:
            col1.metric("Temperatura", f"{last_row["temp"]}  C")

    with col2:
        if "humidity" in last_row:
            col2.metric("Wilgotność", f"{last_row["humidity"]}  %")

    with col3:
        if "wind_speed" in last_row:
            col3.metric("Wiatr", f"{last_row["wind_speed"]}  m/s")

    with col4:
        if "pressure" in last_row:
            col4.metric("Ciśnienie", f"{last_row["pressure"]}  hPa")

    st.divider()

    st.subheader("Statystyki")

    stats_cols = st.columns(4)


    with stats_cols[0]:
        if "temp" in df.columns:
            stats_cols[0].info(
                f"Średnia temperatura: {df['temp'].mean():.2f} C \n \n"
                f"Minimalna temperatura: {df['temp'].min():.2f} C \n \n"               
                f"Maksymalna temperatura: {df['temp'].max():.2f} C \n \n"
            )

    with stats_cols[1]:
        if "humidity" in df.columns:
            stats_cols[1].info(
                f"Średnia wilgotność: {df['humidity'].mean():.2f} % \n \n"
                f"Minimalna wilgotność: {df['humidity'].min():.2f} % \n \n"
                f"Maksymalna wilgotność: {df['humidity'].max():.2f} % \n"
            )
    with stats_cols[2]:
        if "pressure" in df.columns:
            stats_cols[2].info(
                f"Średnie ciśnienie: {df['pressure'].mean():.2f} hPa \n \n"
                f"Minimalne ciśnienie: {df['pressure'].min():.2f} hPa \n \n"
                f"Maksymalne ciśnienie: {df['pressure'].max():.2f} hPa \n"
            )
    with stats_cols[3]:
        if "temp" in df.columns:
            stats_cols[3].info(
                f"Średnia prędkość wiatru: {df['wind_speed'].mean():.2f} m/s \n \n"
                f"Minimalna prędkość wiatru: {df['wind_speed'].min():.2f} m/s \n \n"
                f"Maksymalna prędkość wiatru: {df['wind_speed'].max():.2f} m/s \n"
            )
    st.divider()

    st.subheader("Wykresy")

    chart = st.columns(2)
    with chart[0]:
        if "temp" in df.columns:
            st.markdown("**Temperatura w Czasie**")
            st.line_chart(df, x="timestamp", y=["temp","feels_like"], color=['red','blue'],
                          x_label="Data",
                          y_label="Temperatura")
    with chart[1]:
        if paramsMapping(selected_column) in df.columns:
            st.markdown(f"**{selected_column} w Czasie**")
            st.line_chart(df, x="timestamp", y=[paramsMapping(selected_column)],
                          x_label="Data"
                        )

    if show_table:
        st.divider()
        st.subheader("Wszystkie dane")
        st.dataframe(df)

    st.divider()
    st.subheader("Tabelki")
    st.dataframe(df.tail(10), use_container_width=True)
    st.markdown("**Opis Statystyczny**")

    numeric_df = df.select_dtypes(include="number")
    if not numeric_df.empty:
        st.dataframe(numeric_df.describe(), use_container_width=True)


    ##Sekcja


    st.divider()
    st.subheader("Wykresy")

    # --- PRZYGOTOWANIE DANYCH (Raz dla obu wykresów) ---
    # Upewniamy się, że timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['month_num'] = df['timestamp'].dt.month
    df['month_name'] = df['timestamp'].dt.month_name()

    # Tworzymy listę miesięcy w poprawnej kolejności (1-12), aby użyć jej do kategoryzacji
    # To załatwi problem sortowania raz a dobrze
    month_order = df.sort_values('month_num')['month_name'].unique()

    # --- KOLUMNY ---
    wykres = st.columns(2)


    with wykres[0]:
        st.markdown('**Wilgotność w miesiącach**')
        # Grupowanie
        df_hum = df.groupby(['month_num', 'month_name'])['humidity'].mean().reset_index()
        # Wymuszenie kolejności kategorycznej
        df_hum['month_name'] = pd.Categorical(df_hum['month_name'], categories=month_order, ordered=True)
        df_hum = df_hum.sort_values('month_num')

        st.bar_chart(
            df_hum,
            x='month_name',  # Podajemy nazwę kolumny, nie listę!
            y='humidity',
            x_label="Miesiąc",
            y_label="wilgotność [%]"
        )

    with wykres[1]:
        st.markdown('**Temperatura w miesiącach**')
        # Grupowanie
        df_temp = df.groupby(['month_num', 'month_name'])['temp'].mean().reset_index()
        # Wymuszenie kolejności kategorycznej
        df_temp['month_name'] = pd.Categorical(df_temp['month_name'], categories=month_order, ordered=True)
        df_temp = df_temp.sort_values('month_num')

        st.bar_chart(
            df_temp,
            x='month_name',
            y='temp',
            x_label="Miesiąc",
            y_label="temperatura [°C]"
        )
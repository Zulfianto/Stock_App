import pyrebase
import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import pandas_ta as ta
from datetime import timedelta
import warnings


def data_frame(input_value):
    df = yf.download(tickers=input_value, period="5d", interval='1m')
    df['SMA20'] = df.ta.sma(length=20)
    df['SMA12'] = df.ta.sma(length=12)
    df['EMA8'] = df.ta.ema(length=8)
    df['BBL_20_2.0'] = df.ta.bbands(length=20)['BBL_20_2.0']
    df['BBU_20_2.0'] = df.ta.bbands(length=20)['BBU_20_2.0']
    df['RSI'] = df.ta.rsi(length=14)
    df['MACD_12_26_9'] = df.ta.macd(fast=12, slow=26, signal=9)['MACD_12_26_9']
    df['MACDh_12_26_9'] = df.ta.macd(fast=12, slow=26, signal=9)['MACDh_12_26_9']
    df['MACDs_12_26_9'] = df.ta.macd(fast=12, slow=26, signal=9)['MACDs_12_26_9']
    df['SUPERTl_7_3.0'] = df.ta.supertrend(length=7, multiplier=3)['SUPERTl_7_3.0']
    df['SUPERTs_7_3.0'] = df.ta.supertrend(length=7, multiplier=3)['SUPERTs_7_3.0']
    df['SUPERTl_14_5.0'] = df.ta.supertrend(length=14, multiplier=5)['SUPERTl_14_5.0']
    df['SUPERTs_14_5.0'] = df.ta.supertrend(length=14, multiplier=5)['SUPERTs_14_5.0']
    df['SUPERTl_14_4.5'] = df.ta.supertrend(length=14, multiplier=4.5)['SUPERTl_14_4.5']
    df['SUPERTs_14_4.5'] = df.ta.supertrend(length=14, multiplier=4.5)['SUPERTs_14_4.5']
    df['VWAP_D'] = df.ta.vwap()
    df['PSARl_0.02_0.2'] = df.ta.psar(af0=0.02, af=0.02, max_af=0.2)['PSARl_0.02_0.2']
    df['PSARs_0.02_0.2'] = df.ta.psar(af0=0.02, af=0.02, max_af=0.2)['PSARs_0.02_0.2']
    df['STOCHk_14_3_3'] = df.ta.stoch(k=14, d=3, smooth_k=3)['STOCHk_14_3_3']
    df['STOCHd_14_3_3'] = df.ta.stoch(k=14, d=3, smooth_k=3)['STOCHd_14_3_3']
    df['Last_Close'] = df.Close[-1].round(decimals=2)
    return df


def data_frame1(input_value):
    df = yf.download(tickers=input_value, period="5d", interval='5m')
    df['SMA20'] = df.ta.sma(length=20)
    df['SMA12'] = df.ta.sma(length=12)
    df['EMA8'] = df.ta.ema(length=8)
    df['BBL_20_2.0'] = df.ta.bbands(length=20)['BBL_20_2.0']
    df['BBU_20_2.0'] = df.ta.bbands(length=20)['BBU_20_2.0']
    df['RSI'] = df.ta.rsi(length=14)
    df['MACD_12_26_9'] = df.ta.macd(fast=12, slow=26, signal=9)['MACD_12_26_9']
    df['MACDh_12_26_9'] = df.ta.macd(fast=12, slow=26, signal=9)['MACDh_12_26_9']
    df['MACDs_12_26_9'] = df.ta.macd(fast=12, slow=26, signal=9)['MACDs_12_26_9']
    df['SUPERTl_7_3.0'] = df.ta.supertrend(length=7, multiplier=3)['SUPERTl_7_3.0']
    df['SUPERTs_7_3.0'] = df.ta.supertrend(length=7, multiplier=3)['SUPERTs_7_3.0']
    df['SUPERTl_14_5.0'] = df.ta.supertrend(length=14, multiplier=5)['SUPERTl_14_5.0']
    df['SUPERTs_14_5.0'] = df.ta.supertrend(length=14, multiplier=5)['SUPERTs_14_5.0']
    df['SUPERTl_14_4.5'] = df.ta.supertrend(length=14, multiplier=4.5)['SUPERTl_14_4.5']
    df['SUPERTs_14_4.5'] = df.ta.supertrend(length=14, multiplier=4.5)['SUPERTs_14_4.5']
    df['VWAP_D'] = df.ta.vwap()
    df['PSARl_0.02_0.2'] = df.ta.psar(af0=0.02, af=0.02, max_af=0.2)['PSARl_0.02_0.2']
    df['PSARs_0.02_0.2'] = df.ta.psar(af0=0.02, af=0.02, max_af=0.2)['PSARs_0.02_0.2']
    df['STOCHk_14_3_3'] = df.ta.stoch(k=14, d=3, smooth_k=3)['STOCHk_14_3_3']
    df['STOCHd_14_3_3'] = df.ta.stoch(k=14, d=3, smooth_k=3)['STOCHd_14_3_3']
    df['Last_Close'] = df.Close[-1].round(decimals=2)
    return df


def data_frame2(input_value):
    df = yf.download(tickers=input_value, period="6d", interval='15m')
    df['BBL_20_2.0'] = df.ta.bbands(length=20)['BBL_20_2.0']
    df['BBU_20_2.0'] = df.ta.bbands(length=20)['BBU_20_2.0']
    df['RSI'] = df.ta.rsi(length=14)
    df['PSARl_0.02_0.2'] = df.ta.psar(af0=0.02, af=0.02, max_af=0.2)['PSARl_0.02_0.2']
    df['PSARs_0.02_0.2'] = df.ta.psar(af0=0.02, af=0.02, max_af=0.2)['PSARs_0.02_0.2']
    return df

warnings.simplefilter('ignore', UserWarning)

def candlestick(input_value):
    df = data_frame(input_value=stock)
    df1 = data_frame1(input_value=stock)
    data = go.Figure()

    data.add_trace(go.Candlestick(
        x=df.index[-80:],
        open=df.Open[-80:],
        high=df.High[-80:],
        low=df.Low[-80:],
        close=df.Close[-80:],
        name='candlestick', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df1.index[-16:],
        y=df1.SMA20[-16:],
        name='SMA20',
        mode='lines',
        line=dict(color='orange', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df.SMA12[-80:],
        name='SMA12',
        mode='lines',
        line=dict(color='red', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df.EMA8[-80:],
        name='EMA8',
        mode='lines',
        line=dict(color='blue', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['BBL_20_2.0'][-80:],
        name='BBL',
        mode='lines',
        line=dict(color='black', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['BBU_20_2.0'][-80:],
        name='BBU',
        mode='lines',
        line=dict(color='black', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df1.index[-16:],
        y=df1['BBL_20_2.0'][-16:],
        name='BBL',
        mode='lines',
        line=dict(color='orange', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df1.index[-16:],
        y=df1['BBU_20_2.0'][-16:],
        name='BBU',
        mode='lines',
        line=dict(color='orange', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['PSARl_0.02_0.2'][-80:],
        name='PSARL',
        mode='markers', marker=dict(
            color="black", opacity=1,
            size=6), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['PSARs_0.02_0.2'][-80:],
        name='PSARS',
        mode='markers', marker=dict(
            color="black", opacity=1,
            size=6), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df1.index[-16:],
        y=df1['PSARl_0.02_0.2'][-16:],
        name='PSARL',
        mode='markers', marker=dict(
            color="green", opacity=1,
            size=6), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df1.index[-16:],
        y=df1['PSARs_0.02_0.2'][-16:],
        name='PSARS',
        mode='markers', marker=dict(
            color="red", opacity=1,
            size=6), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['VWAP_D'][-80:],
        name='VWAP',
        mode='lines',
        line=dict(color='purple', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['SUPERTl_7_3.0'][-80:],
        name='SUPERTl',
        mode='lines',
        line=dict(color='green', width=2), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['SUPERTs_7_3.0'][-80:],
        name='SUPERTs',
        mode='lines',
        line=dict(color='red', width=2), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['SUPERTl_14_5.0'][-80:],
        name='SUPERTl',
        mode='lines',
        line=dict(color='green', width=2), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['SUPERTs_14_5.0'][-80:],
        name='SUPERTs',
        mode='lines',
        line=dict(color='red', width=2), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['RSI'][-80:],
        name='RSI',
        mode='lines',
        line=dict(color='black', width=3), yaxis="y2"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['STOCHk_14_3_3'][-80:],
        name='STOCHk_14_3_3',
        mode='lines',
        line=dict(color='blue', width=3), yaxis="y2"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['STOCHd_14_3_3'][-80:],
        name='STOCHd_14_3_3',
        mode='lines',
        line=dict(color='red', width=3), yaxis="y2"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['MACD_12_26_9'][-80:],
        name='mACD',
        mode='lines',
        line=dict(color='blue', width=3), yaxis="y1"))

    data.add_trace(go.Bar(
        x=df.index[-80:],
        y=df['MACDh_12_26_9'][-80:],
        name='MACDh', marker={'color': 'red'},
        yaxis="y1"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['MACDs_12_26_9'][-80:],
        name='MACDs',
        mode='lines',
        line=dict(color='red', width=3), yaxis="y1"))

    data.add_shape(type='line', x0=df.index[-80], y0=df['Close'][-1],
                   x1=df.index[-1], y1=df['Close'][-1], line=dict(color='green', width=0.5, dash='dot'),
                   xref="x",
                   yref='y3')

    data.add_shape(type="rect", x0=df.index[-80], y0=70, x1=df.index[-1], y1=100, fillcolor="red",
                   opacity=0.2,
                   xref="x", yref='y2')
    data.add_shape(type="rect", x0=df.index[-80], y0=30, x1=df.index[-1], y1=70, fillcolor="blue",
                   opacity=0.2,
                   xref="x", yref='y2')
    data.add_shape(type="rect", x0=df.index[-80], y0=0, x1=df.index[-1], y1=30, fillcolor="green",
                   opacity=0.2,
                   xref="x", yref='y2')
    data.add_shape(type='line', x0=df.index[-80], y0=50,
                   x1=df.index[-1], y1=50, line=dict(color='black', width=0.5, dash='dot'), xref="x",
                   yref='y2')

    data.add_annotation(
        x=df.index[-1],
        y=df['Close'][-1],
        xref="x",
        yref="y3",
        text=df['Last_Close'][-1],
        showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=11,
            color="#ffffff"
        ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        ax=30,
        ay=0,
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="green",
        opacity=0.8, )

    data.update_layout(
        autosize=True,
        # width=1500,
        paper_bgcolor='#F5F5F5',
        plot_bgcolor='white',
        height=670,
        margin=dict(t=0, l=0, r=0, b=0),
        xaxis=dict(range=[df.index[-80], df.index[-1] + timedelta(minutes=6)], rangeslider_visible=False,
                   rangebreaks=[
                       dict(bounds=["sat", "mon"]),
                       dict(bounds=[16, 9.5], pattern="hour"),
                       # dict(values=["2021-11-25", ])
                   ]),
        yaxis1=dict(domain=[0, 0.2], side='right', linecolor='grey', linewidth=0.01, gridwidth=0.001,
                    gridcolor='grey', ),
        yaxis2=dict(domain=[0.2, 0.4], side='right', linecolor='grey', linewidth=0.01, ),
        yaxis3=dict(domain=[0.4, 1], side='right', showgrid=True,
                    gridwidth=0.001, gridcolor='grey', linecolor='grey', linewidth=0.01), showlegend=False,


    )
    chart2.plotly_chart(data, use_container_width=True)


def candlestick1(input_value):
    df = data_frame1(input_value=stock)
    df1 = data_frame2(input_value=stock)
    data = go.Figure()

    data.add_trace(go.Candlestick(
        x=df.index[-60:],
        open=df.Open[-60:],
        high=df.High[-60:],
        low=df.Low[-60:],
        close=df.Close[-60:],
        name='candlestick', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df.SMA20[-60:],
        name='SMA20',
        mode='lines',
        line=dict(color='orange', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df.SMA12[-60:],
        name='SMA12',
        mode='lines',
        line=dict(color='red', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df.EMA8[-60:],
        name='EMA8',
        mode='lines',
        line=dict(color='blue', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['BBL_20_2.0'][-60:],
        name='BBL',
        mode='lines',
        line=dict(color='black', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['BBU_20_2.0'][-60:],
        name='BBU',
        mode='lines',
        line=dict(color='black', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df1.index[-20:],
        y=df1['BBL_20_2.0'][-10:],
        name='BBL',
        mode='lines',
        line=dict(color='orange', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df1.index[-20:],
        y=df1['BBU_20_2.0'][-10:],
        name='BBU',
        mode='lines',
        line=dict(color='orange', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['PSARl_0.02_0.2'][-60:],
        name='PSARL',
        mode='markers', marker=dict(
            color="black", opacity=1,
            size=6), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['PSARs_0.02_0.2'][-60:],
        name='PSARS',
        mode='markers', marker=dict(
            color="black", opacity=1,
            size=6), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df1.index[-20:],
        y=df1['PSARl_0.02_0.2'][-16:],
        name='PSARL',
        mode='markers', marker=dict(
            color="green", opacity=1,
            size=6), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df1.index[-20:],
        y=df1['PSARs_0.02_0.2'][-16:],
        name='PSARS',
        mode='markers', marker=dict(
            color="red", opacity=1,
            size=6), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['VWAP_D'][-60:],
        name='VWAP',
        mode='lines',
        line=dict(color='purple', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['SUPERTl_7_3.0'][-60:],
        name='SUPERTl',
        mode='lines',
        line=dict(color='green', width=2), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['SUPERTs_7_3.0'][-60:],
        name='SUPERTs',
        mode='lines',
        line=dict(color='red', width=2), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['SUPERTl_14_5.0'][-60:],
        name='SUPERTl',
        mode='lines',
        line=dict(color='green', width=2), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['SUPERTs_14_5.0'][-60:],
        name='SUPERTs',
        mode='lines',
        line=dict(color='red', width=2), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['RSI'][-60:],
        name='RSI',
        mode='lines',
        line=dict(color='black', width=3), yaxis="y2"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['STOCHk_14_3_3'][-60:],
        name='STOCHk_14_3_3',
        mode='lines',
        line=dict(color='blue', width=3), yaxis="y2"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['STOCHd_14_3_3'][-60:],
        name='STOCHd_14_3_3',
        mode='lines',
        line=dict(color='red', width=3), yaxis="y2"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['MACD_12_26_9'][-60:],
        name='mACD',
        mode='lines',
        line=dict(color='blue', width=3), yaxis="y1"))

    data.add_trace(go.Bar(
        x=df.index[-60:],
        y=df['MACDh_12_26_9'][-60:],
        name='MACDh', marker={'color': 'red'},
        yaxis="y1"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['MACDs_12_26_9'][-60:],
        name='MACDs',
        mode='lines',
        line=dict(color='red', width=3), yaxis="y1"))

    data.add_shape(type='line', x0=df.index[-60], y0=df['Close'][-1],
                   x1=df.index[-1], y1=df['Close'][-1], line=dict(color='green', width=0.5, dash='dot'),
                   xref="x",
                   yref='y3')

    data.add_shape(type="rect", x0=df.index[-60], y0=70, x1=df.index[-1], y1=100, fillcolor="red",
                   opacity=0.2,
                   xref="x", yref='y2')
    data.add_shape(type="rect", x0=df.index[-60], y0=30, x1=df.index[-1], y1=70, fillcolor="blue",
                   opacity=0.2,
                   xref="x", yref='y2')
    data.add_shape(type="rect", x0=df.index[-60], y0=0, x1=df.index[-1], y1=30, fillcolor="green",
                   opacity=0.2,
                   xref="x", yref='y2')
    data.add_shape(type='line', x0=df.index[-60], y0=50,
                   x1=df.index[-1], y1=50, line=dict(color='black', width=0.5, dash='dot'), xref="x",
                   yref='y2')

    data.add_annotation(
        x=df.index[-1],
        y=df['Close'][-1],
        xref="x",
        yref="y3",
        text=df['Last_Close'][-1],
        showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=11,
            color="#ffffff"
        ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        ax=30,
        ay=0,
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="green",
        opacity=0.8, )

    data.update_layout(
        autosize=True,
        # width=1500,
        paper_bgcolor='#F5F5F5',
        plot_bgcolor='white',
        height=670,
        margin=dict(t=0, l=0, r=0, b=0),
        xaxis=dict(range=[df.index[-60], df.index[-1] + timedelta(minutes=20)], rangeslider_visible=False,
                   rangebreaks=[
                       dict(bounds=["sat", "mon"]),
                       dict(bounds=[16, 9.5], pattern="hour"),
                       # dict(values=["2021-11-25", ])
                   ]),
        yaxis1=dict(domain=[0, 0.2], side='right', linecolor='grey', linewidth=0.01, gridwidth=0.001,
                    gridcolor='grey', ),
        yaxis2=dict(domain=[0.2, 0.4], side='right', linecolor='grey', linewidth=0.01, ),
        yaxis3=dict(domain=[0.4, 1], side='right', showgrid=True,
                    gridwidth=0.001, gridcolor='grey', linecolor='grey', linewidth=0.01), showlegend=False,


    )
    chart1.plotly_chart(data, use_container_width=True)


st.set_page_config(layout="wide")

hide_menu_style = """
        <style>
        footer {visibility: hidden;}
        </style>
        """

st.markdown(hide_menu_style, unsafe_allow_html=True)

# Configuration Key
firebaseConfig = {
  'apiKey': "AIzaSyAqL4M1zvYOUy1Vt19SAclJ1IVhmB5BO0w",
  'authDomain': "zulfianto-6c780.firebaseapp.com",
  'projectId': "zulfianto-6c780",
  'databaseURL': 'https://zulfianto-6c780-default-rtdb.europe-west1.firebasedatabase.app/',
  'storageBucket': "zulfianto-6c780.appspot.com",
  'messagingSenderId': "435829402152",
  'appId': "1:435829402152:web:4de405dcfc60f21c18231d",
  'measurementId': "G-WV13RFM13Q"
}

# Firebase Authentification
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Database
db = firebase.database()
storage = firebase.storage()

title = st.sidebar.title('ZULFIANTO Stock App')
username = st.sidebar.text_input('User Name')
password = st.sidebar.text_input('Password', type='password')
login = st.sidebar.button('Sign In')

if login:
    user = auth.sign_in_with_email_and_password(username, password)
    stock = st.sidebar.text_input('Search for a Symbol...', 'NFLX')
    c1, c2 = st.columns(2)
    chart1 = c1.empty()
    chart2 = c2.empty()
    while True:
        candlestick(input_value=stock)
        candlestick1(input_value=stock)









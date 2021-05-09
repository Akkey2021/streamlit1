import yfinance as yf
import pandas as pd
import altair as alt
import streamlit as st 

st.title('あっきーの米国株')

st.sidebar.write("""
# あっきー厳選米国株
こちらは株価可視化ツールです。以下のオプションから表示日数を選んでください
""")
st.sidebar.write("""
## 表示日数選択
""")
days= st.sidebar.slider("日数",1,200,50)
#min:1, max:200, default:50

st.write(f"""
過去 **{days}日間** のあっきー保有銘柄の株価
""")

@st.cache
def get_data(days, TS):
    df =pd.DataFrame()
    for comp in TS.keys():
        tkr = yf.Ticker(TS[comp])
        hist = tkr.history(period=f'{days}d')
        hist.index = hist.index.strftime('%d %B %Y')
        hist=hist[['Close']]
        hist.columns=[comp]
        hist=hist.T
        hist.index.name='TKR'
        df = pd.concat([df,hist])
    return df



try:
    st.sidebar.write("""
    ## 株価の範囲を指定してください(USD)    
    """)
    ymin, ymax =st.sidebar.slider('範囲',0,3500,(0,500))
    #デフォルトの最小を0, 最大を3500に設定

    TS={
        'APPLE':'AAPL',
        'VTI (ETF)':'VTI',
        'UNITY SOFTWARE':'U',
        'C3 AI':'AI',
        'ZOOM':'ZM',
        'ZOOMINFO':'ZI',
        'ROYALITY PHARMA':'RPRX',
        'PINTEREST':'PINS',
        'DELTA AIR LINES':'DAL',    
    }

    df=get_data(days, TS)

    companies= st.multiselect(
        '会社名を選択してください',
        list(df.index),
        ['VTI (ETF)','ZOOM','APPLE']
    )

    if not companies:
        st.error('少なくとも一社は選んでください')
    else:
        data=df.loc[companies]
        st.write("### 株価(USD)",data.sort_index())
        data= data.T.reset_index()
        data=pd.melt(data,id_vars=['Date'])
        data= data.rename(columns={'value':'Stock prices(USD)'})
        chart=(
            alt.Chart(data)
            .mark_line(opacity=0.8, clip =True)
            .encode(
                x="Date:T",
                y=alt.Y("Stock prices(USD):Q", stack=None, scale=alt.Scale(domain=[ymin,ymax])),
                color='TKR:N'
            )
        )
        st.altair_chart(chart, use_container_width=True)
except:
    st.error("何かエラーが起きたようです！")

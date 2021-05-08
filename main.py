import streamlit as st
import numpy as np 
import pandas as pd 
from PIL import Image
import time


st.title('Akkey')
st.write('DataFrame')
# df=pd.DataFrame({
#     '1':[1,2,3,4],
#     '2':[10,20,30,40]
# })
# st.write(df)
# st.dataframe(df, width=100, height=400) #Datadrameのサイズ指定
# st.dataframe(df.style.highlight_max(axis=0)) #各列において、最大の数字をハイライト
# st.dataframe(df.style.highlight_min(axis=0)) 
# st.table(df)

# """
# # 章
# ## 節
# ### 項
# """
#マークダウン記法、見出しの書き方

# df1=pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a','b','c']
# )
# st.dataframe(df1.style.highlight_max(axis=0), width=500, height=4000)

# st.line_chart(df1)
# st.area_chart(df1)
# st.bar_chart(df1)

#いろいろなグラフの作り方

# df2=pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69, 139.70],
#     columns=['lat','lon']
# )

# st.dataframe(df2)
# st.map(df2)

# if st.checkbox('show'):
#     img=Image.open('akkey.JPG')
#     st.image(img, caption='Akkey',use_column_width=True)
# #use_column_width=True: デバイスの横幅に合わせて表示させる



#以下インタラクティブなウイジェット↓

# a = st.selectbox('あなたが好きな数字を教えてください',
#     list(range(1,11))
#     )

# 'あなたが好きな数字は',a,'です。'

# text=st.text_input('あなたの趣味を教えてください')
# 'your hobby is',text

# condition = st.slider('label-your condition',0,1000,100) #最小値、最大値、初期値
# 'your condition',condition

#以下レイアウト設定：sideber, 2column, expander

#sidebar
# a1 = st.sidebar.selectbox('あなたが好きな数字を教えてください',
#     list(range(1,11))
#     )
# text1=st.sidebar.text_input('あなたの趣味を教えてください')
# condition1 = st.sidebar.slider('label-your condition',0,1000,100) #最小値、最大値、初期値

# 'あなたが好きな数字は',a1,'です。'
# 'your hobby is',text1
# 'your condition',condition1

#2column

# left_column, right_column = st.beta_columns(2)

# bottun = left_column.button('this is right column ->')
# if bottun:
#     right_column.write('this is right column')

# #expander, FAQによくあるやつ

# exp = st.beta_expander('ask')
# exp.write('the answer is////')

#progress bar
st.write('Progress bar')
'Start!'
latest_iteration=st.empty()
bar=st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}') #st.empty()の中身を増やしていく、f()はstr()と同じ
    bar.progress(i) #barを増やしていく
    time.sleep(0.04) #interbal time

'Show!!'

img=Image.open('akkey.JPG')
st.image(img, caption='Akkey',use_column_width=True)

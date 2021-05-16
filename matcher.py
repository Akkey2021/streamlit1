import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

url='https://matcher.jp/obogs/886cf2511fbb'
res=requests.get(url)

soup=BeautifulSoup(res.text,'html.parser')
review_num=soup.find_all('div',attrs={'class':'review-summary-numbers'})
review_ave=soup.find_all('div',attrs={'class':'review-summary-rating'})

num = review_num[0].text
result=re.sub(r"\D", "", num)

result1=float(review_ave[0].text)

st.title('matcher')
st.write(f'''
■ レビュー数は**{result}件**です
''')

st.write(f'''
■ 平均レビュースコア（最大5.0）は**{result1}**です
''')

st.write('【最新のレビュー (6件)】')

text=soup.find_all('div',attrs={'class':'review-body'})
    
for i in range(6):    
    a=text[i].text.replace('\n','').replace('白井','あっきー')
    st.write(i+1)
    st.write(a)

#スクレイピングの練習



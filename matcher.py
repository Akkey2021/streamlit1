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

#スクレイピングの練習



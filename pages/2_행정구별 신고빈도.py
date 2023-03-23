import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
from  matplotlib.ticker import FuncFormatter
import numpy as np
import time
import pickle

st.set_page_config(
    page_title = '구급출동 데이터 분석',
    page_icon = ':ambulance:')

# 행정구별 신고빈도 파일 불러오기
df = pd.read_csv('data/gu_total_count.csv', encoding='cp949')
df = df.set_index('시군구명')

# 한글 폰트 지정
# font_path = 'C:/Windows/Fonts/Arial.ttf'
# font_name = fm.FontProperties(fname=font_path).get_name()
# plt.rc('font', family=font_name)

# 행정구별 신고빈도 df, 바그래프
st.subheader(':white_check_mark:2021년도 행정구별 구급신고 빈도(전체)')
agree = st.checkbox('신고빈도 수 내림차순 정렬')
if agree:
    df_sort = df.sort_values(by='신고건수', ascending=False)
    df_sort
    data = df_sort
else:
    df
    data = df

sns.barplot(x=data.index, y='신고건수', data=data, color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.xlabel('시군구명')
plt.ylabel('신고건수')
plt.grid('y')
st.pyplot(plt)

st.markdown('---')


# 행정구별 신고 빈도 멑티선택 df, 바그래프
st.subheader(':white_check_mark:2021년도 행정구별 구급신고 빈도(선택)')
option = st.multiselect('행정구를 선택하세요', df.index, default=['강남구','강서구','송파구','영등포구','관악구'])
df_1 = df.loc[option]
df_1

sns.barplot(x=df_1.index, y='신고건수', data=df_1, color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.xlabel('시군구명')
plt.ylabel('신고건수')
plt.grid('y')
st.pyplot(plt)

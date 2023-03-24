# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import platform
import matplotlib.font_manager as fm
import seaborn as sns

# 한글 폰트 지정
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':  # 맥OS
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':  # 윈도우
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system...  sorry~~~')


st.set_page_config(
    page_title = '구급출동 데이터 분석',
    page_icon = ':ambulance:',
    layout='wide')



# 행정구별 신고빈도 파일 불러오기
df = pd.read_csv('./data/gu_total_count.csv', encoding='cp949')
df = df.set_index('시군구명')

# 행정구별 신고빈도 df, 바그래프
st.subheader(':white_check_mark:2021년도 행정구별 구급신고 빈도(전체)')
agree = st.checkbox('신고빈도 수 내림차순 정렬')
col1, col2 = st.columns([0.2,0.8])
with col1 :
    if agree:
        df_sort = df.sort_values(by='신고건수', ascending=False)
        df_sort
        data = df_sort
    else:
        df
        data = df

with col2 :
    plt.figure(figsize=(15,10))
    sns.barplot(x=data.index, y='신고건수', data=data, color='skyblue')
    plt.xlabel('시군구명', fontsize=15)
    plt.ylabel('신고건수', fontsize=15)
    plt.xticks(rotation=45, ha='right', fontsize=18)
    plt.yticks(fontsize=20)
    plt.grid('y')
    st.pyplot(plt)

st.markdown('---')


# 행정구별 신고 빈도 멑티선택 df, 바그래프
st.subheader(':white_check_mark:2021년도 행정구별 구급신고 빈도(선택)')
option = st.multiselect('행정구를 선택하세요', df.index, default=['강남구','강서구','송파구','영등포구','관악구'])
col3, col4 = st.columns([0.2,0.8])
with col3:
    df_1 = df.loc[option]
    df_1

with col4:
    plt.figure(figsize=(15,10))
    sns.barplot(x=df_1.index, y='신고건수', data=df_1, color='skyblue')
    plt.xlabel('시군구명', fontsize=15)
    plt.ylabel('신고건수', fontsize=15)
    plt.xticks(rotation=45, ha='right', fontsize=18)
    plt.yticks(fontsize=20)
    plt.grid('y')
    st.pyplot(plt)
# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

st.set_page_config(
    page_title = '구급출동 데이터 분석',
    page_icon = ':ambulance:',
    layout='wide')

# 파일 불러오기
df = pd.read_csv('data/dong_sex_count.csv', encoding='cp949')
df = df.set_index('읍면동명', drop=True, encoding='cp949')

# 한글 폰트 지정
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

# 서울 전체 신고자 유형
df_sex = pd.read_csv('data\신고자성별.csv')
df_age = pd.read_csv('data\환자연령대.csv', encoding='euc-kr')
df_season = pd.read_csv('data\계절별 신고빈도.csv', encoding='euc-kr')
df_disease = pd.read_csv('data\서울질병유형.csv')
df_age['환자비율'] = df_age['환자수']/df_age['환자수'].sum()

# 서울 전체 신고자유형 파이그래프
st.subheader(':white_check_mark:2021년도 서울시 전체 신고유형')
st.markdown('---')

colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

fig, axs = plt.subplots(2,2)

axs[0,0].set_title('<신고자 성별 비율>')
axs[0,0].pie(df_sex['0'], labels=df_sex.환자성별구분명, startangle=90,
            radius=1, autopct='%.1f%%', colors=colors, wedgeprops=wedgeprops)

axs[0,1].set_title('<신고자 연령 비율>')
axs[0,1].bar(df_age['환자연령대'], df_age['환자비율'], color='skyblue')
axs[0,1].set_xticklabels(df_age['환자연령대'], rotation=40)
for i in range(len(df_age)) :
    axs[0,1].text(i-0.2, df_age.loc[i,'환자비율'], round(df_age.loc[i,'환자비율']*100,1))


axs[1,0].set_title('<환자 발생 유형 비율>')
axs[1,0].pie(df_disease['0'], labels=df_disease.환자발생유형구분명, startangle=90,
            radius=1, autopct='%.1f%%', colors=colors,wedgeprops=wedgeprops)

axs[1,1].set_title('<신고 계절 비율>')
axs[1,1].pie(df_season['계절 합계'], labels=df_season.계절구분명, startangle=90,
            radius=1, autopct='%.1f%%', colors=colors, wedgeprops=wedgeprops)

plt.rc('font', size=8) # controls default text sizes
plt.rc('axes', titlesize=8) # fontsize of the axes title
plt.rc('axes', labelsize=8) # fontsize of the x and y labels
plt.rc('xtick', labelsize=8) # fontsize of the tick labels
plt.rc('ytick', labelsize=8) # fontsize of the tick labels
plt.rc('legend', fontsize=8) # legend fontsize
plt.rc('figure', titlesize=8)
plt.tight_layout()
st.pyplot(plt)
st.markdown('---')



# 행정구별 신고 빈도 멀티선택 df, 바그래프
st.subheader(':white_check_mark:2021년도 행정구별 구급신고 빈도(선택)')
option = st.multiselect('행정구를 선택하세요', df.index, default=['강남구','강서구','송파구','영등포구','관악구'])
df_1 = df.loc[option]
df_1


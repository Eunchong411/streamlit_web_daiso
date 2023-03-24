# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import platform
import seaborn as sns
import matplotlib.font_manager as fm


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

# 한글폰트지정 2 

fontprop = fm.FontProperties(fname="font/NanumGothic.ttf")


    
    
# 서울 전체 신고자 유형
df_sex = pd.read_csv('./data/df_sex.csv')
df_age = pd.read_csv('./data/df_age.csv', encoding='euc-kr')
df_season = pd.read_csv('./data/df_season.csv', encoding='euc-kr')
df_disease = pd.read_csv('./data/df_disease.csv')
df_age['환자비율'] = df_age['환자수']/df_age['환자수'].sum()

# 서울 전체 신고자유형 파이그래프
st.subheader(':white_check_mark:2021년도 서울시 전체 구급환자 유형')
st.markdown('---')

colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

fig, axs = plt.subplots(2,2)

axs[0,0].set_title('<환자 성별 비율>')
axs[0,0].pie(df_sex['0'], labels=df_sex.환자성별구분명, startangle=90,
            radius=1, autopct='%.1f%%', colors=colors, wedgeprops=wedgeprops)

axs[0,1].set_title('<환자 연령 비율>', fontproperties=fontprop)
axs[0,1].bar(df_age['환자연령대'], df_age['환자비율'], color='skyblue')
axs[0,1].set_xticklabels(df_age['환자연령대'], rotation=40, fontproperties=fontprop)
for i in range(len(df_age)) :
    axs[0,1].text(i-0.2, df_age.loc[i,'환자비율'], round(df_age.loc[i,'환자비율']*100,1))


axs[1,0].set_title('<환자 발생 유형 비율>')
axs[1,0].pie(df_disease['0'], labels=df_disease.환자발생유형구분명, startangle=90,
            radius=1, autopct='%.1f%%', colors=colors,wedgeprops=wedgeprops)

axs[1,1].set_title('<신고 계절 비율>')
axs[1,1].pie(df_season['계절 합계'], labels=df_season.계절구분명, startangle=90,
            radius=1, autopct='%.1f%%', colors=colors, wedgeprops=wedgeprops)


plt.tight_layout()
st.pyplot(plt)
st.markdown('---')

# 동별 신고자 유형
dong_sex = pd.read_csv('./data/dong_sex_count.csv')
dong_age = pd.read_csv('./data/dong_age_count.csv')
dong_season = pd.read_csv('./data/dong_season_count.csv')
dong_disease = pd.read_csv('./data/dong_disease_count.csv')
dong_sex = dong_sex.set_index(keys='읍면동명')
dong_age = dong_age.set_index(keys='읍면동명')
dong_season = dong_season.set_index(keys='읍면동명')
dong_disease = dong_disease.set_index(keys='읍면동명')



# 행정구별 신고 빈도 멀티선택 df, 바그래프
st.subheader(':white_check_mark:2021년도 행정동별 구급환자 유형(선택)')
dong = st.selectbox('행정동을 선택하세요', dong_age.index)

fig2, axs2 = plt.subplots(2,2)

axs2[0,0].set_title('<환자 성별 비율>')
axs2[0,0].pie(dong_sex[dong_sex.index==dong].iloc[0,:], labels=dong_sex.columns, startangle=90,
            radius=1, autopct='%.1f%%', colors=colors, wedgeprops=wedgeprops)

axs2[0,1].set_title('<환자 연령 비율>')
axs2[0,1].bar(dong_age.columns, dong_age[dong_age.index==dong].iloc[0,:], color='skyblue')
axs2[0,1].set_xticklabels(dong_age.columns, rotation=50)


axs2[1,0].set_title('<환자 발생 유형 비율>')
axs2[1,0].pie(dong_disease[dong_disease.index==dong].iloc[0,:], labels=dong_disease.columns, startangle=90,
            radius=1, autopct='%.1f%%', colors=colors, wedgeprops=wedgeprops)

axs2[1,1].set_title('<신고 계절 비율>')
axs2[1,1].pie(dong_season[dong_season.index==dong].iloc[0,:], labels=dong_season.columns, startangle=90,
            radius=1, autopct='%.1f%%', colors=colors, wedgeprops=wedgeprops)

plt.tight_layout()
st.pyplot(plt)

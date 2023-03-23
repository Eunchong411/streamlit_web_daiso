# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import platform
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
    layout='wide'
)
# 파일 불러오기
sec1_pv = pd.read_csv('./data/전체 단거리.csv', encoding='cp949')
sec2_pv = pd.read_csv('./data/전체 중거리.csv', encoding='cp949')
sec1_pv = sec1_pv.set_index(['읍면동명','요일'])
sec2_pv = sec2_pv.set_index(['읍면동명','요일'])

day_hour_1 = pd.read_csv('./data/day_hour_1.csv', encoding='cp949')
day_hour_2 = pd.read_csv('./data/day_hour_2.csv', encoding='cp949')
day_hour_1 = day_hour_1.set_index('Unnamed: 0')
day_hour_2 = day_hour_2.set_index('Unnamed: 0')

weeks = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
season = ['봄','여름','가을','겨울']

st.subheader(':traffic_light:선정한 5개동의 평균 운행속도(km/h)')

# 라디오 버튼
col1, col2, col3 = st.columns([0.3, 0.3, 0.3])
st.write('')
with col1:
    button1 = st.radio('지역',('수유동','미아동','봉천동','신림동','화곡동'))

with col2:
    button2 = st.radio('거리',('단거리(4km이하)','중거리(4km초과 15km이하'))

# 체크박스
with col3:
    st.write('조건')
    num = st.checkbox('차트내 값 표시')

st.markdown("---")

plt.rc('font', size=8) # controls default text sizes
plt.rc('axes', titlesize=8) # fontsize of the axes title
plt.rc('axes', labelsize=8) # fontsize of the x and y labels
plt.rc('xtick', labelsize=8) # fontsize of the tick labels
plt.rc('ytick', labelsize=8) # fontsize of the tick labels
plt.rc('legend', fontsize=8) # legend fontsize
plt.rc('figure', titlesize=8)

# 배치
col1, col2 = st.columns([0.5,0.5])
with col1 :
    if button2 == '단거리(4km이하)':
        data = day_hour_1
    else :
        data = day_hour_2
    if num :
        annot = True
    else:
        annot = False
    plt.figure(figsize=(22, 12))
    sns.heatmap(data, vmax=data.max().max(), vmin=data.min().min(), cmap='Reds', annot=annot,
                fmt='.2f')
    plt.title(f'서울시 전체 : {button2} 현장 출동 평균시속', fontsize=16)
    plt.yticks(rotation=0)
    plt.ylabel('요일', rotation=0)
    st.pyplot(plt)

with col2 :
    if num :
        annot = True
    else:
        annot = False
    plt.figure(figsize=(22, 12))
    sns.heatmap(sec1_pv.loc[f'{button1}'].agg(weeks), cmap='Reds', annot=annot, fmt='.2f', annot_kws={'size': 15}, vmin=0.34,
                    vmax=0.48)
    plt.title(f'{button1} : {button2} 현장 출동 평균시속', fontsize=16)
    plt.xlabel('시간대', fontsize=12)
    plt.ylabel('요일', fontsize=12, rotation=0)
    st.pyplot(plt)

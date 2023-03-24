# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import platform
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
    
st.set_page_config(
    page_title = '구급출동 데이터 분석',
    page_icon = ':ambulance:',
    layout='wide'
)
# 파일 불러오기
sec1_pv = pd.read_csv('./data/total_short.csv', encoding='euc-kr')
sec2_pv = pd.read_csv('./data/total_middle.csv', encoding='euc-kr')
sec1_pv = sec1_pv.set_index(['읍면동명','요일'])
sec2_pv = sec2_pv.set_index(['읍면동명','요일'])

day_hour_1 = pd.read_csv('./data/day_hour_1.csv')
day_hour_2 = pd.read_csv('./data/day_hour_2.csv')
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
    button2 = st.radio('거리',('단거리(4km이하)','중거리(4km초과 15km이하)'))

# 체크박스
with col3:
    st.write('조건')
    num = st.checkbox('차트내 값 표시')

st.markdown("---")



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
    sns.heatmap(data*60, vmax=data.max().max()*60, vmin=data.min().min()*60, cmap='Reds', annot=annot, annot_kws={'size': 25},
                fmt='.0f')
    plt.title(f'서울시 전체 : {button2} 현장 출동 평균시속', fontsize=40, fontproperties=fontprop)
    plt.xlabel('시간대', fontsize=30, fontproperties=fontprop)
    plt.xticks(fontsize=30, fontproperties=fontprop)
    plt.yticks(fontsize=30, rotation=0, fontproperties=fontprop)
    plt.ylabel('', fontproperties=fontprop)
    st.pyplot(plt)

with col2 :
    if button2 == '단거리(4km이하)':
        data2 = sec1_pv
    else :
        data2 = sec2_pv
    if num :
        annot = True
    else:
        annot = False
    plt.figure(figsize=(22, 12))
    sns.heatmap(data2.loc[f'{button1}'].agg(weeks)*60, cmap='Reds', annot=annot, fmt='.0f', annot_kws={'size': 25}, vmin=data.min().min()*60,
                    vmax=data.max().max()*60)
    plt.title(f'{button1} : {button2} 현장 출동 평균시속', fontsize=40, fontproperties=fontprop)
    plt.xlabel('시간대', fontsize=30, fontproperties=fontprop)
    plt.xticks(fontsize=30, fontproperties=fontprop)
    plt.yticks(fontsize=30, rotation=0, fontproperties=fontprop)
    st.pyplot(plt)

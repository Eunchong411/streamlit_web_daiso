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

time_df_new = pd.read_csv('./data/time_df_new.csv')
time_df_new = time_df_new.drop(columns='Unnamed: 0')

weeks = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
season = ['봄','여름','가을','겨울']

# 라디오 버튼
st.subheader(':traffic_light:신고빈도 상위 20개동의 평균 운행속도(km/h)')
st.write('')
button = st.radio('기준',('시간대별','요일별','월별','계절별'))
# 체크박스
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

if num :
    annot = True
else:
    annot = False
if button == '시간대별' :
    plt.title('신고빈도 상위 20개동의 시간대별 평균 운행속도')
    dong_hour = time_df_new.pivot_table(index='읍면동명', columns='출동시', values='거리(km)/시간(분)', aggfunc='mean')*60
    plt.figure(figsize=(20, 10))
    sns.heatmap(dong_hour, vmax=dong_hour.max().max(), vmin=dong_hour.min().min(), cmap='Reds', annot=annot, fmt='.0f')
    st.pyplot(plt)
elif button == '요일별' :
    dong_day = time_df_new.pivot_table(index='요일', columns='읍면동명', values='거리(km)/시간(분)', aggfunc='mean').agg(weeks).T*60
    plt.title('신고빈도 상위 20개동의 요일별 평균 운행속도')
    plt.figure(figsize=(20, 10))
    sns.heatmap(dong_day, vmax=dong_day.max().max(), vmin=dong_day.min().min(), cmap='Reds', annot=annot, fmt='.0f')
    st.pyplot(plt)
elif button == '월별' :
    dong_month = time_df_new.pivot_table(index=['읍면동명'], columns='출동월', values='거리(km)/시간(분)', aggfunc='mean')*60
    plt.title('신고빈도 상위 20개동의 월별 평균 운행속도')
    plt.figure(figsize=(20, 10))
    sns.heatmap(dong_month, vmax=dong_month.max().max(), vmin=dong_month.min().min(), cmap='Reds', annot=annot,fmt='.0f')
    st.pyplot(plt)
else :
    dong_season = time_df_new.pivot_table(index=['계절구분명'], columns='읍면동명', values='거리(km)/시간(분)', aggfunc='mean').agg(season).T*60
    plt.title('신고빈도 상위 20개동의 계절별 평균 운행속도')
    plt.figure(figsize=(20, 10))
    sns.heatmap(dong_season, vmax=dong_season.max().max(), vmin=dong_season.min().min(), cmap='Reds', annot=annot,
                fmt='.0f')
    st.pyplot(plt)

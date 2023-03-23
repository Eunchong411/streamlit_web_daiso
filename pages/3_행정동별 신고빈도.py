import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium
import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
from folium.plugins import MarkerCluster

# 페이지 설정
st.set_page_config(
    page_title = '구급출동 데이터 분석',
    page_icon = ':ambulance:')

# 행정동별 신고빈도 파일 불러오기
df = pd.read_csv('data/dong_total_count.csv')
df = df.set_index(keys='읍면동명', drop=True)

st.subheader(':white_check_mark:2021년도 행정동별 구급신고 빈도(지도시각화)')

# 가나다순 -> 내림차순 정렬 체크박스
agree = st.checkbox('신고빈도 수 내림차순 정렬')
if agree:
    df_sort = df.sort_values(by='신고건수', ascending=False)
    df_sort

else:
    df

# folium 지도 시각화
with open ('data/seoul.json', encoding='utf-8') as f:
    geo_seoul = json.loads(f.read())

m = folium.Map(location=[37.566535, 126.9779691999996],zoom_start=11)
folium.Choropleth(geo_data = geo_seoul,
                 data = df['신고건수'],
                  columns = [df.index, df['신고건수']],
                  fill_color = 'YlGn', fill_opacity=0.7,
                  line_opacity=0.3,
                  key_on='feature.properties.EMD_NM',).add_to(m)

st_folium(m,width=750)
st.markdown('---')


# 그래프 한글 폰트 지정
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

# 신고 빈도 상위 20개동 df, 바그래프
st.subheader(':white_check_mark:2021년도 구급신고 빈도 상위 20개동')
dong_20 = df.sort_values(by='신고건수', ascending=False).iloc[:20,:]
dong_20
sns.barplot(x=dong_20.index, y='신고건수', data=dong_20, color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.xlabel('읍면동명')
plt.ylabel('신고건수')
plt.grid('y')
st.pyplot(plt)

st.markdown('---')

# 행정동별 신고 빈도 멑티선택 df, 바그래프
st.subheader(':white_check_mark:2021년도 행정동별 구급신고 빈도(선택)')
option = st.multiselect('행정동을 선택하세요', df.index, default=['신림동','봉천동','화곡동','상계동','신정동'])
df_1 = df.loc[option]
df_1

sns.barplot(x=df_1.index, y='신고건수', data=df_1, color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.xlabel('읍면동명')
plt.ylabel('신고건수')
plt.grid('y')
st.pyplot(plt)
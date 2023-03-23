import streamlit as st
import numpy as np
import pandas as pd

# 페이지 기본 설정

st.set_page_config(
    page_title = '구급출동 데이터 분석',
    page_icon = ':ambulance:',
    layout= 'wide',
    menu_items= {
        # 'Get Help' : 'https://www.naver.com',
        'About':'다이소조 주간프로젝트 작업물입니다.'
    },
    initial_sidebar_state='expanded'
)

# 터미널 streamlit run MyApp.py

st.subheader(':ambulance:구급차량 출동시간 단축을 위한 서울시 구급 신고다발지역 현황분석')
st.subheader(': 2021년 구급출동현황 데이터를 중심으로')

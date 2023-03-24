# -*- coding: utf-8 -*-
import streamlit as st
import numpy as np
import pandas as pd

# 페이지 기본 설정

st.set_page_config(
    page_title = '구급출동 데이터 분석',
    page_icon = ':ambulance:',
    layout= 'wide',
    menu_items= {
        'Get Help' : 'https://github.com/Yerial1125/weeklyproject',
        'About':'다이소조 주간프로젝트 작업물입니다.'
    },
    initial_sidebar_state='expanded'
)


st.subheader(':ambulance:구급차량 출동시간 단축을 위한 서울시 구급 신고다발지역 현황분석')
st.markdown('**다이소조**: 권예진, 김영민, 김희진, 여은총')
st.markdown('---')

st.markdown(':white_check_mark:**선정 배경**')
st.markdown('우리 주변에는 지금 이 순간에도 수 많은 사건, 사고가 발생하고 위급한 경우 구급 차량이 출동을 하여 생명을 구함으로써'
         ' 우리 사회 구성원의 안전을 책임지고 있다. 하지만 이런 사건 사고는 언제, 어디서, 어떻게 발생할지 예상하는 것은 결코'
         ' 쉬운 일이 아니다. 구급 차량 도달, 업무처리시간의 경우, 국민의 생명과 직결되는 중요한 문제이다.')
st.markdown('**따라서 우리 다이소 조는 소방 구급 출동 데이터와 서울시 교통량 조사 데이터를 이용하여 신고빈도가 많은 지역을 시간대별로 분류하여 출동 시간을 단축시킨다.** ')
st.write('')
st.write('')

st.markdown(':white_check_mark:**목적**')
st.markdown('구급차량 출동시간을 단축할 수 있는 방안을 찾기 위해 다양한 관점에서 데이터 분석을 진행할 계획이다. 이에, 우리는 1차적으로 성별,'
            ' 연령대, 질병유형 등 환자의 유형별로 분석을 진행하였다. 이후, 행정지역별 신고빈도 분석과 교통 혼잡도 분석을 통해 출동 시간과 '
            '교통량에 영향을 미치는 요일, 시간 계절적 특성을 파악하고자 한다. 또한, 결과를 바탕으로 출동시간을 최대한 단축시킬 수 있는 방안을 찾을 것이다.')
st.write('')
st.write('')

st.markdown(':white_check_mark:**대상**')
st.markdown('다음과 같이 해당 정보가 필요한 모든 기업과 국가기관을 대상으로 진행된다.')
st.markdown('**- 한국도로교통공사, 서울특별시청, 소방서, 병원**')
st.write('')
st.write('')

st.markdown(':white_check_mark:**기대 효과**')
st.markdown('1. 분석한 출동 현황 통계 자료를 기반으로 **구급 차량의 도착시간 및 업무 처리시간을 단축**시켜 구급력을 강화시킬 수 있다.')
st.markdown('2. 다양한 조건별로 분석한 결과를 통해 평소 **구급 인력과 장비를 배정할 장소와 시간대**를 수월하게 지정할 수 있다.')
st.markdown('3. 사고 발생이 잦은 곳은 **신호체계 및 응급차량 도로**를 미리 준비함에 따라 출동시간을 단축할 수 있다.')
st.write('')

st.markdown(':white_check_mark:**데이터 소개**')
st.markdown('**1. 2021 구급출동현황** (https://www.bigdata-119.kr/goods/goodsInfo?goods_id=202302000060)')
st.markdown('환자발생유무, 현장도착시각,출동시각, 도착시각, 현장거리 등 데이터 크기: 551597(행)개수')
st.write('')

st.markdown('**2. 2021 서울시 교통량 조사자료** (https://topis.seoul.go.kr/refRoom/openRefRoom_2.do)')
st.markdown('서울시의 도로별, 방향별, 시간대별 교통량 등 데이터 크기: 8371(행)개수 * 12개월')
st.write('')

st.markdown('**3. 2021 서울시 차량통행속도** (https://topis.seoul.go.kr/refRoom/openRefRoom_2.do)')
st.markdown('서울시의 일자, 요일, 시간대별 차량통행속도 등 데이터 크기: 150000(행)개수 * 12개월')
st.write('')
# streamlit_web_daiso
스트림릿 웹 배포_다이소조


# weeklyproject
### 데이터 분석 및 시각화 주간 프로젝트 : 다이소조
## 구급차량 출동시간 단축을 위한 서울시 구급 신고다발지역 현황분석

### 사용프로그램
[streamlit](https://streamlit.io/)

```
pip install streamlit
```

### 파이참 인터프리터 추가 설치

```
streamlit-folium
```

### 대시보드 구성 및 변수

#### 1. 메인페이지

#### 2. 구급환자유형 빈도
- df_sex : 성별 신고빈도(서울 전체)
- df_age : 나이대별 신고빈도(서울 전체)
- df_season : 계절별 신고빈도(서울 전체)
- df_disease : 환자발생유형별 신고빈도(서울 전체)

#### 3. 행정구별 신고빈도
- gu_total_count : 행정구별 신고빈도

#### 4. 행정동별 신고빈도
- dong_total_count : 행정동별 신고빈도
- geo_seoul : 서울 행정구 경계
- dong_marker : 서울 행정동 위경도

#### 5. 상위 20개동 평균 운행속도
- time_df_new : 상위 20개동 운행속도

#### 6. 선정된 5개동 평균 운행속도
- day_hour_1 : 서울시 평균 운행속도(단거리:4km이하)
- day_hour_2 : 서울시 평균 운행속도(중거리:4km초과 15km이하)
- sec1_pv : 행정구별 평균 운행속도(단거리:4km이하)
- sec2_pv : 행정구별 평균 운행속도(중거리:4km초과 15km이하)

### 데이터 출처
1. **2021 구급출동현황** (https://www.bigdata-119.kr/goods/goodsInfo?goods_id=202302000060)
 - 환자발생유무, 현장도착시각,출동시각, 도착시각, 현장거리 등 데이터 크기: 551597(행)개수

2. **2021 서울시 차량통행속도** (https://topis.seoul.go.kr/refRoom/openRefRoom_2.do)
  - 서울시의 일자, 요일, 시간대별 차량통행속도 등 데이터 크기: 150000(행)개수 * 12개월

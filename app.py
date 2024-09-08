import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# Pretendard-Bold.otf 폰트 등록
font_path = 'data/Pretendard-Bold.otf'
font_prop = FontProperties(fname=font_path)

# 페이지 제목
st.title("데이터 대시보드 템플릿")

# 사이드바에 데이터 업로드 기능
st.sidebar.header("데이터 업로드")
uploaded_file = st.sidebar.file_uploader("CSV 파일을 업로드 하세요", type=["csv"])
uploaded_file = 'data/경찰청_범죄 발생 지역별 통계_20221231.csv'

# 데이터 업로드 후 처리
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.header("데이터 미리보기")
    st.write(df.head())

    st.header("데이터 요약 통계")
    st.write(df.describe())

    # 컬럼 선택
    st.sidebar.header("시각화 설정")
    selected_column = st.sidebar.selectbox("컬럼 선택", df.columns)
    
    # 히스토그램
    st.header(f"'{selected_column}' 컬럼의 히스토그램")
    fig, ax = plt.subplots()
    ax.hist(df[selected_column], bins=20)
    ax.set_title(f"'{selected_column}' 히스토그램", fontproperties=font_prop)
    ax.set_xlabel(selected_column, fontproperties=font_prop)
    ax.set_ylabel('빈도', fontproperties=font_prop)
    st.pyplot(fig)

    # Scatter plot
    st.sidebar.header("산점도 설정")
    x_axis = st.sidebar.selectbox("X축 선택", df.columns)
    y_axis = st.sidebar.selectbox("Y축 선택", df.columns)

    st.header(f"산점도: {x_axis} vs {y_axis}")
    fig, ax = plt.subplots()
    ax.scatter(df[x_axis], df[y_axis])
    ax.set_xlabel(x_axis, fontproperties=font_prop)
    ax.set_ylabel(y_axis, fontproperties=font_prop)
    ax.set_title(f"{x_axis} vs {y_axis}", fontproperties=font_prop)
    st.pyplot(fig)
    
else:
    st.write("왼쪽 사이드바에서 CSV 파일을 업로드 해주세요.")
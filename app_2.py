import math
import folium
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정 및 호선별 색상 사전 정의
# -----------------------------------------------------------------------------
st.set_page_config(page_title="부산 지하철 지도 분석", layout="wide")
st.title("🚇 부산 지하철 역별 이용객 수 지도 분석")

# [색상] 호선별 색상 매핑 (1호선: 주황, 2호선: 초록, 3호선: 갈색, 4호선: 파랑)
LINE_COLORS = {
    "1호선": "#FF7F0E",  # 주황
    "2호선": "#2CA02C",  # 초록
    "3호선": "#8C564B",  # 갈색
    "4호선": "#1F77B4",  # 파랑
}

# -----------------------------------------------------------------------------
# 2. CSV 파일 업로드
# -----------------------------------------------------------------------------
uploaded_file = st.file_uploader(
    "busan_subway.csv 파일을 업로드하세요", type=["csv"]
)

if uploaded_file is not None:
    # CSV 파일 읽기
    df = pd.read_csv(uploaded_file)

    # -------------------------------------------------------------------------
    # 3. [호선 필터] multiselect 생성 및 데이터 필터링
    # -------------------------------------------------------------------------
    # 데이터에 존재하는 호선 목록 추출
    all_lines = list(df["호선"].unique())

    # 기본값으로 모든 호선이 선택되도록 설정
    selected_lines = st.multiselect(
        "🎛️ 표시할 호선을 선택하세요", options=all_lines, default=all_lines
    )

    # 선택한 호선에 해당하는 데이터만 필터링
    filtered_df = df[df["호선"].isin(selected_lines)]

    # -------------------------------------------------------------------------
    # 4. 전체 데이터 표 & [표] 이용객 상위 5개 역 표시
    # -------------------------------------------------------------------------
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📄 전체 지하철 데이터")
        st.dataframe(filtered_df, use_container_width=True, height=220)

    with col2:
        st.subheader("🏆 이용객 상위 5개 역")
        # 이용객수 기준으로 내림차순 정렬 후 상위 5개 추출
        top5_df = filtered_df.sort_values(by="이용객수", ascending=False).head(5)
        st.dataframe(
            top5_df[["호선", "역명", "이용객수"]],
            use_container_width=True,
            height=220,
        )

    # -------------------------------------------------------------------------
    # 5. Folium 지도 생성 및 [색상] 호선별 CircleMarker 추가
    # -------------------------------------------------------------------------
    st.subheader("🗺️ 역별 이용객 수 지도")

    # 부산 중심 좌표(서면역 근처)로 지도 초기화
    m = folium.Map(location=[35.1578, 129.0592], zoom_start=11)

    # 필터링된 데이터를 바탕으로 지도에 마커 표시
    for _, row in filtered_df.iterrows():
        # 원의 면적이 이용객수에 비례하도록 반지름(제곱근) 계산
        radius_value = math.sqrt(row["이용객수"]) * 0.05

        # 호선에 맞는 색상 가져오기 (사전에 없으면 기본 검은색)
        line_color = LINE_COLORS.get(row["호선"], "#000000")

        # CircleMarker 추가
        folium.CircleMarker(
            location=[row["위도"], row["경도"]],
            radius=radius_value,
            color=line_color,  # 테두리 색상 (호선별 색상)
            fill=True,
            fill_color=line_color,  # 내부 채우기 색상
            fill_opacity=0.6,
            tooltip=f"[{row['호선']}] {row['역명']}",  # 마우스 올렸을 때
            popup=f"{row['역명']}: {row['이용객수']:,}명",  # 클릭했을 때
        ).add_to(m)

    # Streamlit 화면에 지도 출력
    st_folium(m, width=1100, height=600)

else:
    st.info("시작하려면 busan_subway.csv 파일을 업로드해 주세요.")
# 🚇 부산 지하철 역별 이용객 수 지도 분석 앱

Streamlit과 Folium을 활용하여 부산 지하철 역별 이용객 수를 지도에 시각화하고 분석하는 웹 애플리케이션입니다.

---

## 📌 주요 기능

1. **CSV 데이터 업로드 및 조회**
   - 지하철 역별 이용객 수 데이터(`busan_subway.csv`) 업로드
   - 전체 지하철 데이터 목록 표 표출
2. **이용객 상위 역 분석**
   - 이용객 수가 가장 많은 상위 5개 역 자동 선별 및 표 표출
3. **호선별 필터링**
   - Multiselect를 통해 원하는 호선(1~4호선)만 선택하여 시각화
4. **인터랙티브 지도 시각화 (Folium)**
   - **호선별 색상 구분**: 1호선(주황), 2호선(초록), 3호선(갈색), 4호선(파랑)
   - **이용객 수 비례 원 크기**: 이용객 수의 제곱근(Sqrt) 비율을 적용하여 CircleMarker 생성
   - **툴팁 & 팝업**: 마우스를 올리면 역명 표시, 클릭 시 상세 이용객 수 표시

---

## 🛠️ 기술 스택 (Tech Stack)

- **Language:** Python
- **Web Framework:** Streamlit
- **Data Processing:** Pandas
- **Map Visualization:** Folium, Streamlit-Folium

---

## 🚀 실행 방법 (Local Run)

### 1. 저장소 클론 (Clone)
```bash
git clone [https://github.com/사용자이름/저장소이름.git](https://github.com/사용자이름/저장소이름.git)
cd 저장소이름
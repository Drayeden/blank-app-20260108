import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image, ImageDraw
import io

# --------------------------------------
# Streamlit 요소 예제 모음 (단일 페이지)
# 각 섹션에 한국어 주석(각주)으로 설명을 달아 학습에 도움을 줍니다.
# 실행: `streamlit run streamlit_app.py`
# --------------------------------------

st.set_page_config(page_title="Streamlit 요소 예제", layout="wide")

st.title("🎈 Streamlit 요소 예제 모음")
st.markdown("다양한 Streamlit 위젯과 출력 요소를 한 페이지에 모아놓은 예제입니다.")

# ---------------------- 텍스트 관련 ----------------------
st.header("텍스트 및 마크다운")
# st.title/st.header/st.subheader/st.caption 등은 문서 구조를 잡을 때 사용
st.subheader("기본 텍스트 출력")
st.write("`st.write()`는 가장 범용적입니다: 문자열, 수치, 데이터프레임 등 어떤 타입도 출력 가능")
st.write("Hello, Streamlit!")

st.markdown("**Markdown** 형식도 지원합니다. 링크, 굵은 글씨, 리스트 등을 쓸 수 있어요.")
st.code("print('Hello world')", language="python")
st.latex(r"E = mc^2")

# ---------------------- 인터랙티브 위젯 - 단일 값 ----------------------
st.header("인터랙티브 위젯 (단일 값)")
col1, col2 = st.columns(2)

with col1:
    st.subheader("버튼과 체크박스")
    # 버튼: 누르면 True를 반환하는 일회성 액션
    if st.button("클릭해보기 (Button)"):
        st.success("버튼이 눌렸습니다!")

    # 체크박스: 토글 상태를 유지
    agree = st.checkbox("동의합니다 (Checkbox)")
    st.write("동의 상태:", agree)

with col2:
    st.subheader("라디오 / 셀렉트박스")
    color = st.radio("색상 선택 (Radio)", ("빨강", "초록", "파랑"))
    st.selectbox("항목 선택 (Selectbox)", ["옵션 A", "옵션 B", "옵션 C"], index=1)
    st.write("선택한 색:", color)

# ---------------------- 멀티 선택 / 슬라이더 ----------------------
st.subheader("멀티선택, 슬라이더, 숫자 입력")
choises = st.multiselect("좋아하는 과일 (Multiselect)", ["사과", "바나나", "오렌지", "포도"], default=["사과"])
st.write("선택한 과일:", choises)

age = st.slider("나이 (Slider)", 0, 120, 30)
height = st.number_input("키 (Number input, cm)", min_value=50, max_value=250, value=170)
st.write(f"나이: {age}, 키: {height}cm")

# ---------------------- 텍스트 입력 ----------------------
st.header("텍스트 입력과 폼")
name = st.text_input("이름을 입력하세요")
bio = st.text_area("자기소개 (Text area)")
st.write("안녕하세요,", name)

with st.form("my_form"):
    st.write("폼 예시: 여러 입력을 묶어 한 번에 전송")
    ok = st.checkbox("조건 동의")
    rating = st.slider("평점", 1, 5, 3)
    submitted = st.form_submit_button("제출")
    if submitted:
        st.write("폼 제출됨:", {"ok": ok, "rating": rating})

# ---------------------- 날짜/시간/파일 ----------------------
st.header("날짜, 시간, 파일 업로드")
st.date_input("날짜 선택")
st.time_input("시간 선택")
uploaded = st.file_uploader("파일 업로드 (이미지/텍스트) - 업로드하면 아래에 미리보기")
if uploaded is not None:
    # 업로드된 바이너리 데이터를 PIL이미지로 열어 미리보기
    try:
        img = Image.open(uploaded)
        st.image(img, caption="업로드된 이미지", use_column_width=True)
    except Exception:
        uploaded.seek(0)
        st.text(uploaded.read().decode('utf-8', errors='ignore'))

# ---------------------- 미디어 & 다운로드 ----------------------
st.header("미디어: 이미지, 오디오, 비디오, 다운로드")
st.write("아래는 동적으로 생성한 이미지 예시와 다운로드 버튼입니다.")

# 간단한 이미지를 메모리에서 생성
img = Image.new("RGB", (300, 100), color=(73, 109, 137))
draw = ImageDraw.Draw(img)
draw.text((10, 40), "Streamlit Demo", fill=(255, 255, 0))
buf = io.BytesIO()
img.save(buf, format="PNG")
buf.seek(0)
st.image(buf, caption="메모리에서 생성한 이미지")
st.download_button("이미지 다운로드", data=buf, file_name="demo.png", mime="image/png")

# ---------------------- 데이터 출력 (표, 데이터프레임, JSON) ----------------------
st.header("데이터 출력")
df = pd.DataFrame({
    "이름": ["철수", "영희", "민수"],
    "나이": [25, 31, 19],
    "점수": [88, 92, 77]
})
st.dataframe(df)  # 인터랙티브한 데이터프레임
st.table(df)      # 정적 표
st.json({"예시": True, "값": [1, 2, 3]})

# ---------------------- 차트 (간단한 예) ----------------------
st.header("차트 예시")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)
st.area_chart(chart_data)
st.bar_chart(chart_data.iloc[:5])

# ---------------------- 레이아웃: 컬럼, 익스팬더, 탭 ----------------------
st.header("레이아웃 구성")
left, right = st.columns(2)
with left:
    st.subheader("왼쪽 컬럼")
    st.info("여기는 왼쪽 영역입니다.")
with right:
    st.subheader("오른쪽 컬럼")
    st.warning("여기는 오른쪽 영역입니다.")

with st.expander("더보기 (Expander)"):
    st.write("숨겨진 내용을 여기에 둡니다. 긴 설명이나 참조를 넣기 좋습니다.")

tabs = st.tabs(["탭1", "탭2", "탭3"])
tabs[0].write("탭 1의 내용")
tabs[1].write("탭 2의 내용")
tabs[2].write("탭 3의 내용")

# ---------------------- 사이드바 예시 ----------------------
st.sidebar.title("사이드바 설정")
st.sidebar.write("사이드바는 설정/네비게이션에 적합합니다")
st.sidebar.selectbox("사이드바 선택", ["A", "B", "C"]) 

# ---------------------- 상태 표시기 및 진행바 ----------------------
st.header("상태 표시기 및 진행상태")
with st.spinner("작업 진행 중..."):
    import time

    time.sleep(0.5)
st.success("스피너 완료")

progress = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1)

# ---------------------- 캐시 / 성능 (간단 설명) ----------------------
st.header("캐시 예시 (데모)")
st.write("`st.cache_data` 또는 `st.cache_resource`를 이용해 비용이 큰 작업을 캐시할 수 있습니다.")

@st.cache_data
def expensive_computation(x):
    # 실제로는 무거운 처리(예: API 호출, 긴 계산 등)를 캐시
    return x * 2

st.write("캐시된 함수 호출 예시:", expensive_computation(21))

# ---------------------- 마무리 안내 ----------------------
st.markdown("---")
st.write("이 페이지는 Streamlit의 주요 요소들을 한 곳에서 살펴볼 수 있게 구성되었습니다.")
st.write("코드 주석을 참고하며 각각의 위젯을 직접 눌러보고 파라미터를 바꿔보세요.")


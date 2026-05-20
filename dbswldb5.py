import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(
    page_title="Beauty BM Studio",
    page_icon="💄",
    layout="wide"
)

# 제목
st.title("💄 Beauty BM Studio")
st.write("색조 화장품 BM 분석 앱")

# 샘플 데이터
products = pd.DataFrame({
    "브랜드": ["Rom&nd", "3CE", "Hince", "Clio"],
    "제품": ["쥬시 틴트", "벨벳 립", "글로우 립밤", "킬커버 쿠션"],
    "가격": [13000, 17000, 18000, 32000],
    "평점": [4.7, 4.5, 4.8, 4.6],
    "판매량": [5400, 4300, 3900, 6100]
})

# 메뉴
menu = st.sidebar.selectbox(
    "메뉴 선택",
    [
        "BM 대시보드",
        "경쟁 브랜드 분석",
        "퍼스널 컬러 추천"
    ]
)

# BM 대시보드
if menu == "BM 대시보드":

    st.header("📊 BM 대시보드")

    st.dataframe(products)

    st.bar_chart(
        products.set_index("브랜드")["판매량"]
    )

# 경쟁 브랜드 분석
elif menu == "경쟁 브랜드 분석":

    st.header("📈 경쟁 브랜드 분석")

    brand = st.selectbox(
        "브랜드 선택",
        products["브랜드"]
    )

    filtered = products[
        products["브랜드"] == brand
    ]

    st.dataframe(filtered)

# 퍼스널 컬러 추천
elif menu == "퍼스널 컬러 추천":

    st.header("🎨 퍼스널 컬러 추천")

    skin = st.selectbox(
        "피부톤 선택",
        ["봄 웜", "여름 쿨", "가을 웜", "겨울 쿨"]
    )

    color_map = {
        "봄 웜": ["코랄", "피치", "살몬 핑크"],
        "여름 쿨": ["로즈", "모브", "쿨 핑크"],
        "가을 웜": ["브릭", "테라코타", "브라운 레드"],
        "겨울 쿨": ["버건디", "체리 레드", "플럼"]
    }

    st.success(
        f"{skin} 추천 컬러: {', '.join(color_map[skin])}"
    )

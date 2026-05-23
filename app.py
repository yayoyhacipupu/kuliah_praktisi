import streamlit as st

st.set_page_config(
  page_title="kuliah_praktisi",
  page_icon="🧊",
  layout="centered",
  initial_sidebar_state="expanded",
)
  
# Hirarki teks
st.title("📊 Dashboard")
st.header("Laporan Bulanan")
st.subheader("📈 Monthly Expenses")
st.caption("Made with ❤️ using Streamlit")
st.write("Hello, *World!* :sunglasses:")
color = st.color_picker("Pick A Color", "#c92580")
st.write("The current color is", color)

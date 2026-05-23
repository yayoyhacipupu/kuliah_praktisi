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
left, middle, right = st.columns(3)
if left.button("Hanna", width="stretch"):
    left.markdown("You clicked the Hanna.")
if middle.button("Aisy", icon="😃", width="stretch"):
    middle.markdown("You clicked the Aisy.")
if right.button("Divi", icon=":material/mood:", width="stretch"):
    right.markdown("You clicked the Divi.")

genre = st.radio(
    "What's your favorite dosen",
    [":rainbow[bu lina]", "***kak roma***", "pak edi"],
)

if genre == ":rainbow[bu lina]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")

your-repository/
├── pages/
│   ├── page_1.py
│   └── page_2.py
└── your_app.py
st.page_link("your_app.py", label="Home", icon="🏠")
st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")

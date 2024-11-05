import streamlit as st

st.title('算出')

ramuda_ori = st.number_imput('とうちゃくりつ')
myu_ori = st.number_imput('さーびすりつ')

ramuda = 1 / ramuda_ori
myu = 1 / myu_ori

ro = ramuda / myu

bo = 1 - ro

hidari = ro / bo
migi = 1 / myu

answer = hidari * migi

if myu > ramuda:
    st.title(answer)
else:
    st.title('はっさん')
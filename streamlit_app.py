import streamlit as st

st.title('算出')

ramuda_ori = st.number_input('とうちゃくjikann',0)
myu_ori = st.number_input('さーびすjikann',0)

if ramuda_ori != 0 and myu_ori != 0:
    ramuda = 1 / ramuda_ori
    myu = 1 / myu_ori

    ro = ramuda / myu

    bo = 1 - ro

    hidari = ro / bo
    migi = 1 / myu

    st.write('ro')
    st.subheader(ro)

    st.write('bunnnoiti')
    st.subheader(hidari)

    answer = hidari * migi

    if myu > ramuda:
        st.title(answer)
    else:
        st.title('はっさん')
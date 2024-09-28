import streamlit as st
import numpy as np

from st_paywall import add_auth

add_auth(required=True)


st.write(st.session_state.email)
st.write(st.session_state.user_subscribed)

with st.chat_message("assistant"):
    st.write("Hello human")
    st.bar_chart(np.random.randn(30, 3))

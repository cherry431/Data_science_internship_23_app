import streamlit as st
import time

st.title(":blue[అసమర్థుడు]")



btn_click = st.button("Click Me!")


progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)

if btn_click == True:
    st.subheader("You clicked me :heartbeat:")
    st.balloons()
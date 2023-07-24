import streamlit as st
import time
import datetime
import asyncio


print("rerun")


def on_click():
    print("on_click")
    # st.stop()
    # st.experimental_rerun()


btn = st.button("btn", on_click=on_click)
if btn:
    print("post click")
    # st.stop()
    # st.experimental_rerun()


def main():
    while True:
        print(datetime.datetime.now())
        st.write(datetime.datetime.now())
        time.sleep(1)


main()

"""
Watch the difference in the console output when comment in line 26 (`st.write(datetime.datetime.now())`).

When `st` is used inside the loop, streamlit will handle the control flow correctly: rerunning the script will close the event loop in the previous run.

Using asyncio also works, see controflow2.py
"""

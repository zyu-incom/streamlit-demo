import time
import datetime
import streamlit as st
from streamlit_autorefresh import st_autorefresh

print(datetime.datetime.now())

# Run the autorefresh about every 2000 milliseconds (2 seconds)
count = st_autorefresh(interval=1000, limit=None, debounce=True, key="fizzbuzzcounter")

# The function returns a counter for number of refreshes. This allows the
# ability to make special requests at different intervals based on the count

st.button("btn")

time.sleep(2)
st.write(f"Count: {count}")
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


async def main():
    # with st.empty():
        while True:
            print(datetime.datetime.now())
            st.write(datetime.datetime.now())
            await asyncio.sleep(1)


asyncio.run(main())

# if __name__ == "__main__":
#     # loop = asyncio.new_event_loop()
#     # asyncio.set_event_loop(loop)
#     try:
#         asyncio.run(main())
#     except KeyboardInterrupt:
#         pass
#     finally:
#         print("Closing loop")
#         # loop.close()


"""
Same behavior as controlflow1.py

Using the commented block of code at line 33 also behaves the same.
"""

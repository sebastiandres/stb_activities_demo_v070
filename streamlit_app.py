import streamlit as st
import streamlit_book as stb
import time
import random

def main():
    # Set wide display
    st.set_page_config(layout="wide", page_icon="📝", page_title="Activities Demo 0.7.0")

    # Streamlit content
    st.title("Basic streamlit_book behavior")
    st.write("This tests mixing streamlit and streamlit_book libraries. Notice that the streamlit_book library is imported as stb but no multipage capability is enabled!!! Similar examples can be constructed for other activities.")

    # Default
    st.header("Question with minimal arguments")
    c1, c2 = st.columns([5,5])
    with c1:
        st.code("""
stb.true_or_false("Are you a robot?", False)
            """)
    with c2:
        stb.true_or_false("Are you a robot?", False)

    # Default
    st.header("Question with all optional arguments")
    c1, c2 = st.columns([5,4])
    with c1:
        st.code("""
stb.true_or_false("Are you a cyborg?", False, 
                  success='Pfiuuuuu!!!', 
                  error='RoBoTs NoT WeLcOmE to tHiS aPp', 
                  button='Check MY answer')
            """)
    with c2:
        stb.true_or_false("Are you a cyborg?", False, 
                            success='Pfiuuuuu!!!', 
                            error='RoBoTs NoT WeLcOmE to tHiS aPp', 
                            button='Check MY answer')

    # Custom question
    st.header("Question with custom behavior")
    c1, c2 = st.columns([4,3])
    with c1:
        st.code("""
checked_answer, correct_answer = stb.true_or_false("Are you a cyborg robot?", 
                                                   False, 
                                                   success="",
                                                   error="",
                                                   button='Check THIS answer')
if checked_answer:
    if correct_answer:
        st.info("Welcome fellow human!")            
        st.balloons()
    else:
        N = 10.0
        pb = st.progress(0.0)
        ph = st.empty()
        robot_message = ""
        for i in range(1, int(N+1)):
            pb.progress(i/N)
            robot_message += random.choice(["Bip ", "bip ", "Bop ", "bop "])
            ph.code(robot_message)
            time.sleep(.5)
else:
    st.write("You need to check the answer")
            """)
    with c2:
        checked_answer, correct_answer = stb.true_or_false("Are you a cyborg robot?", 
                                                            False, 
                                                            success="",
                                                            error="",
                                                            button='Check THIS answer')
        if checked_answer:
            if correct_answer:
                st.info("Welcome fellow human!")            
                st.balloons()
            else:
                N = 10.0
                pb = st.progress(0.0)
                ph = st.empty()
                robot_message = ""
                for i in range(1, int(N+1)):
                    pb.progress(i/N)
                    robot_message += random.choice(["BIP ", "bip ", "BOP ", "bop "])
                    ph.code(robot_message)
                    time.sleep(.5)
        else:
            st.write("You need to check the answer")
    

if __name__ == "__main__":
    main()
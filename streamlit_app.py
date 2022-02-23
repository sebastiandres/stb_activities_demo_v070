import streamlit as st
import streamlit_book as stb

def main():
    # Set wide display
    st.set_page_config(layout="wide")

    # Streamlit content
    st.title("Basic streamlit_book behavior")
    st.write("This tests mixing streamlit and streamlit_book libraries. Notice that the streamlit_book library is imported as stb but no multipage capability is enabled!!!")

    # Default
    st.header("Question with minimal argumens")
    stb.true_or_false("Are you a robot?", False)

    # Default
    st.header("Question with all optional arguments")
    stb.true_or_false("Are you a cyborg?", False, 
                        success='Pfiuuuuu!!!', 
                        error='RoBoTs NoT WeLcOmE to tHiS aPp', 
                        button='Check MY answer')

    # Custom question
    st.header("Question with custom behavior")
    checked_answer, correct_answer = stb.true_or_false("Are you a cyborg robot?", 
                                                        False, 
                                                        success="",
                                                        error="",
                                                        button='Check THIS answer')
    if checked_answer:
        if correct_answer:
            st.write("Welcome fellow human!")            
            st.balloons()
        else:
            st.write("Are you part of the Robot Apocalypse???")
    else:
        st.write("You need to check the answer")
    

if __name__ == "__main__":
    main()
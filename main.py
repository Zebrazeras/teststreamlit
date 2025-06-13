import streamlit as st
import pandas as pd 
with st.echo(): #โชว์โค้ดทั้งหมด
    st.title("Getting Stated Streamlit")
    st.write("Please Click")
    st.markdown("## Run")

    code = '''def hello():
        print("Hello"")'''
        
    run_btn = st.button("Run") #รับว่าถูกกดหรือยัง
    if run_btn:
        st.markdown("Button has already clicked")
        st.code(code, language='python')

    st.markdown("# NLP Task") 
    cols = st.columns(2)
    with cols[0]:
        age_inp = st.number_input("Input your age")
        st.markdown(f"Your age is {age_inp}") # f คือมีพารามิเตอร์ใส่เข้ามา

    with cols[1]:
        text_inp = st.text_input("Input your text")
        word_tokenize = "|".join(text_inp.split())
        st.markdown(f"{text_inp}")
        st.markdown(f"{word_tokenize}")
        
    df = pd.DataFrame({ 
        'first col' : [1, 2, 3, 4],
        'second col': [10, 20, 30, 40] 
    })
    st.dataframe(df)
    show_schart_btn = st.button("Show Chart")
    if show_schart_btn:
        st.line_chart(df, x='first col', y='second col')
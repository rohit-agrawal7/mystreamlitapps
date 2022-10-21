import streamlit as st
st.title('SIMPLE INTEREST CALCULATOR')
st.header('Calculate SI using this app')
principal= st.text_input('Principal', placeholder='Enter Principal (in Rs.)')
rate= st.number_input(label='Rate (in %)',min_value=0,max_value=5)
time= st.number_input(label='Time (in yrs.)',min_value=0,max_value=10)
click= st.button('Calculate SI')
if(click==True):
 SI=int(principal)*rate*time/100
 st.subheader(f'SI : Rs. {round(SI)}')
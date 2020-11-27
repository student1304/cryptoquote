import streamlit as st
from cryptoquote import encrypt

st.title('Cryptoquote by Alex')
st.write('Please enter a quote which you want to turn into a cryptoquote game')
quote = st.text_area('Enter or paste your quote here:')
encrpyted = encrypt(quote)
st.write('Your game begins:')
st.markdown(f'**{encrpyted}**')

st.text('---------------------------------------------------------------')
st.text("To print just use use browser's print function or press CTRL-P")
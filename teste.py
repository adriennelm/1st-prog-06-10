import streamlit as st

st.write("Oiee usuários do planeta Terra 🌎")
nome = st.text_input("Digite o seu username nesta galáxia... PS: sem ninguém ver!")
if nome: 
  st.write(nome.upper())

import streamlit as st

st.write("Oiee usuários do planeta Terra 🌎🌊🌫🌄")

nome = st.text_input("Digite o seu username nesta galáxia 🌌🪐... PS: sem ninguém ver! 👀")

if nome:
    st.write(f"{nome.upper()} — Você recebeu permissão de ocupar uma vaga pelo tempo de 1 vida humana, aproveite! 🌍")
    
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/The_Earth_seen_from_Apollo_17.jpg/600px-The_Earth_seen_from_Apollo_17.jpg",
        caption="Bem-vindo ao planeta Terra 🌍")

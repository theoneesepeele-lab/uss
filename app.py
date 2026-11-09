import streamlit as st

# URL oficial de la imagen/logo de la USS
logo_uss = "https://researchers.uss.cl/skins/custom/images/logo.svg"

# --- BARRA LATERAL ---
st.sidebar.image(logo_uss, width=160)
st.sidebar.title("Mi primera barra lateral de Streamlit")
st.sidebar.header("¡Hola, Barra Lateral!")
st.sidebar.text("Esto es una barra lateral")

if st.sidebar.button("Haz clic pero en la barra lateral"):
    st.sidebar.write("¡Botón de la barra lateral presionado!")

texto_barra = st.sidebar.text_input("Escribe algo en la barra:")
if texto_barra:
    st.sidebar.write(f"Escribiste en la barra: {texto_barra}")


# --- ÁREA PRINCIPAL ---
st.image(logo_uss, width=220)
st.title("Mi primera aplicación de Streamlit")
st.header("¡Hola, Streamlit!")
st.text("Esta es una aplicación simple")

if st.button("Haz clic"):
    st.write("¡Botón principal presionado!")

texto_principal = st.text_input("Escribe algo:")
if texto_principal:
    st.write(f"Escribiste: {texto_principal}")

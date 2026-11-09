import streamlit as st

# URL del escudo de la USS para que cargue directamente en la web
logo_uss = "https://upload.wikimedia.org/wikipedia/commons/2/23/Escudo_Universidad_San_Sebasti%C3%A1n.png"

# --- BARRA LATERAL ---
st.sidebar.image(logo_uss, width=120)
st.sidebar.title("Mi primera barra lateral de Streamlit")
st.sidebar.header("¡Hola, Barra Lateral!")
st.sidebar.text("Esto es una barra lateral")

if st.sidebar.button("Haz clic pero en la barra lateral"):
    st.sidebar.write("¡Botón de la barra lateral presionado!")

texto_barra = st.sidebar.text_input("Escribe algo en la barra:")
if texto_barra:
    st.sidebar.write(f"Escribiste en la barra: {texto_barra}")


# --- ÁREA PRINCIPAL ---
st.image(logo_uss, width=120)
st.title("Mi primera aplicación de Streamlit")
st.header("¡Hola, Streamlit!")
st.text("Esta es una aplicación simple")

if st.button("Haz clic"):
    st.write("¡Botón principal presionado!")

texto_principal = st.text_input("Escribe algo:")
if texto_principal:
    st.write(f"Escribiste: {texto_principal}")

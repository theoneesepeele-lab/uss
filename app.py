import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(
    page_title="Panel de Ingeniería y Programación - USS",
    page_icon="⚡",
    layout="wide"
)

# --- BARRA LATERAL (Sidebar Profesional) ---
st.sidebar.image("logo u.jpg", width=220)
st.sidebar.title("Panel de Control USS")
st.sidebar.markdown("---")

st.sidebar.subheader("Parámetros de Simulación")
modo_analisis = st.sidebar.selectbox(
    "Seleccione el modelo analítico:",
    ["Análisis Estructural (Matriz)", "Dinámica de Fluidos", "Procesamiento de Datos Masivos"]
)

umbral_alerta = st.sidebar.slider("Umbral crítico de tolerancia", 0.0, 100.0, 75.0)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Estado del Sistema:** Conectado al servidor central de simulación computacional.")


# --- ÁREA PRINCIPAL ---
st.title("🚀 Sistema Avanzado de Procesamiento e Ingeniería")
st.markdown("Plataforma interactiva desarrollada en **Python y Streamlit** para el análisis computacional de variables físicas y operativas.")

# Fila de métricas clave (KPIs estilo ejecutivo)
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Eficiencia Algorítmica", value="98.4%", delta="+1.2%")
col2.metric(label="Latencia de Red", value="14 ms", delta="-2 ms")
col3.metric(label="Registros Procesados", value="45,820", delta="+340")
col4.metric(label="Estado del Nodo", value="Óptimo", delta="Estable")

st.markdown("---")

# Visualización del logotipo principal integrado en el flujo de diseño
st.image("logo u.jpg", width=320)
st.header("Módulo de Visualización y Análisis Gráfico")

# Generación de datos dinámicos basados en programación científica
np.random.seed(42)
x_vals = np.linspace(0, 10, 100)
y_vals = np.sin(x_vals) * np.exp(-0.1 * x_vals) * 50 + np.random.normal(0, 2, 100)

# Pestañas para organizar la interfaz de forma experta
tab1, tab2, tab3 = st.tabs(["📊 Gráfico de Tendencias", "📝 Registro de Eventos (Logs)", "⚙️ Consola de Comandos"])

with tab1:
    st.subheader("Comportamiento Dinámico del Sistema")
    st.markdown("Gráfico en tiempo real generado mediante procesamiento matricial con `NumPy` y renderizado con `Matplotlib`.")
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(x_vals, y_vals, color="#1f77b4", linewidth=2.5, label="Señal Simulada")
    ax.axhline(y=umbral_alerta, color="red", linestyle="--", label=f"Umbral Crítico ({umbral_alerta})")
    ax.set_title(f"Modelo: {modo_analisis}", fontsize=12, fontweight='bold')
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Amplitud / Carga")
    ax.legend()
    ax.grid(True, linestyle=":", alpha=0.6)
    
    st.pyplot(fig)

with tab2:
    st.subheader("Registro de Transacciones y Ejecuciones")
    st.text("Últimos eventos del sistema recopilados por el kernel de Python:")
    
    # Simulación de consola de datos estructurados
    import pandas as pd
    df_logs = pd.DataFrame({
        "Timestamp": ["15:20:01", "15:20:05", "15:20:12", "15:20:18"],
        "Módulo": ["Core Engine", "Database", "API Gateway", "Security Layer"],
        "Nivel": ["INFO", "SUCCESS", "WARNING", "INFO"],
        "Mensaje": ["Inicialización completada", "Conexión establecida con éxito", "Alta demanda de recursos detectada", "Token validado correctamente"]
    })
    st.dataframe(df_logs, use_container_width=True)

with tab3:
    st.subheader("Consola Interactiva de Entrada")
    texto_usuario = st.text_input("Ingrese un comando de consulta para el sistema:")
    
    if st.button("Ejecutar Código / Proceso"):
        if texto_usuario:
            st.success(f"Comando ejecutado con éxito: `{texto_usuario}`")
            st.code(f"# Resultado de la simulación para la entrada:\noutput = process_query('{texto_usuario}')\n>>> Estado: Procesado sin errores.", language="python")
        else:
            st.warning("Por favor, ingrese un comando válido en la caja de texto antes de ejecutar.")

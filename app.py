import streamlit as st
import datetime

# Configuración
st.set_page_config(page_title="VITARA AETERNUM", layout="wide", page_icon="🌍")

# Estilos
st.markdown("""
<style>
    .main {background: linear-gradient(to bottom, #e6f7ff, #fff0e6); font-size: 24px;}
    h1 {font-size: 48px !important; color: #ff6b6b; text-align: center;}
    .stButton > button {font-size: 28px !important; padding: 20px; height: 80px; border-radius: 20px; background: #ff6b6b;}
    .card {background: #fff; border-radius: 20px; padding: 20px; margin: 20px 0; box-shadow: 0 4px 20px rgba(0,0,0,0.1);}
</style>
""", unsafe_allow_html=True)

# Memoria
st.session_state.setdefault('nombre', '')
st.session_state.setdefault('calorias', 0)
st.session_state.setdefault('agua', 0)
st.session_state.setdefault('sueño', 7)
st.session_state.setdefault('recordatorios', [])

# Header
st.title("🌍 VITARA AETERNUM")
st.markdown("<h2>Tu compañera eterna de salud y longevidad</h2>", unsafe_allow_html=True)

# Nombre
nombre = st.text_input("Tu nombre", value=st.session_state.nombre)
if nombre:
    st.session_state.nombre = nombre
    st.markdown(f"<div class='card'><h3>¡Hola {nombre}! Hoy cuidamos tu vitalidad.</h3></div>", unsafe_allow_html=True)

# Tabs
tabs = st.tabs(["🍽️ Nutrición", "😴 Sueño", "🔔 Recordatorios", "💊 Medicamentos", "💰 Premium"])

with tabs[0]:
    st.header("Nutrición Diaria")
    calorias = st.number_input("Calorías hoy", 0, 5000, st.session_state.calorias)
    agua = st.number_input("Vasos de agua", 0, 20, st.session_state.agua)
    if st.button("Guardar"):
        st.session_state.calorias = calorias
        st.session_state.agua = agua
        st.success("¡Nutrición guardada!")
        st.balloons()

with tabs[1]:
    st.header("Sueño")
    sueño = st.slider("Horas dormidas", 0, 12, st.session_state.sueño)
    if st.button("Guardar sueño"):
        st.session_state.sueño = sueño
        if sueño < 7:
            st.warning("¡Intenta dormir más para tu vitalidad!")
        else:
            st.success("¡Sueño óptimo!")
        st.balloons()

with tabs[2]:
    st.header("Recordatorios")
    nuevo = st.text_input("Nuevo recordatorio")
    hora = st.time_input("Hora")
    if st.button("Agregar"):
        st.session_state.recordatorios.append(f"{nuevo} a las {hora}")
        st.success("Recordatorio agregado.")
        st.balloons()

with tabs[3]:
    st.header("Medicamentos")
    med = st.text_input("Medicamento")
    hora_med = st.time_input("Hora para tomar")
    if st.button("Agregar medicamento"):
        st.session_state.recordatorios.append(f"Tomar {med} a las {hora_med}")
        st.success("Medicamento agregado.")
        st.balloons()

with tabs[4]:
    st.header("Premium – Acceso Total")
    st.write("• IA diagnóstica avanzada")
    st.write("• Seguimiento familiar")
    st.write("• Marketplace real")
    st.write("• Consultas con médicos")
    st.write("**$4.99/mes o $49/año**")
    if st.button("Activar Premium"):
        st.success("Redirigiendo a pago seguro...")
        st.balloons()

st.success("**Vitara Aeternum – tu amiga diaria para siempre.**")

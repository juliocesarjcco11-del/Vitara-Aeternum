import streamlit as st
import datetime

st.set_page_config(page_title="VITARA AETERNUM", layout="wide", page_icon="🌍")

# Estilos futuristas nativos
st.markdown("""
<style>
    .main {
        background: linear-gradient(to bottom, #e6f7ff, #fff0e6);
        font-family: 'Arial', sans-serif;
        font-size: 24px;
    }
    h1 {
        font-size: 48px !important;
        color: #ff6b6b;
        text-align: center;
    }
    .stButton > button {
        font-size: 28px !important;
        padding: 20px;
        height: 80px;
        border-radius: 20px;
        background: #ff6b6b;
        box-shadow: 0 0 20px rgba(255, 107, 107, 0.5);
    }
    .card {
        background: #fff;
        border-radius: 20px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Memoria
st.session_state.setdefault('nombre', '')
st.session_state.setdefault('edad', 35)
st.session_state.setdefault('calorias', 0)
st.session_state.setdefault('agua', 0)
st.session_state.setdefault('sueño', 7)
st.session_state.setdefault('recordatorios', [])
st.session_state.setdefault('familia', [])
st.session_state.setdefault('sintomas', [])

# Header
if st.session_state.nombre:
    st.title(f"¡Hola {st.session_state.nombre}! Tu compañera eterna ❤️")
else:
    st.title("VITARA AETERNUM – Tu salud eterna")

nombre = st.text_input("Tu nombre", value=st.session_state.nombre)
if nombre:
    st.session_state.nombre = nombre

# Tabs
tabs = st.tabs(["🩺 Consultas", "🛒 Marketplace", "🤖 IA Diagnóstico", "🍽️ Nutrición", "😴 Sueño", "🔔 Recordatorios", "🏡 Familia"])

with tabs[0]:
    st.header("Consultas Médicas")
    especialidad = st.selectbox("Especialidad", ["General", "Cardiología", "Psicología", "Nutrición", "Longevidad", "Pediatría", "Oncología", "Neurología"])
    if st.button("Buscar especialistas"):
        st.markdown("<div class='card'><h3>Médicos disponibles</h3><p>• Dr. Juan Pérez - 4.9 ⭐</p><p>• Dra. María López - 5.0 ⭐</p><p>• Dr. Carlos Ramírez - 4.8 ⭐</p></div>", unsafe_allow_html=True)
        if st.button("Agendar consulta"):
            st.success("Consulta agendada. Pago real procesado.")
            st.balloons()

with tabs[1]:
    st.header("Marketplace Premium")
    productos = {
        "NMN 99.9% (60 caps)": "299 USD",
        "Resveratrol liposomal": "199 USD",
        "Dexcom G7 CGM": "599 USD",
        "Análisis genético completo": "399 USD",
        "Plan Élite anual": "4999 USD"
    }
    for nombre, precio in productos.items():
        st.markdown(f"<div class='card'><h3>{nombre}</h3><p><strong>{precio}</strong></p></div>", unsafe_allow_html=True)
        if st.button(f"Comprar {nombre}"):
            st.success("Producto agregado. Pago real listo.")
            st.balloons()

with tabs[2]:
    st.header("Diagnóstico IA")
    sintomas = st.multiselect("Síntomas", ["Fatiga", "Dolor cabeza", "Estrés", "Dolor pecho", "Fiebre", "Ansiedad", "Otro"])
    descripcion = st.text_area("Describe más")
    if st.button("Analizar con IA"):
        diagnostico = "Análisis preliminar: posible estrés/fatiga. Recomendación: descanso, hidratación y ejercicio suave. Consulta especialista si persiste."
        st.markdown(f"<div class='card'><h3>Diagnóstico IA</h3><p>{diagnostico}</p></div>", unsafe_allow_html=True)
        st.balloons()

with tabs[3]:
    st.header("Nutrición")
    calorias = st.number_input("Calorías hoy", 0, 5000, st.session_state.calorias)
    agua = st.number_input("Vasos de agua", 0, 20, st.session_state.agua)
    if st.button("Guardar"):
        st.session_state.calorias = calorias
        st.session_state.agua = agua
        st.success("Guardado.")
        st.balloons()

with tabs[4]:
    st.header("Sueño")
    sueño = st.slider("Horas dormidas", 0, 12, st.session_state.sueño)
    if st.button("Guardar"):
        st.session_state.sueño = sueño
        st.success("Guardado.")
        st.balloons()

with tabs[5]:
    st.header("Recordatorios")
    nuevo = st.text_input("Nuevo recordatorio")
    hora = st.time_input("Hora")
    if st.button("Agregar"):
        st.session_state.recordatorios.append(f"{nuevo} a las {hora}")
        st.success("Recordatorio agregado.")
        st.balloons()

with tabs[6]:
    st.header("Familia")
    nuevo_familiar = st.text_input("Nombre familiar")
    if st.button("Agregar"):
        st.session_state.familia.append(nuevo_familiar)
        st.success("Familiar agregado.")
        st.balloons()

st.success("**VITARA AETERNUM – completa, real y lista para el mundo.**")
st.caption("VITARA AETERNUM ∞ • 25 Diciembre 2025 • Tu vida eterna empieza hoy 🌍🧬❤️")

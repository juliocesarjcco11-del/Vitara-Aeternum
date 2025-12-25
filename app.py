import streamlit as st
import datetime

st.set_page_config(page_title="VITARA AETERNUM", layout="wide", page_icon="🌍")

# Memoria completa
st.session_state.setdefault('nombre', '')
st.session_state.setdefault('edad', 35)
st.session_state.setdefault('condicion', 'Ninguna')
st.session_state.setdefault('modo', 'adulto')
st.session_state.setdefault('familia', [])
st.session_state.setdefault('calorias', 0)
st.session_state.setdefault('agua', 0)
st.session_state.setdefault('sueño', 7)
st.session_state.setdefault('recordatorios', [])
st.session_state.setdefault('habitos', {'ejercicio': False, 'meditacion': False})

# Voz guía
def voz_guia(texto, tipo="normal"):
    rate = "1.2" if tipo == "niño" else "0.9" if tipo == "cronico" else "1.0"
    st.components.v1.html(f"""
    <script>
        const utterance = new SpeechSynthesisUtterance("{texto}");
        utterance.lang = 'es-ES';
        utterance.rate = {rate};
        speechSynthesis.speak(utterance);
    </script>
    """, height=0)

# Detectar modo
if st.session_state.edad < 13:
    st.session_state.modo = 'niño'
elif st.session_state.condicion in ["Diabetes", "Cáncer", "Alzheimer", "Artritis"]:
    st.session_state.modo = 'cronico'

# Estilos según modo
if st.session_state.modo == 'niño':
    st.markdown("""
    <style>
        .main {background: linear-gradient(to bottom, #ffe0e0, #ffffe0); font-size: 28px !important;}
        h1 {color: #ff4081; font-size: 48px !important;}
        .stButton > button {background: #ff4081; font-size: 32px !important; height: 100px;}
    </style>
    """, unsafe_allow_html=True)
    voz_guia("¡Hola superhéroe! Vamos a ganar estrellas hoy.", "niño")
    st.title("🌟 VITARA PARA NIÑOS 🌟")
    st.balloons()

elif st.session_state.modo == 'cronico':
    st.markdown("""
    <style>
        .main {background: linear-gradient(to bottom, #e0f7fa, #e8f5e8); font-size: 26px !important;}
        h1 {color: #00695c; font-size: 44px !important;}
    </style>
    """, unsafe_allow_html=True)
    voz_guia("Hola guerrero. Hoy es un día más de victoria.", "cronico")
    st.title("💚 VITARA CONTIGO SIEMPRE 💚")

else:
    st.markdown("<style>.main {font-size: 24px !important;}</style>", unsafe_allow_html=True)
    voz_guia("Bienvenido a Vitara Aeternum.")
    st.title("🌍 VITARA AETERNUM")

# Nombre y configuración
nombre = st.text_input("Tu nombre", value=st.session_state.nombre)
if nombre:
    st.session_state.nombre = nombre

edad = st.slider("Edad", 1, 100, st.session_state.edad)
st.session_state.edad = edad

condicion = st.selectbox("Condición crónica", ["Ninguna", "Diabetes", "Cáncer", "Alzheimer", "Artritis", "Otra"])
st.session_state.condicion = condicion

# Tabs
tabs = st.tabs(["🏡 Familia", "🍽️ Nutrición", "😴 Sueño", "🔔 Recordatorios", "💪 Hábitos"])

with tabs[0]:
    st.header("Mi Familia")
    nuevo_familiar = st.text_input("Nombre del familiar")
    edad_familiar = st.slider("Edad", 1, 100, 30, key="edad_familiar")
    if st.button("Agregar familiar"):
        st.session_state.familia.append({"nombre": nuevo_familiar, "edad": edad_familiar})
        st.success(f"{nuevo_familiar} agregado.")
        st.balloons()

    for f in st.session_state.familia:
        st.write(f"👨‍👩‍👧‍👦 {f['nombre']} ({f['edad']} años)")

with tabs[1]:
    st.header("Nutrición")
    calorias = st.number_input("Calorías hoy", 0, 5000, st.session_state.calorias)
    agua = st.number_input("Vasos de agua", 0, 20, st.session_state.agua)
    if st.button("Guardar nutrición"):
        st.session_state.calorias = calorias
        st.session_state.agua = agua
        st.success("Guardado.")
        st.balloons()

with tabs[2]:
    st.header("Sueño")
    sueño = st.slider("Horas dormidas", 0, 12, st.session_state.sueño)
    if st.button("Guardar sueño"):
        st.session_state.sueño = sueño
        st.success("Guardado.")
        st.balloons()

with tabs[3]:
    st.header("Recordatorios")
    nuevo = st.text_input("Nuevo recordatorio")
    hora = st.time_input("Hora")
    if st.button("Agregar"):
        st.session_state.recordatorios.append(f"{nuevo} a las {hora}")
        st.success("Recordatorio agregado.")
        st.balloons()

with tabs[4]:
    st.header("Hábitos")
    ejercicio = st.checkbox("Ejercicio")
    meditacion = st.checkbox("Meditación")
    if st.button("Guardar hábitos"):
        st.session_state.habitos['ejercicio'] = ejercicio
        st.session_state.habitos['meditacion'] = meditacion
        st.success("Hábitos guardados.")
        st.balloons()

st.success("**Vitara Aeternum – tu compañera eterna.**")

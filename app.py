import streamlit as st
import datetime

st.set_page_config(page_title="VITARA AETERNUM", layout="wide", page_icon="🌍")

# Estilos futuristas nativos + fondos personalizados
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
    .specialty-container {
        background-size: cover;
        background-position: center;
        border-radius: 20px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 0 30px rgba(255, 107, 107, 0.7);
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

# Tabs principales
tabs = st.tabs(["🩺 Consultas", "🛒 Marketplace", "🤖 IA Diagnóstico", "🍽️ Nutrición", "😴 Sueño", "🔔 Recordatorios", "🏡 Familia"])

with tabs[0]:
    st.header("Consultas Médicas – Elige tu Especialista")
    # Lista de especialidades con fondos únicos (de las imágenes generadas)
    especialidades = {
        "General": "https://i.imgur.com/5zK8jLp.png",  # Logo original
        "Cardiología": "https://i.imgur.com/8vQfR3d.png",  # Glow alternativo
        "Psicología": "https://i.imgur.com/Gl1tCh9.png",  # Glitch 1
        "Nutrición": "https://i.imgur.com/9fKxP2m.png",  # Glitch 2
        "Longevidad": "https://i.imgur.com/Qw3vR8t.png",  # Glitch 3
        "Pediatría": "https://i.imgur.com/Hj5mN7v.png",  # Glitch 4
        "Oncología": "https://i.imgur.com/another1.png",  # Otra de la historia
        "Neurología": "https://i.imgur.com/another2.png",  # Otra
        "Urología": "https://i.imgur.com/another3.png",  # Otra
        "Cirugía": "https://i.imgur.com/another4.png",  # Otra
        "Dermatología": "https://i.imgur.com/another5.png",  # Agregada
        "Endocrinología": "https://i.imgur.com/another6.png",  # Agregada
        "Gastroenterología": "https://i.imgur.com/another7.png"  # Agregada
    }

    # Grid de icons/botones para especialistas
    cols = st.columns(3)
    for i, (esp, bg_url) in enumerate(especialidades.items()):
        with cols[i % 3]:
            if st.button(esp, key=esp):
                st.session_state.selected_esp = esp

    # Mostrar el consultorio del seleccionado
    if 'selected_esp' in st.session_state:
        esp = st.session_state.selected_esp
        bg_url = especialidades[esp]
        with st.expander(f"Consultorio de {esp}", expanded=True):
            st.markdown(f"""
            <div class='specialty-container' style='background-image: url("{bg_url}");'>
            """, unsafe_allow_html=True)
            st.header(f"Especialista en {esp}")
            st.write("Médicos disponibles:")
            st.markdown("<p>• Dr. Juan Pérez - 4.9 ⭐</p><p>• Dra. María López - 5.0 ⭐</p><p>• Dr. Carlos Ramírez - 4.8 ⭐</p>", unsafe_allow_html=True)
            if st.button("Agendar consulta", key=f"agendar_{esp}"):
                st.success("Consulta agendada. Pago real procesado.")
                st.balloons()
            if st.button("Generar Imagen Personalizada (IA)", key=f"gen_{esp}"):
                st.write("Generando imagen con IA... (Conecta a xAI API para real: https://x.ai/api)")
                st.image(bg_url, caption="Imagen generada para tu consultorio")
            st.markdown("</div>", unsafe_allow_html=True)

# Otras tabs permanecen similares, pero con fondos opcionales si quieres agregar
with tabs[1]:
    st.header("Marketplace Premium")
    # ... (mismo código que antes)

with tabs[2]:
    st.header("Diagnóstico IA")
    # ... (mismo)

with tabs[3]:
    st.header("Nutrición")
    # ... (mismo)

with tabs[4]:
    st.header("Sueño")
    # ... (mismo)

with tabs[5]:
    st.header("Recordatorios")
    # ... (mismo)

with tabs[6]:
    st.header("Familia")
    # ... (mismo)

st.success("**VITARA AETERNUM v21.0 – hermosa, única y lista para cambiar el mundo.**")
st.caption("VITARA AETERNUM ∞ • 25 Diciembre 2025 • Tu vida eterna empieza hoy 🌍🧬❤️")

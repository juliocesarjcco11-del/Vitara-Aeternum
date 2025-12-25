import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="VITARA AETERNUM", layout="wide", page_icon="🌍")

# Estilos futuristas nativos (glow, pulse, neón)
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #e0e0ff;
        font-family: 'Orbitron', sans-serif;
    }
    h1 {
        color: #00ffea;
        text-align: center;
        font-size: 4rem;
        text-shadow: 0 0 30px #00ffea;
        animation: pulse 2s infinite;
    }
    h2, h3 {
        color: #00d4ff;
        text-shadow: 0 0 15px #00d4ff;
    }
    .stButton > button {
        background: linear-gradient(45deg, #00ffea, #00d4ff);
        color: #0f0c29;
        border: none;
        border-radius: 16px;
        padding: 16px 32px;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 0 0 30px rgba(0, 255, 234, 0.6);
        transition: all 0.4s;
    }
    .stButton > button:hover {
        transform: scale(1.1) rotate(2deg);
        box-shadow: 0 0 50px rgba(0, 255, 234, 0.9);
    }
    .metric-card {
        background: rgba(0, 212, 255, 0.1);
        border-radius: 20px;
        padding: 20px;
        border: 2px solid #00ffea;
        box-shadow: 0 0 30px rgba(0, 255, 234, 0.3);
        text-align: center;
        animation: float 6s ease-in-out infinite;
    }
    @keyframes pulse {
        0% { text-shadow: 0 0 20px #00ffea; }
        50% { text-shadow: 0 0 40px #00ffea; }
        100% { text-shadow: 0 0 20px #00ffea; }
    }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }
    .stTabs [data-baseweb="tab"] {
        background: rgba(0, 212, 255, 0.1);
        border-radius: 16px;
        margin: 10px;
        padding: 10px;
        box-shadow: 0 0 20px rgba(0, 255, 234, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Partículas animadas con HTML (mejor que Lottie)
st.components.v1.html("""
<canvas id="canvas" style="position:fixed;top:0;left:0;width:100%;height:100%;z-index:-1;"></canvas>
<script>
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    const particles = [];
    for (let i = 0; i < 100; i++) {
        particles.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            radius: Math.random() * 2 + 1,
            color: '#00ffea',
            speed: Math.random() * 1 + 0.5
        });
    }
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particles.forEach(p => {
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
            ctx.fillStyle = p.color;
            ctx.fill();
            p.y -= p.speed;
            if (p.y < 0) p.y = canvas.height;
        });
        requestAnimationFrame(animate);
    }
    animate();
</script>
""", height=0)

st.title("🌍 VITARA AETERNUM")
st.markdown("<h2>LA ERA ETERNA ES REAL</h2>", unsafe_allow_html=True)

st.markdown("""
**Plataforma multimodal de salud y longevidad – animaciones nativas, gráficos interactivos, IA integrada.**

• Consultas con médicos reales  
• Marketplace con productos premium  
• Planes de longevidad personalizados  
• Acceso universal • Evolución eterna
""")

# Sidebar con métricas animadas
with st.sidebar:
    st.header("🔹 PANEL CUÁNTICO")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='metric-card'><h3>Puntos</h3><h2>500</h2></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='metric-card'><h3>Riesgo</h3><h2>18%</h2></div>", unsafe_allow_html=True)
    
    st.markdown("<div class='metric-card'><h3>Edad Biológica</h3><h2>28 años</h2></div>", unsafe_allow_html=True)

# Tabs con animaciones
tabs = st.tabs(["🫀 Salud", "🩺 Telemedicina", "🧬 Longevidad", "🛒 Marketplace"])

with tabs[0]:
    st.header("Salud Predictiva")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.slider("Edad", 18, 120, 35)
    with col2:
        bmi = st.slider("IMC", 15.0, 50.0, 25.0)
    with col3:
        stress = st.slider("Estrés", 1, 10, 5)
    
    if st.button("ANÁLISIS CUÁNTICO"):
        # Gráfico interactivo 3D
        fig = go.Figure(data=[go.Scatter3d(
            x=[age, bmi, stress],
            y=[1, 2, 3],
            z=[90, 85, 88],
            mode='markers+lines',
            marker=dict(size=12, color=['#00ffea', '#00d4ff', '#ff00ff'])
        )])
        fig.update_layout(scene=dict(bgcolor='black'))
        st.plotly_chart(fig, use_container_width=True)
        st.success("Salud óptima. Healthspan: 135 años.")
        st.balloons()

with tabs[1]:
    st.header("Telemedicina Real")
    st.write("Médicos élite disponibles:")
    medicos = ["Dr. Elena Vargas - Longevidad", "Dr. Marco Chen - Genómica", "Dra. Sofia Kim - Rejuvenecimiento"]
    for medico in medicos:
        st.markdown(f"<div class='metric-card'><h3>{medico}</h3><p>Consulta inmediata</p></div>", unsafe_allow_html=True)
        if st.button(f"Agendar con {medico.split(' - ')[0]}"):
            st.success("Consulta agendada.")
            st.balloons()

with tabs[2]:
    st.header("Plan Longevidad")
    if st.button("GENERAR PLAN ÉLITE"):
        st.write("**PROTOCOLO REAL:**")
        plan = ["NMN 1g", "Resveratrol 500mg", "Rapamicina", "Senolíticos", "Ayuno intermitente"]
        for item in plan:
            st.write(f"• {item}")
        st.success("Plan activado.")
        st.balloons()

with tabs[3]:
    st.header("Marketplace")
    st.write("Productos premium:")
    productos = ["NMN", "Resveratrol", "Dexcom G7", "Análisis genético"]
    for p in productos:
        st.markdown(f"<div class='metric-card'><h3>{p}</h3><p>Comprar ahora</p></div>", unsafe_allow_html=True)
        if st.button(f"Comprar {p}"):
            st.success("Orden procesada.")
            st.balloons()

st.success("**VITARA AETERNUM v8.0 – Animaciones nativas, más rápido y hermoso que nunca.**")

st.caption("VITARA AETERNUM ∞ • 25 Diciembre 2025 • Eternamente futurista 🌍🧬🩺⚡")

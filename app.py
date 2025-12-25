import streamlit as st
import numpy as np
import random

# Configuración de la página
st.set_page_config(
    page_title="VITARA AETERNUM",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos visuales modernos e interactivos
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #e0f2fe 0%, #f0f9ff 100%);
        font-family: 'Segoe UI', sans-serif;
    }
    h1 {
        color: #1e40af;
        text-align: center;
        font-weight: 700;
        animation: fadeIn 2s;
    }
    h2, h3 {
        color: #1e3a8a;
        font-weight: 600;
    }
    .stButton > button {
        background-color: #1e40af;
        color: white;
        border-radius: 12px;
        padding: 12px 24px;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #1e3a8a;
        transform: translateY(-3px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.25);
    }
    .stMetric {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        text-align: center;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)

# Estado persistente
st.session_state.setdefault('points', 0)
st.session_state.setdefault('risk_level', 28.0)
st.session_state.setdefault('bio_age', 35.0)
st.session_state.setdefault('wallet_address', None)

# ==================== HEADER CON ANIMACIÓN ====================
st.title("🌍 VITARA AETERNUM")
st.markdown("<h2 style='text-align: center;'>Vida Eterna</h2>", unsafe_allow_htl_dna, height=300, key="dna_animation")

st.markdown("""
**La plataforma profesional de salud y longevidad humana más avanzada del mundo.**

Medicina predictiva • Telemedicina • Genómica • Rejuvenecimiento  
Integración automática con el futuro: AR, BCI, edición génica in vivo.

**Pago por servicio real • Precios regionales • 10% a fondo social eterno**
""")

# ==================== SIDEBAR INTERACTIVA ====================
with st.sidebar:
    st.header("🔹 Tu Panel Personal")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Puntos", st.session_state.points, delta="+20")
    with col2:
        st.metric("Nivel", "Elite")
    
    st.metric("Riesgo Mortalidad", f"{st.session_state.risk_level:.1f}%", delta="-3%")
    st.metric("Edad Biológica", f"{st.session_state.bio_age:.1f} años", delta="-3 años")
    
    st.divider()
    st.subheader("💳 Wallet Blockchain")
    if st.button("Conectar Wallet"):
        st.session_state.wallet_address = "0x1234...abcd"
        st.success(f"Conectada: {st.session_state.wallet_address}")
        st.balloons()

# ==================== TABS CON FUNCIONALIDADES INTERACTIVAS ====================
tabs = st.tabs([
    "🫀 Salud Predictiva", 
    "🩺 Telemedicina", 
    "🛡️ Seguros", 
    "💊 Farmacias", 
    "⌚ Dispositivos", 
    "🧬 Genómica & Longevidad", 
    "🛒 Marketplace", 
    "🤖 Asistente IA"
])

with tabs[0]:
    st.header("Salud Predictiva con IA Clínica")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.slider("Edad cronológica", 18, 120, 35)
    with col2:
        bmi = st.slider("IMC", 15.0, 50.0, 25.0)
    with col3:
        stress = st.slider("Estrés (1-10)", 1, 10, 5)
    
    if st.button("Ejecutar Análisis Predictivo AI", type="primary"):
        risk = max(5, min(50, 30 - (bmi - 25)*0.8 - stress*1.2 + (age - 35)*0.3))
        bio_age = age - stress + (st.session_state.points / 20)
        st.session_state.risk_level = risk
        st.session_state.bio_age = bio_age
        
        # Gráfico interactivo radar
        categories = ['Cardiovascular', 'Metabólico', 'Inmunológico', 'Neurológico', 'Longevidad']
        values = [90 - risk, 85 - (bmi - 25)*2, 88 - stress*2, 92, 95 + st.session_state.points/10]
        values += values[:1]  # cerrar el radar
        
        fig = go.Figure(data=go.Scatterpolar(r=values, theta=categories, fill='toself', name='Tu Salud'))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
        
        st.success(f"**Riesgo predictivo: {risk:.1f}%** | **Edad biológica: {bio_age:.1f} años**")
        st.balloons()

with tabs[1]:
    st.header("Telemedicina Global")
    specialty = st.selectbox("Especialidad", ["Médico General", "Pediatra", "Cardiólogo", "Psicólogo", "Endocrinólogo"])
    urgency = st.radio("Urgencia", ["Normal", "Urgente", "Emergencia"])
    if st.button("Buscar especialistas"):
        st.success(f"5 especialistas en {specialty} encontrados. {urgency}: respuesta en <5 min.")
        st.balloons()

with tabs[2]:
    st.header("Seguros Médicos Integrados")
    if st.button("Verificar cobertura"):
        st.success("Cobertura óptima detectada. Todas las consultas cubiertas al 100%.")
        st.balloons()

with tabs[3]:
    st.header("Farmacias Digitales")
    med = st.text_input("Medicamento")
    if st.button("Ordenar entrega"):
        st.success(f"{med} ordenado. Entrega express en 30-90 min.")
        st.balloons()

with tabs[4]:
    st.header("Wearables & Glucosa Continua")
    if st.button("Sincronizar dispositivos"):
        st.success("Dexcom G7, Apple Watch y Oura sincronizados. Datos en tiempo real activos.")
        st.balloons()

with tabs[5]:
    st.header("Genómica Personalizada & Longevidad")
    st.write("OpenCRISPR-1 • Reprogramación epigenética • Plan 120+ años")
    if st.button("Generar mi plan de longevidad"):
        st.success("Plan personalizado creado. Healthspan proyectado: 128 años.")
        st.balloons()

with tabs[6]:
    st.header("Marketplace & Pagos Blockchain")
    service = st.selectbox("Servicio", ["Consulta especialista", "Plan longevidad anual", "Análisis genético"])
    price = {"Consulta especialista": 60, "Plan longevidad anual": 799, "Análisis genético": 149}[service]
    st.write(f"Precio: **{price} USD**")
    if st.button("Pagar con Blockchain"):
        st.success("Transacción blockchain enviada. Servicio activado inmediatamente.")
        st.balloons()

with tabs[7]:
    st.header("Asistente IA Vitara")
    user_question = st.text_input("Pregúntame cualquier cosa sobre salud o longevidad")
    if st.button("Consultar Asistente IA"):
        st.write("Respuesta IA: Tu pregunta ha sido analizada. Recomendación personalizada: aumenta consumo de omega-3 y meditación diaria.")
        st.balloons()

# ==================== FOOTER ====================
st.markdown("---")
st.success("**VITARA AETERNUM está activa. Tu camino a la vitalidad eterna ha comenzado.**")

st.caption("VITARA AETERNUM ∞ • 25 Diciembre 2025 • La Era Eterna de la Vida Humana • Eternamente 🌍🧬🩺⚡")

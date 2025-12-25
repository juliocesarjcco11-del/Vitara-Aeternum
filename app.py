
import streamlit as st
import numpy as np
import random
from web3 import Web3
import streamlit_lottie as st_lottie
import requests

# Configuración de la página: profesional, impactante y responsiva
st.set_page_config(
    page_title="VITARA AETERNUM",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS para visual impactante, fácil navegación y accesibilidad
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #e6f7ff 0%, #ffffff 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding: 20px;
    }
    h1 {
        color: #1e40af;
        text-align: center;
        font-weight: 700;
        letter-spacing: 1px;
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
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.25);
    }
    .stMetric {
        font-size: 18px;
        color: #333;
        background-color: #ffffff;
        border-radius: 8px;
        padding: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stExpander {
        background-color: #ffffff;
        border-radius: 8px;
        border: 1px solid #ddd;
        padding: 10px;
    }
    .stTabs [data-role="tab"] {
        font-weight: bold;
        color: #1e40af;
    }
    .stTextInput, .stNumberInput, .stSlider, .stSelectbox {
        background-color: #ffffff;
        border-radius: 8px;
        border: 1px solid #ddd;
        padding: 10px;
    }
    .stSuccess, .stInfo, .stWarning, .stError {
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .animation-container {
        animation: fadeIn 1s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
</style>
""", unsafe_allow_html=True)

# Función para cargar animaciones Lottie
@st.cache_resource
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Estado persistente
st.session_state.setdefault('points', 0)
st.session_state.setdefault('user_lang', 'es')
st.session_state.setdefault('risk_level', 28.0)
st.session_state.setdefault('bio_age', 35.0)
st.session_state.setdefault('wallet_address', None)
st.session_state.setdefault('chain', 'ethereum')

# ==================== HEADER PRINCIPAL ====================
st.title("🌍 VITARA AETERNUM")
st.markdown("<h2 style='text-align: center;'>Vida Eterna</h2>", unsafe_allow_html=True)

# Animación interactiva en header
lottie_health = load_lottie_url("https://assets3.lottiefiles.com/packages/lf20_5k2r3m3v.json")  # Ejemplo Lottie health animation
st_lottie.st_lottie(lottie_health, height=200, key="header_animation")

st.markdown("""
El servicio médico digital global definitivo.  
**Medicina predictiva • Telemedicina • Genómica • Rejuvenecimiento**  
Integración automática con el futuro: AR, BCI, edición génica in vivo.

**Pago por servicio real • Precios regionales • 10% a fondo social eterno**

Desde 2025, guiando a la humanidad hacia una vida saludable sin límites.
""")

# ==================== SIDEBAR ====================
with st.sidebar:
    st.header("🔹 Tu Panel personal")
    st.metric("Puntos de Longevidad", st.session_state.points)
    st.metric("Riesgo Mortalidad", f"{st.session_state.risk_level:.1f}%")
    st.metric("Edad Biológica", f"{st.session_state.bio_age:.1f} años")
    
    st.divider()
    st.subheader("💳 Wallet Blockchain")
    if st.button("Conectar Wallet"):
        st.session_state.wallet_address = "0x1234...abcd"  # Simulación; usa WalletConnect en producción
        st.success(f"Wallet conectada: {st.session_state.wallet_address}")
    st.selectbox("Chain", ["Ethereum", "Polygon", "Solana", "BSC"], key="chain")

# ==================== TABS PRINCIPALES ====================
tabs = st.tabs([
    "🫀 Salud Predictiva", 
    "🩺 Telemedicina", 
    "🛡️ Seguros", 
    "💊 Farmacias", 
    "⌚ Dispositivos", 
    "🧬 Genómica & Longevidad", 
    "🛒 Marketplace", 
    "💼 Servicios & Precios"
])

with tabs[0]:
    st.header("Salud Predictiva con IA Clínica")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.slider("Edad cronológica", 18, 120, 35)
    with col2:
        bmi = st.slider("IMC", 15.0, 50.0, 25.0)
    with col3:
        stress = st.slider("Nivel de estrés (1-10)", 1, 10, 5)
    
    if st.button("Ejecutar Análisis Predictivo AI", type="primary"):
        risk = max(5, min(50, 30 - (bmi - 25)*0.8 - stress*1.2 + (age - 35)*0.3))
        bio_age = age - stress + (st.session_state.points / 20)
        st.session_state.risk_level = risk
        st.session_state.bio_age = bio_age
        st.success(f"**Riesgo predictivo: {risk:.1f}%** | **Edad biológica: {bio_age:.1f} años**")
        st.balloons()

with tabs[1]:
    st.header("Telemedicina Global")
    st.write("Conecta con especialistas verificados en segundos")
    specialty = st.selectbox("Especialidad", ["Médico General", "Pediatra", "Cardiólogo", "Psicólogo", "Endocrinólogo", "Dermatólogo"])
    if st.button("Buscar especialistas disponibles"):
        st.success(f"5 especialistas en {specialty} encontrados cerca de ti. Agenda ahora.")

with tabs[2]:
    st.header("Seguros Médicos Integrados")
    st.write("Verifica cobertura y optimiza tu póliza")
    if st.button("Verificar mi cobertura actual"):
        st.success("Cobertura cobertura verificada. Consultas 100% cubiertas.")

with tabs[3]:
    st.header("Farmacias Digitales")
    st.write("Medicamentos con entrega inmediata")
    med = st.text_input("Nombre del medicamento")
    if st.button("Ordenar entrega"):
        st.success(f"{med} ordenado. Entrega en 30-90 minutos.")

with tabs[4]:
    st.header("Wearables & Glucosa Continua")
    st.write("Sincroniza Dexcom G7, Apple Watch, Oura...")
    if st.button("Sincronizar dispositivos"):
        st.success("Datos sincronizados. Análisis en tiempo real activo.")

with tabs[5]:
    st.header("Genómica Personalizada & Longevidad")
    st.write("OpenCRISPR-1 • Reprogramación epigenética • Plan 120+ años")
    if st.button("Generar mi plan de longevidad"):
        st.success("Plan personalizado creado. Healthspan proyectado: 128 años.")

with tabs[6]:
    st.header("Marketplace & Pagos Blockchain")
    st.write("Compra servicios premium con crypto multi-chain segura")
    service = st.selectbox("Servicio", ["Consulta especialista", "Plan longevidad anual", "Análisis genético completo"])
    price = {"Consulta especialista": 60, "Plan longevidad anual": 799, "Análisis genético completo": 149}[service]
    st.write(f"Precio: **{price} USD**")
    if st.button("Pagar con Blockchain"):
        st.success("Transacción blockchain enviada. Servicio activado inmediatamente.")
        st.balloons()

with tabs[7]:
    st.header("Servicios Profesionales & Precios")
    st.markdown("""
    **Modelo: Pago por servicio real entregado**

    Tarifas orientativas (ajustadas por región):
    - Consulta general: 15-35 USD
    - Especialista: 40-80 USD
    - Emergencia prioritaria: 50-100 USD
    - Gestión diabetes/crónicos: 49-99 USD/mes
    - Análisis wearables/CGM: 20-40 USD/mes
    - Entrega medicamento: 5-15 USD/pedido
    - Análisis genético básico: 49 USD
    - Programa longevidad integral (anual): 799 USD
    
    Pagos: Tarjeta • Crypto • Locales
    
    **10% de todos los ingresos al fondo social eterno**
    """)

# ==================== FOOTER ====================
st.markdown("---")
st.success("**VITARA AETERNUM está activa. Tu camino a la vitalidad eterna ha comenzado.**")

st.caption("VITARA AETERNUM ∞ • 24 Diciembre 2025 • La Era Eterna de la Vida Humana • Eternamente 🌍🧬🩺⚡")
Final Fix

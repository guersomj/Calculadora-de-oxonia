import streamlit as st
import math

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Calculadora de Oxonia", page_icon="🧪", layout="centered")

# Regla: 70 mL por 30 L
ML_POR_30L = 70
L_BASE = 30

def oxonia_ml(litros_agua: float) -> float:
    return (litros_agua / L_BASE) * ML_POR_30L

def ceil_1_decimal(valor: float) -> float:
    """Redondea hacia arriba a 1 decimal."""
    return math.ceil(valor * 10) / 10

# ---------------- DATOS SISTEMAS ----------------
# Nota: "tanque" es el volumen de CADA tanque (Tanque 1 y Tanque 2).
SISTEMAS = {
    "BIG": {"tanque": 1200, "proceso": 670},
    "PBS": {"tanque": 1200, "proceso": 1000},
    "BBG": {"tanque": 500, "proceso": 120},
    "BGA": {"tanque": 500, "proceso": 180},
    "5GL": {"tanque": 500, "proceso": 200},
    "BBB": {"tanque": 500, "proceso": 80},
    "BBS": {"tanque": 200, "proceso": 30},
}

# ---------------- UI ----------------
st.title("🧪 Calculadora de Oxonia")
st.caption("Regla: por cada 30 L de agua → 70 mL de Oxonia")
st.divider()

sistema = st.radio(
    "Selecciona el sistema",
    options=list(SISTEMAS.keys()),
    horizontal=True
)

datos = SISTEMAS[sistema]
litros_tanque = datos["tanque"]
litros_proceso = datos["proceso"]

st.subheader(f"Sistema seleccionado: {sistema}")

c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Tanque 1 (L)", f"{litros_tanque}")
with c2:
    st.metric("Tanque 2 (L)", f"{litros_tanque}")
with c3:
    st.metric("Proceso (L)", f"{litros_proceso}")

st.caption("Nota: El volumen del Proceso se suma automáticamente al Tanque 1.")
st.divider()

# ---------------- CÁLCULO ----------------
tanque1_total = litros_tanque + litros_proceso
tanque2_total = litros_tanque

ox1_ml = math.ceil(oxonia_ml(tanque1_total))   # mL enteros hacia arriba
ox2_ml = math.ceil(oxonia_ml(tanque2_total))

ox1_l = ceil_1_decimal(ox1_ml / 1000)         # Litros, 1 decimal hacia arriba
ox2_l = ceil_1_decimal(ox2_ml / 1000)

total_ox_l = ceil_1_decimal((ox1_ml + ox2_ml) / 1000)

# ---------------- RESULTADOS ----------------
st.subheader("🧪 Oxonia a agregar (L)")

r1, r2 = st.columns(2)
with r1:
    st.metric("Tanque 1", f"{ox1_l} L")
with r2:
    st.metric("Tanque 2", f"{ox2_l} L")

st.divider()
st.metric("Oxonia total a preparar", f"{total_ox_l} L")

st.caption("Valores redondeados hacia arriba para asegurar concentración efectiva.")

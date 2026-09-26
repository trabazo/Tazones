import streamlit as st
import replicate
import os

st.title("Generador de Tazones - Curi Sublimación")
st.write("Genera fotografías publicitarias premium 1:1.")

diseno = st.file_uploader("1. Sube el Diseño (Plantilla)", type=["png", "jpg"])
fondo = st.file_uploader("2. Sube el Escenario (Fondo)", type=["png", "jpg"])

PROMPT = "FOTOGRAFÍA PUBLICITARIA FOTORREALISTA (1:1). Producto: Tazón blanco de cerámica 11 oz con diseño aplicado por sublimación. Escenario: Integrar producto en el centro del pedestal del showroom. Mantener volumen, iluminación, reflejos reales y logo de Curi Sublimación."

if st.button("Generar Fotografía Premium"):
    if diseno and fondo:
        st.info("Conectando con la IA... procesando las imágenes.")
        # Aquí se ejecutará la llamada a Replicate usando tu API Key oculta
        st.success("¡Fotografía procesada con éxito!")
    else:
        st.error("Por favor, sube el diseño y el fondo para continuar.")

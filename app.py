import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="Detector de Cajas", page_icon="📦", layout="centered")
st.title("📦 Detector de Cajas Vacías y Llenas con IA")
st.markdown("Sube una imagen para que el modelo detecte las cajas vacías y llenas.")

imagen_subida = st.file_uploader("📤 Sube una imagen", type=["jpg", "jpeg", "png"])

if imagen_subida:
    st.image(imagen_subida, caption="📷 Imagen Original", use_column_width=True)

if st.button("🚀 Procesar imagen"):
    if imagen_subida is not None:
        try:
            with st.spinner("Procesando imagen... ⏳"):
                files = {"file": imagen_subida.getvalue()}
                response = requests.post("http://localhost:8000/procesar/", files=files)

                if response.status_code == 200:
                    imagen_procesada = Image.open(io.BytesIO(response.content))
                    st.success("✅ Procesamiento completado")
                    st.image(imagen_procesada, caption="📦 Imagen Procesada", use_column_width=True)
                else:
                    st.error(f"❌ Error al procesar la imagen. Código: {response.status_code}")
        except Exception as e:
            st.error(f"⚠️ Error al conectarse con el backend: {str(e)}")
    else:
        st.warning("Por favor, sube una imagen antes de procesar.")
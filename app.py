import streamlit as st
from freeGPT import Client  # Asegúrate de que esta es la importación correcta
from PIL import Image
from io import BytesIO

# Si el cliente no se puede instanciar, usa la función adecuada para crear la generación
def generate_image(prompt):
    # Aquí debes llamar a la función adecuada de freeGPT para generar la imagen
    return Client.create_generation("prodia", prompt)  # Ajusta esto si es necesario

# Título de la aplicación
st.title("Generador de Imágenes con AI")

# Input del usuario
prompt = st.text_input("Ingresa tu prompt para generar una imagen:")

if st.button("Generar Imagen"):
    if prompt:
        try:
            # Generar la imagen usando el prompt
            resp = generate_image(prompt)
            image = Image.open(BytesIO(resp))

            # Mostrar la imagen en la aplicación
            st.image(image, caption="Imagen generada", use_column_width=True)
            st.success("🤖: Imagen mostrada.")
        except Exception as e:
            st.error(f"🤖: Ocurrió un error: {e}")
    else:
        st.warning("Por favor, ingresa un prompt.")

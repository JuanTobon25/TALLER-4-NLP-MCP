import streamlit as st
from agents.agent1 import Agent1
from agents.agent2 import Agent2
from utils.mcp_protocol import send_message

# --- Inicializar agentes ---
agent1 = Agent1()
agent2 = Agent2()

st.set_page_config(page_title="Demo MCP con Agentes", layout="centered")

st.title("🔗 Demostración MCP - Comunicación entre Agentes")
st.write("Este demo muestra cómo dos agentes (planificador y ejecutor) se comunican usando un protocolo estilo MCP.")

# Entrada del usuario
user_input = st.text_input("Escribe una instrucción:", "Consulta el clima en Bogotá")

if st.button("Enviar"):
    with st.spinner("Procesando..."):
        request, response = send_message(agent1, agent2, user_input)

        st.subheader("📤 Mensaje enviado por Agente 1 (Cliente)")
        st.json(request)

        st.subheader("📥 Respuesta de Agente 2 (Servidor)")
        st.json(response)

        st.success(f"✅ Resultado final: {response['result']}")

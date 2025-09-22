import json
import requests

class Agent2:
    def __init__(self, name="Agente Ejecutor"):
        self.name = name

    def handle_request(self, request: dict) -> dict:
        """Recibe la petición y responde simulando un servidor MCP."""
        instruction = request["params"]["instruction"]

        # Ejemplo simple: si el usuario pide clima, llama a API pública
        if "clima" in instruction.lower():
            city = "Bogotá"
            try:
                r = requests.get(f"https://wttr.in/{city}?format=3")
                result = r.text
            except:
                result = "No se pudo obtener el clima."
        else:
            result = f"Tarea recibida: {instruction}"

        response = {
            "jsonrpc": "2.0",
            "result": result,
            "id": request["id"]
        }
        return response

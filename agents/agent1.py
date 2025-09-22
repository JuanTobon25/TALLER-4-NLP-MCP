import json

class Agent1:
    def __init__(self, name="Agente Planificador"):
        self.name = name

    def create_task(self, user_input: str) -> dict:
        """Genera una petición en formato JSON-RPC simulando MCP."""
        request = {
            "jsonrpc": "2.0",
            "method": "execute_task",
            "params": {"instruction": user_input},
            "id": 1
        }
        return request
        

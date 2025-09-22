def send_message(agent_client, agent_server, user_input: str):
    """Simula la comunicación entre cliente (Agent1) y servidor (Agent2)."""
    request = agent_client.create_task(user_input)
    response = agent_server.handle_request(request)
    return request, response

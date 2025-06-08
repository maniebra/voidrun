def enqueue_websocket_execution(
    connection,
    lang: str,
    code_files,
    stdin_file=None,
    setup_commands=None,
    network_enabled: bool = False,
):
    # Placeholder for websocket-based queuing
    # connection is assumed to be an open WebSocket connection
    connection.send_text("[VoidRun] WebSocket queuing not yet implemented.")

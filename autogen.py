async def add_agent_tools() -> None:
    """Add tools for the agent."""
    font_file_info = None

    # Add the functions tool
    toolset.add(functions)

    # Add the tents data sheet to a new vector data store
    vector_store = await utilities.create_vector_store(
        project_client,
        files=[TENTS_DATA_SHEET_FILE],
        vector_store_name="Contoso Product Information Vector Store",
    )
    file_search_tool = FileSearchTool(vector_store_ids=[vector_store.id])
    toolset.add(file_search_tool)

    # Add the code interpreter tool
    # code_interpreter = CodeInterpreterTool()
    # toolset.add(code_interpreter)

    # Add multilingual support to the code interpreter
    # font_file_info = await utilities.upload_file(project_client, utilities.shared_files_path / FONTS_ZIP)
    # code_interpreter.add_file(file_id=font_file_info.id)

    # Add the Bing grounding tool
    # bing_connection = await project_client.connections.get(connection_name=BING_CONNECTION_NAME)
    # bing_grounding = BingGroundingTool(connection_id=bing_connection.id)
    # toolset.add(bing_grounding)

    return font_file_info
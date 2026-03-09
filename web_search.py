#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from langchain.tools import tool
from tavily import TavilyClient
from typing import Dict, Any

load_dotenv()

tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

@tool
def web_search(search_query:str)->dict[str,Any]:
    """search the web for information"""
    return tavily_client.search(search_query)


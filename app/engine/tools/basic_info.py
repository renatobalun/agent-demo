from llama_index.core.tools.tool_spec.base import BaseToolSpec
import qdrant_client
import os
import json
from dotenv import load_dotenv

load_dotenv()

qdrant_link = os.getenv("QDRANT_LINK")
#qdrant_api_key = os.getenv("QDRANT_API_KEY")
basic_info_vdb_collection_name = os.getenv("BASIC_INFO_VDB_COLLECTION") 

class BasicInfoSpec(BaseToolSpec):
    """Basic Info Spec"""

    spec_functions = ["basic_info"]

    def basic_info(self):
        "A tool for getting basic information about hotel. It has information about the room, restaurant, spa and wellness zone, bussines clients, pets and more."

        client = qdrant_client.QdrantClient(
            qdrant_link
        )

        points = client.scroll(
            collection_name=basic_info_vdb_collection_name,
            limit=10000
        )

        result = ""
        if points:
            for point in points:
                if point:
                    for p in point:
                        payload = None
                        if hasattr(p, 'payload'):
                            payload = p.payload
                            if payload["_node_content"]:
                                result = result + json.loads(payload["_node_content"])['text']

        return result

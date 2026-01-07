from llama_index.core.tools.tool_spec.base import BaseToolSpec
import qdrant_client
import os
import json
from dotenv import load_dotenv

load_dotenv()

qdrant_link = os.getenv("QDRANT_LINK")
qdrant_api_key = os.getenv("QDRANT_API_KEY") 
events_vdb_collection_name = os.getenv("EVENTS_VDB_COLLECTION") 

class EventsSpec(BaseToolSpec):
    """Events Spec"""

    spec_functions = ["events"]

    def events(self):
        "A tool for getting information about events, concerts and atractions in the area."

        client = qdrant_client.QdrantClient(
            qdrant_link,
            api_key=qdrant_api_key,
            https=True,
            port=None
        )

        points = client.scroll(
            collection_name=events_vdb_collection_name,
            limit=10000
        )
        
        nodes = []
        if points:
            for point in points:
                if point:
                    for p in point:
                        payload = None
                        if hasattr(p, 'payload'):
                            payload = p.payload
                            if payload.get("_node_content"):
                                nodes.append({
                                    'text': json.loads(payload["_node_content"])['text'],
                                    'node_number': int(payload.get("node_number", 0))
                                })

        # Sort nodes by node_number
        sorted_nodes = sorted(nodes, key=lambda x: x['node_number'])

        # Combine the text in order
        result = ''.join(node['text'] for node in sorted_nodes)

        return result

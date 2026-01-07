from llama_index.core.tools.tool_spec.base import BaseToolSpec
import qdrant_client
import os
import json
from dotenv import load_dotenv

load_dotenv()

qdrant_link = os.getenv("QDRANT_LINK")
qdrant_api_key = os.getenv("QDRANT_API_KEY") 
offers_vdb_collection_name = os.getenv("OFFERS_VDB_COLLECTION") 

class OffersSpec(BaseToolSpec):
    """Offers Spec"""

    spec_functions = ["offers"]

    def offers(self):
        "A tool for getting information about special offers."

        client = qdrant_client.QdrantClient(
            qdrant_link,
            api_key=qdrant_api_key,
            https=True,
            port=None
        )

        points = client.scroll(
            collection_name=offers_vdb_collection_name,
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

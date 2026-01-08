import logging
import os

from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
)
from llama_index.vector_stores.qdrant import QdrantVectorStore
import qdrant_client
from dotenv import load_dotenv

load_dotenv()
#qdrant_api_key = os.getenv("QDRANT_API_KEY")
qdrant_link = os.getenv("QDRANT_LINK")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def generate_datasource():
    documents = SimpleDirectoryReader("../../data/events").load_data()
    logger.info("Connecting to qdrant")

    client = qdrant_client.QdrantClient(
        qdrant_link
    )
    logger.info("Creating new index")

    vector_store = QdrantVectorStore(client=client, collection_name="grand_hotel_events")
    logger.info("Created QdrantVectorStore")

    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    logger.info("Created StorageContext")
    
    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
    )

    logger.info("Done")
    
if __name__ == "__main__":
    generate_datasource()

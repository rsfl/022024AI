import os

use_serverless = True

from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Pinecone
from pinecone import ServerlessSpec, PodSpec
import time
from pinecone import Pinecone


from pinecone import ServerlessSpec, PodSpec
import time

if use_serverless:
    spec = ServerlessSpec(cloud='aws', region='us-west-2')
else:
    # if not using a starter index, you should specify a pod_type too
    spec = PodSpec()

# check for and delete index if already exists
index_name = 'langchain-retrieval-augmentation-fast'
if index_name in pc.list_indexes().names():
    pc.delete_index(index_name)

# we create a new index
pc.create_index(
        index_name,
        dimension=1536,  # dimensionality of text-embedding-ada-002
        metric='dotproduct',
        spec=spec
    )

# wait for index to be initialized
while not pc.describe_index(index_name).status['ready']:
    time.sleep(1)
# initialize connection to pinecone (get API key at app.pinecone.io)
api_key = '267d76c0-2add-4020-be1d-9492d08b2e9c'
pc = Pinecone(api_key=api_key)
text_field = "text"

index = pc.Index(index_name)
index.describe_index_stats()

vectorstore = Pinecone(
    index, embed.embed_query, text_field
)
query = "who was Benito Mussolini?"

import os

from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, UnstructuredPDFLoader
# from langchain_community.vectorstores.pgvector import PGVector
from langchain_experimental.text_splitter import SemanticChunker
# import semanticChunker
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
# from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores import Chroma

import shutil

CHROMA_PATH = "chroma"


load_dotenv()
loader = DirectoryLoader(
    # os.path.abspath("./pdf-documents"),
    os.path.abspath("C:/Users/tusca/OneDrive/Documents/GitHub/LLMBootcamp/nextjsLLMapp-part1/pdf-documents"),
    # "../pdf-documents",
    glob="**/*.pdf",
    use_multithreading=True,
    show_progress=True,
    max_concurrency=50,
    loader_cls=UnstructuredPDFLoader,
)

docs = loader.load()
# print(docs[0])
embeddings = OpenAIEmbeddings(model='text-embedding-ada-002', )

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
texts = text_splitter.split_documents(docs[0])

# print(texts)


persist_directory = "./chroma"
vectordb = Chroma.from_documents(
    texts, OpenAIEmbeddings(), persist_directory=persist_directory
)
vectordb.persist()

# testing
# question = "Who was the best president?"
# docs = vectordb.similarity_search(question)
# # print(len(docs))

# llm = ChatOpenAI(temperature=0, model='gpt-4-1106-preview', streaming=True)

# response_message = llm.invoke(
#     "Simulate a rap battle between Stephen Colbert and John Oliver"
# )

# print(response_message.content)

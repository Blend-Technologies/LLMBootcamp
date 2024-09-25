import os
from operator import itemgetter
from typing import TypedDict
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
# from langchain_community.vectorstores.pgvector import PGVector
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.runnables import RunnableParallel
from langchain_core.runnables import RunnablePassthrough

from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores import Chroma

load_dotenv()

# vector_store = PGVector(
#     collection_name="collection164",
#     connection_string="postgresql+psycopg://postgres@localhost:5432/database164",
#     embedding_function=OpenAIEmbeddings()
# )

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
vector_store = Chroma(
    # collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma",  # Where to save data locally, remove if not neccesary
)

# print(vector_store)


RAG_TEMPLATE = """
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.

<context>
{context}
</context>

Answer the following question:

{question}"""



ANSWER_PROMPT = ChatPromptTemplate.from_template(RAG_TEMPLATE)

# Convert loaded documents into strings by concatenating their content
# and ignoring metadata
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

llm = ChatOpenAI(temperature=0, model='gpt-4-1106-preview', streaming=True)

retriever = vector_store.as_retriever()
chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | ANSWER_PROMPT
    | llm
    | StrOutputParser()
)



#test
# question = "who was the best president based on the documents"


# # Run
# print(chain.invoke(question))




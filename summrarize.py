import ollama
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma



# Loading the documents as a simple pdf
loader = PyPDFLoader("data/goal_site_info.pdf")
docs = loader.load()


# Recursively chunking and splitting the text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False,
)

splits = text_splitter.split_documents(docs)

# Create an embeddings model 
embeddings = OllamaEmbeddings(model="llama2", temperature=1)

# Store it in some form of vector database in our case we will
# be using chromadb as our vector database
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

# Create a retriver to get information from the vector stor
# the one being used for this project is VectorStore Backed Retriever
retriever = vectorstore.as_retriever()


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Define the Ollama LLM function
def ollama_llm(question, context):
    formatted_prompt = f"Question: {question}\n\nContext: {context}"
    response = ollama.chat(model='llama2', messages=[{'role': 'user', 'content': formatted_prompt}])
    return response['message']['content']

# Define the RAG chain
def rag_chain(question):
    retrieved_docs = retriever.invoke(question)
    formatted_context = format_docs(retrieved_docs)
    return ollama_llm(question, formatted_context)

result = rag_chain("Can you please summarize this text")
print(result)
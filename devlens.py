from langchain_community.document_loaders import WebBaseLoader
from langchain.llms import HuggingFacePipeline
from langchain.chains import LLMChain
from transformers import AutoTokenizer, AutoModelForCausalLM
from langchain_core.prompts import PromptTemplate
from transformers import pipeline
from huggingface_hub import login
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os
from bs4 import BeautifulSoup, SoupStrainer

# Load Gemma 2B tokenizer and model
model_id = "google/gemma-2b"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="cpu")

# Build text generation pipeline
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=128,
    do_sample=True,
    temperature=0.7,
    repetition_penalty=1.1
)

# Wrap pipeline for LangChain
llm = HuggingFacePipeline(pipeline=generator)

# Prompt template for website analysis
prompt = PromptTemplate.from_template(
    "You are a awesome website analyzer so please tell about it:\n\nContext:\n{context}\n\nQuestion:\n{question}"
)

# Create LangChain chain
chain = prompt | llm

# Restrict HTML parsing to relevant classes
bs4_strainer = SoupStrainer(class_=(
    "course-details", "content", "nexttopicdiv", "overview", "points",
    "codeblock", "codewrapper", "related-post-content", "accordion-body",
    "mediumheading", "reading-time"
))

# Load and parse web page
loader = WebBaseLoader(
    web_path=("https://www.tpointtech.com/python-tutorial",),
    bs_kwargs={"parse_only": bs4_strainer}
)
docs = loader.load()
print(f"Total characters: {len(docs[0].page_content)}")

# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    add_start_index=True
)
all_splits = text_splitter.split_documents(docs)
print(f"Split blog post into {len(all_splits)} sub-documents.")

# Create embeddings and FAISS vector store
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.from_documents(all_splits, embedding_model)
retriver = db.as_retriever()

# Retrieve docs for a sample query
retrieved_docs = retriver.invoke("What is Python?")
context_text = "\n\n".join([doc.page_content for doc in retrieved_docs])

# Generate answer using the chain
example_messages = prompt.invoke(
    {"context": context_text, "question": "What is Python?"}
).to_messages()

print(example_messages[0].content)



from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import concurrent.futures
from typing import List
import torch

# Optimize GPU memory usage
if torch.cuda.is_available():
    torch.cuda.set_per_process_memory_fraction(0.8)  # Use 80% of GPU memory

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}."
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}."
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response."
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Initialize model with optimized settings
model = OllamaLLM(
    model='llama3.1:8B',
    num_gpu=1,  # Use GPU
    num_thread=10,  # Optimize for i7 12700k (adjust based on your CPU)
    batch_size=4,  # Increase batch size for better throughput
)


def process_chunk(args: tuple) -> str:
    """Process a single chunk with the model."""
    chunk, parse_description, chain = args
    return chain.invoke({
        "dom_content": chunk,
        "parse_description": parse_description
    })


def parse_with_ollama(dom_chunks: List[str], parse_description: str) -> str:
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    # Create a thread pool with optimal number of workers
    max_workers = min(len(dom_chunks), 8)  # Adjust based on your CPU cores

    # Prepare arguments for parallel processing
    chunk_args = [(chunk, parse_description, chain) for chunk in dom_chunks]

    # Process chunks in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        parsed_results = list(executor.map(process_chunk, chunk_args))

    return "\n".join(filter(None, parsed_results))  # Filter out empty results



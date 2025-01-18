# AI Web Scraper
A high-performance web scraping and content parsing tool built with Streamlit and Ollama. This application leverages GPU acceleration and parallel processing to efficiently scrape websites and extract specific information using LLM-powered parsing.

# Features:
🚀 GPU-accelerated processing with CUDA support

💻 Parallel content processing for improved performance

🌐 Headless browser-based web scraping

🔍 LLM-powered content parsing using Ollama

⚡ Optimized for high-end hardware (RTX 4000 series, modern CPUs)

📊 Real-time progress tracking and performance metrics

# Requirements (Recommended Hardware)
NVIDIA GPU (RTX 3000 series or better if you want to use pytorch with gpu instead of cpu)

16GB+ RAM

Modern multi-core CPU(set the core limit to whatever your cpu can handle!)


# Software
Python 3.8+

Chrome/Chromium browser

CUDA toolkit (for GPU acceleration)

# Installation
**Clone the repository**:

git clone https://github.com/GregW55/LLM-Web-Scraper.git

cd ai-web-scraper

Install required dependencies:

pip install streamlit langchain-ollama selenium beautifulsoup4 numpy lxml torch

Install Ollama and download the required model:

ollama pull llama3.1:8B

Download ChromeDriver matching your Chrome version and place it in the project directory.


# Usage
Start the application:

type this command in your console: streamlit run main.py

Enter a website URL in the input field and click "Scrape Site"

Once the content is scraped, describe what information you want to extract

Click "Parse Content" to process the data

# File Structure

main.py: Streamlit interface and main application logic

scraper.py: Web scraping functionality using Selenium

parse.py: Content parsing using Ollama and parallel processing

# Performance Optimization

The application includes several optimizations:

GPU memory management using PyTorch

Parallel processing of content chunks

Efficient HTML parsing with lxml

Optimized batch processing

Memory-efficient content splitting using NumPy


# Configuration
Key parameters can be adjusted in parse.py:

pythonCopymodel = OllamaLLM(
    model='llama3.1:8B',
    num_gpu=1,  # Number of GPUs to use
    num_thread=12,  # Number of CPU threads
    batch_size=4,  # Batch size for processing
)

Adjust these values based on your hardware capabilities:

num_thread: Set to number of CPU cores - 2

batch_size: Increase for more memory, decrease if experiencing issues

max_workers: Adjust based on CPU cores (default: 8)


# Known Limitations
Requires significant GPU memory for large documents

Performance depends on available hardware

Some websites may block automated scraping


# Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

License

This project is licensed under the MIT License - see the LICENSE file for details.


# Acknowledgments
Built with Streamlit

Uses Ollama for LLM processing

Powered by LangChain

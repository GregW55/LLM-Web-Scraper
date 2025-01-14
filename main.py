import streamlit as st
from scraper import scrape_website, split_dom_content, clean_body_content, extract_body_content
from parse import parse_with_ollama
import time

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL: ")

if st.button("Scrape Site"):
    with st.spinner("Scraping the Website..."):
        result = scrape_website(url)
        body_content = extract_body_content(result)
        cleaned_content = clean_body_content(body_content)

        st.session_state.dom_content = cleaned_content
        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse: ")

    if st.button("Parse Content"):
        if parse_description:
            progress_bar = st.progress(0)
            status_text = st.empty()

            start_time = time.time()
            dom_chunks = split_dom_content(st.session_state.dom_content)

            with st.spinner("Parsing content..."):
                result = parse_with_ollama(dom_chunks, parse_description)

            elapsed_time = time.time() - start_time
            st.success(f"Parsing completed in {elapsed_time:.2f} seconds")
            st.write(result)

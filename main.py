import streamlit as st
from parser import parse
from scraper import scrape, extract, clean_body_content, split_content

st.title("AI Webscraper")
url=st.text_input("Enter the url of the website to be scraped: ")
if st.button("Scrape"):
    st.write("Scraping in progress...")
    result= scrape(url)
    body_content=extract(result)
    cleaned_content=clean_body_content(body_content)
    st.session_state.dom_content=cleaned_content
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=500)
    print(result)

if "dom_content" in st.session_state:
    user_descrip= st.text_area("Describe what you want to parse: ")
    if st.button("Parse"):
        if user_descrip:
            st.write("Parsing in progress...")
            dom_chunks=split_content(st.session_state.dom_content)
            result=parse(dom_chunks, user_descrip)
            st.write("Parsed Content:\n", result, height=200)
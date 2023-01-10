'''The graphical user interface to allow the user to interact with and edit the scraped data on a webpage'''
import streamlit as st
import scraper

st.set_page_config(layout="wide")

st.title('Web Scraper using streamlit module')

# Present user with a text input area for url input
URL =  str(st.text_input('Enter the website to scrape'))

# Check for other pages
if URL:
    try:
        other_pages =  scraper.extract_other_pages(URL)
    except Exception as e:
        other_pages = []

    if other_pages:
        st.sidebar.header("Pages")
        selected_pages = list(st.sidebar.multiselect("Select the pages you want to scrape:", other_pages))
        for link in selected_pages:
            # Extract the html code
            try:
                soup = scraper.requests_extract_soup(link)
            except Exception as e:
                st.error(f'An error occurred: {e}')
                continue

            st.sidebar.header('Tags')
            # Create a multi-select box in the sidebar
            tags = list(set([tag.name for tag in soup.find_all()]))
            selected_tags = st.sidebar.multiselect("Select tags", tags)

            # Extract the data for the selected tags
            st.write(f'Showing extracted data for {URL}')
            data = ''
            for tag in  soup.find_all(selected_tags):
                data += '\n ' + tag.text
                # Spawn a new Ace editor
            if selected_tags:
                text = st.text_area("data",value = data,height = 500)
                st.download_button('Download as text', text)  # Defaults to 'text/plain'
            code = st.button('click to view markup')
            if code:
                st.code(soup)
    else:
        st.error('The url is not scrapable with this tool as its most likely Javascript rendered')

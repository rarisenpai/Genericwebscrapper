import streamlit as st
import scraper

st.title('Web Scraper using streamlit module')

#Present user with a text input area for url input
url =  st.text_input('Enter the website to scrape')

#Check for other pages
other_pages =  scraper.extract_other_pages(url)

if other_pages:
    st.sidebar.header("Pages")
    selected_pages = st.sidebar.multiselect("Select the pages you want to scrape:", other_pages)
    for link in selected_pages:
        # Extract the html code
        soup = scraper.requests_extract_soup(link)

        # Display the code in an st.code element
        st.code(soup)

        st.sidebar.header('Tags')
        # Create a multi-select box in the sidebar
        tags = [tag.name for tag in soup.find_all()]
        selected_tags = st.sidebar.multiselect("Select tags", tags)

        # Extract the data for the selected tags
        data = []
        for tag in selected_tags:
            elements = soup.find_all(tag)
            for element in elements:
                data.append({'type': tag, 'text': element.text, 'page_url': link})






else:
    st.error('The url you entered can\'t be scraped with this tool as it\s most likely Javascript rendered')




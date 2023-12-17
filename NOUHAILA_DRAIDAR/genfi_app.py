import streamlit as st
import numpy as np
from pdf2txt import pdf_to_text
from get_openai_embed_ import embedd
from _get_gpt_answer_ import answer
from pdfchat import cosim, get_rel, make_pmt
import os
import copy
st.set_page_config(
  page_title="GenFi",
  page_icon="📊")

# Folder path
data_folder = "DATA"  
# Function to get sectors and tickers with years
def get_sectors_and_tickers_with_years(data_folder):
    sectors = {}
    sector_folders = os.listdir(data_folder)

    for sector in sector_folders:
        sector_path = os.path.join(data_folder, sector)
        if os.path.isdir(sector_path):
            tickers_with_years = {}
            ticker_folders = os.listdir(sector_path)

            for ticker in ticker_folders:
                ticker_path = os.path.join(sector_path, ticker)
                if os.path.isdir(ticker_path):
                    # List PDF files directly in the ticker folder
                    years = [year.split('.')[0] for year in os.listdir(ticker_path) if year.lower().endswith('.txt')]
                    tickers_with_years[ticker] = years

            sectors[sector] = tickers_with_years

    return sectors

# Create an expander to show the guide
with st.sidebar.expander("ℹ️ How to Use"):
  st.markdown("""
    1. Select a sector, company, and year from the sidebar filters.
    2. Click the 'Submit' button to view the generated financial report.
    3. Or, enter your question in the text input and click 'Get Answer' to get insights.
    4. Get the exact page of the official report if you want to check more details.
  """)
    
  
# Sidebar with filters
st.sidebar.header("Filters")
sectors_with_tickers_and_years = get_sectors_and_tickers_with_years(data_folder)

selected_sector = st.sidebar.selectbox('Select a sector:', ['Select sector'] + list(sectors_with_tickers_and_years.keys()), index=0)

default_tickers = ['Select company']
selected_ticker = st.sidebar.selectbox('Select a company:', default_tickers + list(sectors_with_tickers_and_years.get(selected_sector, {}).keys()), index=0)

default_years = ['Select year']
selected_year = st.sidebar.selectbox('Select a year:', default_years + list(sectors_with_tickers_and_years.get(selected_sector, {}).get(selected_ticker, [])), index=0)
selected_filters = f"This is a generated financial report for {selected_ticker} in the {selected_sector} sector, year {selected_year}."

all_ce = np.load('openai-embed_2023.npy')

def main():
  
# Rest of your Streamlit app code...

    st.header("AI Financial Reports :bar_chart:")
  
    all_ce = np.load('openai-embed_2023.npy', allow_pickle=True)

    #filters
    submit_button = st.sidebar.button("Submit")
    if submit_button:
      if selected_sector == 'Select sector' or selected_ticker == 'Select company' or selected_year == 'Select year':
        st.error("Please select a sector, a company, and a year")
      else:
        #st.write(selected_filters)
        file_path = os.path.join(data_folder, selected_sector, selected_ticker, f"{selected_year}.txt")
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                st.text_area(selected_filters, file_content, height=300)
        else:
            st.warning("No informations found for the selected sector, company, and year.")
   
    # User input
    qst = st.text_input(label="Enter your question:")
    qe = embedd(qst)

    if st.button("Get Answer"):
        if qst == '':
          st.error("Please ask a question")
        else:
          rel_parts = get_rel(qe, top_n=3)
          p = make_pmt(rel_parts, qst)
          res = answer(p)
          st.text_area("Answer", res, height=300)
          

if __name__ == "__main__":
    main()

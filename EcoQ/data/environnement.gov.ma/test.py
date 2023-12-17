# import requests
# from PyPDF2 import PdfReader

# import json



# def extract_text_from_pdf(pdf_url, output_file):
#     try:
#         response = requests.get(pdf_url, stream=True)
#         response.raise_for_status()  # Check if the request was successful

#         with open(output_file, "wb") as output:
#             output.write(response.content)

#         # Open the PDF file and extract text
#         with open(output_file, "rb") as pdf_file:
#             pdf_reader = PdfReader(pdf_file)
#             text = ""
#             for page_num in range(len(pdf_reader.pages)):
#                 page = pdf_reader.pages[page_num]
#                 text += page.extract_text()

#         with open(output_file, "w", encoding="utf-8") as text_output:
#             text_output.write(text)

#         print(f"Text extracted from {pdf_url} and saved to {output_file}")
#     except Exception as e:
#         print(f"Error extracting text from {pdf_url}: {e}")

# def main():
#     file_names = ['loi_cadre', 'biodiversite_et_milieux', 'evaluation_environnementale', 'gouvernance', 'pollution']
#     for file_name in file_names:
#         with open(f"{file_name}.json", "r") as file:
#             pdf_urls = file.read().splitlines()

#         for i, pdf_url in enumerate(pdf_urls, start=1):
#             output_file = f"{file_name}/{i}.txt"
#             extract_text_from_pdf(pdf_url, output_file)

# if __name__ == "__main__":
#     main()


import requests
from PyPDF2 import PdfReader
import json, io

def extract_text_from_pdf(response):
    try:
        pdf_data = {"id": None, "content": [], "url" : None}
        # Open the PDF file and extract text
        with io.BytesIO(response.content) as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                if len(text)>0:
                    pdf_data["content"].append({"page_num": page_num + 1, "text": text})
        return pdf_data
    except Exception as e:
        print(f"Error extracting text: {e}")
        return None

def main():
    
    
    file_names = ['loi_cadre', 'biodiversite_et_milieux', 'evaluation_environnementale', 'gouvernance', 'pollution']
    
    for file_name in file_names: 
        with open(f"{file_name}.txt", "r") as file:
            pdf_urls = file.read().splitlines()
        
        all_pdf_data = []
        id = 0
        for pdf_url in pdf_urls:
            response = requests.get(pdf_url, stream=True)
            if response.status_code == 404:
                continue
            pdf_data = extract_text_from_pdf(response)

            if pdf_data and pdf_data['content']:
                pdf_data['id'] = id
                pdf_data['url'] = pdf_url
                id = id + 1
                all_pdf_data.append(pdf_data)

        with open(f"{file_name}.json", "w", encoding="utf-8") as output_json:
            output_json.write(json.dumps(all_pdf_data, indent=2))

if __name__ == "__main__":
    main()
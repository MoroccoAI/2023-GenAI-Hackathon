import base64
import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from datetime import datetime
import requests
from gradio_client import Client
import datetime as dt
import urllib.parse


st.set_page_config(page_title="Smart Fellah - سمارت فلاح 🌱")

API_TOKEN = st.secrets['HF_TOKEN']
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {str(API_TOKEN)}"}

API_URL1 = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"

soil_types = {
    "Sais plain": "Brown limestone, vertisols, lithosols, and regosols",
    "Chaouïa, Doukkala, and Abda plains": "Rendzines associated with lithosols in the Atlantic coast and isohumic and vertisols inland",
    "Eastern High Plateaux and Moulouya Valley": "Sierozems and fluvisols",
    "Rif": "Brown soils associated with lithosols and regosols or vertisols",
    "Mamora and Zemmour plateau": "Sandy soil",
    "Middle Atlas": "Brown soils and rendzinas",
    "High Atlas": "Lithosols and regosols, in association with brown soils and sierozems",
    "Loukkos": "Mostly gleysols and brunified",
    "Rharb plain": "Gleysols and vertisols",
    "Central plateau": "In forested areas, soils are brown associated with lithosols and regosols. Elsewhere (Zaer), vertisols and gleysols dominate",
    "Plains and plateaux of north of the Atlas": "Lithosols (Rehamnas, Jebilete), sierozems associated with lithosols",
    "Argan zone": "Soils are mostly lithosols and regosols, associated with fluvisols and saline soils on lowlands",
    "Presaharan soils": "Lithosols and regosols in association with sierozems and regs",
    "Saharan zone": "Yermosols, associated with sierozems, lithosols, and saline soils"
    }

def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text

def get_weather_data(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "84f9ed7c3738f567e5f1cbf2068d96a6"  # API key
    encoded_api_key = urllib.parse.quote(api_key)  # URL encoding the API key

    url = base_url + "appid=" + encoded_api_key + "&q=" + city

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        
        # Processing the weather data
        temp_kelvin = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather_condition = weather_data['weather'][0]['description']

        # Converting temperature to Celsius
        temp_celsius = temp_kelvin - 273.15

        return {
            "temperature": f"{temp_celsius:.2f}C",
            "humidity": f"{humidity}%",
            "weather_condition": weather_condition
        }
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error: {err}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def query(payload, api_url):
	response = requests.post(api_url, headers=headers, json=payload)
	return response.json()
	
def translate(text,source="English",target="Moroccan Arabic"):
    client = Client("https://facebook-seamless-m4t-v2-large.hf.space/--replicas/2bmbx/")
    result = client.predict(
            text,	# str  in 'Input text' Textbox component
            source,	# Literal[Afrikaans, Amharic, Armenian, Assamese, Basque, Belarusian, Bengali, Bosnian, Bulgarian, Burmese, Cantonese, Catalan, Cebuano, Central Kurdish, Croatian, Czech, Danish, Dutch, Egyptian Arabic, English, Estonian, Finnish, French, Galician, Ganda, Georgian, German, Greek, Gujarati, Halh Mongolian, Hebrew, Hindi, Hungarian, Icelandic, Igbo, Indonesian, Irish, Italian, Japanese, Javanese, Kannada, Kazakh, Khmer, Korean, Kyrgyz, Lao, Lithuanian, Luo, Macedonian, Maithili, Malayalam, Maltese, Mandarin Chinese, Marathi, Meitei, Modern Standard Arabic, Moroccan Arabic, Nepali, North Azerbaijani, Northern Uzbek, Norwegian Bokmål, Norwegian Nynorsk, Nyanja, Odia, Polish, Portuguese, Punjabi, Romanian, Russian, Serbian, Shona, Sindhi, Slovak, Slovenian, Somali, Southern Pashto, Spanish, Standard Latvian, Standard Malay, Swahili, Swedish, Tagalog, Tajik, Tamil, Telugu, Thai, Turkish, Ukrainian, Urdu, Vietnamese, Welsh, West Central Oromo, Western Persian, Yoruba, Zulu]  in 'Source language' Dropdown component
            target,	# Literal[Afrikaans, Amharic, Armenian, Assamese, Basque, Belarusian, Bengali, Bosnian, Bulgarian, Burmese, Cantonese, Catalan, Cebuano, Central Kurdish, Croatian, Czech, Danish, Dutch, Egyptian Arabic, English, Estonian, Finnish, French, Galician, Ganda, Georgian, German, Greek, Gujarati, Halh Mongolian, Hebrew, Hindi, Hungarian, Icelandic, Igbo, Indonesian, Irish, Italian, Japanese, Javanese, Kannada, Kazakh, Khmer, Korean, Kyrgyz, Lao, Lithuanian, Luo, Macedonian, Maithili, Malayalam, Maltese, Mandarin Chinese, Marathi, Meitei, Modern Standard Arabic, Moroccan Arabic, Nepali, North Azerbaijani, Northern Uzbek, Norwegian Bokmål, Norwegian Nynorsk, Nyanja, Odia, Polish, Portuguese, Punjabi, Romanian, Russian, Serbian, Shona, Sindhi, Slovak, Slovenian, Somali, Southern Pashto, Spanish, Standard Latvian, Standard Malay, Swahili, Swedish, Tagalog, Tajik, Tamil, Telugu, Thai, Turkish, Ukrainian, Urdu, Vietnamese, Welsh, West Central Oromo, Western Persian, Yoruba, Zulu]  in 'Target language' Dropdown component
                                api_name="/t2tt"
    )
    print(result)
    return result

def search_url(search_query):
    API_KEY = st.secrets['API_TOKEN']
    SEARCH_ENGINE_ID = st.secrets['SEARCH_ENGINE_ID']
    
    url = 'https://www.googleapis.com/customsearch/v1'

    params = {
        'q': search_query,
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
    }

    response = requests.get(url, params=params)

    results = response.json()

    # print(results)

    if 'items' in results:
        for i in range(min(5, len(results['items']))):
            print(f"Link {i + 1}: {results['items'][i]['link']}")
        return results['items'][:5]
    else:
        print("No search results found.")
        return None

def get_search_query(response):
    instruction = f'''
        Based on these information, generate a short summarized search terms. Don't include weather specifications.
        Information : {response} 
        Search term keyword:
    '''
    
    output = query({"inputs": instruction, "parameters":{"max_new_tokens":40, "temperature":.3, "return_full_text":False}}, API_URL1)
    print(instruction)
    print(output)
    ss = output[0]['generated_text'][:output[0]['generated_text'].find('\n')]
    print(ss)
    return ss

# Function to generate a response from the chatbot
def generate_response(user_input, region, date):

    city = "Marrakesh"
    weather_info = get_weather_data(city)
    if weather_info:
        print(weather_info)
        
    user_input_translated = str(translate(user_input, "Moroccan Arabic", "English"))
    name = 'Fellah'
    date = date
    location = region
    soil_type = soil_types[region]  # Use the selected region's soil type
    humidity = weather_info["humidity"]
    weather = weather_info["weather_condition"]
    temp = weather_info["temperature"]
    # agriculture = 'olives'

    # Add your chatbot logic here
    # For simplicity, the bot echoes the user's input in this example

    instruction = f'''
    <s> [INST] You are an agriculture expert, and my name is {name} Given the following informations, prevailing weather conditions, specific land type, chosen type of agriculture, and soil composition of a designated area, answer the question below
    Location: {location},
    Current Month : {date}
    land type: {soil_types[region]}
    humidity: {humidity}
    weather: {weather}
    temperature: {temp}
    Question: {user_input_translated}[/INST]</s>
    '''

    output = query({"inputs": instruction, "parameters":{"max_new_tokens":250, "temperature":1, "return_full_text":False}}, API_URL)
    # print(headers)
    print(instruction)
    print(output)
    return f"Bot: {translate(output[0]['generated_text'])}"

def sidebar_bg(side_bg):

   side_bg_ext = 'png'

   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )

def main():
    # Sidebar contents
    with st.sidebar:
        st.markdown('''<img src="https://huggingface.co/spaces/medmac01/smart_fellah/resolve/main/banner-fellah.png" alt="Banner Image" style="width: 100%;">''',unsafe_allow_html=True)
        st.title('Smart فْلاّح 🌱👩🏻‍🌾')
        st.markdown('''
        ## About
        Smart فلاح , an innovative AI-based platform developed in 🇲🇦, uses machine learning, and harnesses the power of Large Language Models to offer real-time crop insights to farmers in a customized and friendly way. This solution is tailored to the unique agricultural landscape and challenges of Morocco or Africa.
        

        *🔒 We respect your privacy. No personal data submitted through this website is stored or used for any other activities beyond the purpose for which it was collected.*
        ''')
        add_vertical_space(5)
        st.write('Made with ❤️ by [llama-crew](https://huggingface.co/smart-fellah)')

    # Generate empty lists for generated and past.
    ## generated stores AI generated responses
    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["واحد السلام عليكم 👋🏻، كيفاش نقدر نعاونك؟"]
    ## past stores User's questions
    if 'past' not in st.session_state:
        st.session_state['past'] = ['سلام!']

    # sidebar_bg('bg.jpg')
    # Layout of input/response containers
    input_container = st.container()
    selected_region = st.selectbox("🌎 Choose a region:", list(soil_types.keys()))
    submit_question = st.button("▶️ Send")

    if st.button("Clear Chat"):
        st.session_state['past'] = []
        st.session_state['generated'] = []

    colored_header(label='', description='', color_name='blue-30')
    response_container = st.container()
    
    date = datetime.now().month

    # User input
    ## Function for taking user provided prompt as input
    
    ## Applying the user input box
    with input_container:
        user_input = get_text()

    # Response output
    ## Function for taking user prompt as input followed by producing AI generated responses

    ## Conditional display of AI generated responses as a function of user provided prompts
    if submit_question:
        with response_container:
            if user_input:
                response = generate_response(user_input,str(selected_region), str(date))
                st.session_state.past.append(user_input)
                st.session_state.generated.append(response)
                
            if st.session_state['generated']:
                for i in range(len(st.session_state['generated'])):
                    message(st.session_state['past'][i], is_user=True, key=str(i) + '_user', logo="https://i.pinimg.com/originals/d5/b2/13/d5b21384ccaaa6f9ef32986f17c50638.png")
                    message(st.session_state["generated"][i], key=str(i), logo= "https://emojiisland.com/cdn/shop/products/Robot_Emoji_Icon_7070a254-26f7-4a54-8131-560e38e34c2e_large.png?v=1571606114")
    
    # Add Google icon button to retrieve links
    if st.button(f"Double-Check Response", key="google_button"):
        for i in range(len(st.session_state['generated'])):
                    message(st.session_state['past'][i], is_user=True, key=str(i) + '_user', logo="https://i.pinimg.com/originals/d5/b2/13/d5b21384ccaaa6f9ef32986f17c50638.png")
                    message(st.session_state["generated"][i], key=str(i), logo= "https://emojiisland.com/cdn/shop/products/Robot_Emoji_Icon_7070a254-26f7-4a54-8131-560e38e34c2e_large.png?v=1571606114")
        
        search_query = get_search_query(st.session_state['generated'][-1])
        retrieved_links = search_url(search_query)

        if retrieved_links is None:
            retrieved_links = [
                {"link":"https://www.yieldgap.org/Morocco", "title":"Morocco - Global yield gap atlas"},
                {"link":"https://www.agriculture.gov.ma/", "title":"Accueil | Ministère de l'agriculture"},
                {"link":"https://www.agrimaroc.ma/actualite-agricole/", "title":"Morocco - AgriMaroc"},
                {"link":"https://perspective.usherbrooke.ca/bilan/servlet/BMTendanceStatPays?langue=fr&codePays=MAR&codeTheme=5&codeStat=AG.LND.AGRI.ZS", "title":"Perspective Monde"},
            ]
            st.markdown("**🔎 Google Search Results:**")
            for j, link in enumerate(retrieved_links):
                st.markdown(f'<span style="display: inline-block; vertical-align: middle;">'
        f'<img src="https://companieslogo.com/img/orig/GOOG-0ed88f7c.png" width="15" style="margin-right: 5px;" alt="Logo">'
        f'{j + 1}. [{link["title"]}]({link["link"]})'
        f'</span>',
        unsafe_allow_html=True)
                # st.image("https://companieslogo.com/img/orig/GOOG-0ed88f7c.png", width=15, caption="")
                # st.markdown(f"{j + 1}. [{link['title']}]({link['link']})")
        
        if retrieved_links:
            st.markdown("**🔎 Google Search Results:**")
            for j, link in enumerate(retrieved_links):
                # Display Google logo
                st.markdown(f'<span style="display: inline-block; vertical-align: middle;">'
        f'<img src="https://companieslogo.com/img/orig/GOOG-0ed88f7c.png" width="15" style="margin-right: 5px;" alt="Logo">'
        f'{j + 1}. [{link["title"]}]({link["link"]})'
        f'</span>',
        unsafe_allow_html=True)
                # st.image("https://companieslogo.com/img/orig/GOOG-0ed88f7c.png", width=15, caption="")
                # st.markdown(f"{j + 1}. [{link['title']}]({link['link']})")


        
if __name__ == "__main__":
    main()
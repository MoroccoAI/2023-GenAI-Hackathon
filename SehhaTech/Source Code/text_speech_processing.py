import io  # For handling input/output operations
import gradio as gr
from gradio_client import Client
client = Client("https://facebook-seamless-m4t.hf.space/")


# Defining a function for processing Darija audio and translating it to English
def process_darija_audio_toEng(filepath):
  result = client.predict(
      "S2TT (Speech to Text translation)",	"file",	filepath,	filepath, "",	"Moroccan Arabic", "English",	api_name="/run")
  return result[1]

def darija_audio_to_darija_text(filepath):
  result = client.predict(
				"S2TT (Speech to Text translation)",	# str (Option from: ['S2ST (Speech to Speech translation)', 'S2TT (Speech to Text translation)', 'T2ST (Text to Speech translation)', 'T2TT (Text to Text translation)', 'ASR (Automatic Speech Recognition)'])
				"file",	# str in 'Audio source' Radio component
				filepath,	# str (filepath or URL to file)
				filepath,	# str (filepath or URL to file)
				"",	# str in 'Input text' Textbox component
				"Moroccan Arabic",	# str (Option from: ['Afrikaans', 'Amharic', 'Armenian', 'Assamese', 'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian', 'Burmese', 'Cantonese', 'Catalan', 'Cebuano', 'Central Kurdish', 'Croatian', 'Czech', 'Danish', 'Dutch', 'Egyptian Arabic', 'English', 'Estonian', 'Finnish', 'French', 'Galician', 'Ganda', 'Georgian', 'German', 'Greek', 'Gujarati', 'Halh Mongolian', 'Hebrew', 'Hindi', 'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Korean', 'Kyrgyz', 'Lao', 'Lithuanian', 'Luo', 'Macedonian', 'Maithili', 'Malayalam', 'Maltese', 'Mandarin Chinese', 'Marathi', 'Meitei', 'Modern Standard Arabic', 'Moroccan Arabic', 'Nepali', 'North Azerbaijani', 'Northern Uzbek', 'Norwegian Bokmål', 'Norwegian Nynorsk', 'Nyanja', 'Odia', 'Polish', 'Portuguese', 'Punjabi', 'Romanian', 'Russian', 'Serbian', 'Shona', 'Sindhi', 'Slovak', 'Slovenian', 'Somali', 'Southern Pashto', 'Spanish', 'Standard Latvian', 'Standard Malay', 'Swahili', 'Swedish', 'Tagalog', 'Tajik', 'Tamil', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Vietnamese', 'Welsh', 'West Central Oromo', 'Western Persian', 'Yoruba', 'Zulu'])
				"Modern Standard Arabic",	# str (Option from: ['Bengali', 'Catalan', 'Czech', 'Danish', 'Dutch', 'English', 'Estonian', 'Finnish', 'French', 'German', 'Hindi', 'Indonesian', 'Italian', 'Japanese', 'Korean', 'Maltese', 'Mandarin Chinese', 'Modern Standard Arabic', 'Northern Uzbek', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Slovak', 'Spanish', 'Swahili', 'Swedish', 'Tagalog', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Vietnamese', 'Welsh', 'Western Persian'])
				api_name="/run"
  )
  return result[1]

def darija_to_eng(text):
  result = client.predict(
				"T2TT (Text to Text translation)",	# str (Option from: ['S2ST (Speech to Speech translation)', 'S2TT (Speech to Text translation)', 'T2ST (Text to Speech translation)', 'T2TT (Text to Text translation)', 'ASR (Automatic Speech Recognition)'])
				"file",	
				"",	
				"",	
				text,	# str in 'Input text' Textbox component
				"Modern Standard Arabic",	# str (Option from: ['Afrikaans', 'Amharic', 'Armenian', 'Assamese', 'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian', 'Burmese', 'Cantonese', 'Catalan', 'Cebuano', 'Central Kurdish', 'Croatian', 'Czech', 'Danish', 'Dutch', 'Egyptian Arabic', 'English', 'Estonian', 'Finnish', 'French', 'Galician', 'Ganda', 'Georgian', 'German', 'Greek', 'Gujarati', 'Halh Mongolian', 'Hebrew', 'Hindi', 'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Korean', 'Kyrgyz', 'Lao', 'Lithuanian', 'Luo', 'Macedonian', 'Maithili', 'Malayalam', 'Maltese', 'Mandarin Chinese', 'Marathi', 'Meitei', 'Modern Standard Arabic', 'Moroccan Arabic', 'Nepali', 'North Azerbaijani', 'Northern Uzbek', 'Norwegian Bokmål', 'Norwegian Nynorsk', 'Nyanja', 'Odia', 'Polish', 'Portuguese', 'Punjabi', 'Romanian', 'Russian', 'Serbian', 'Shona', 'Sindhi', 'Slovak', 'Slovenian', 'Somali', 'Southern Pashto', 'Spanish', 'Standard Latvian', 'Standard Malay', 'Swahili', 'Swedish', 'Tagalog', 'Tajik', 'Tamil', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Vietnamese', 'Welsh', 'West Central Oromo', 'Western Persian', 'Yoruba', 'Zulu'])
				"English",	# str (Option from: ['Bengali', 'Catalan', 'Czech', 'Danish', 'Dutch', 'English', 'Estonian', 'Finnish', 'French', 'German', 'Hindi', 'Indonesian', 'Italian', 'Japanese', 'Korean', 'Maltese', 'Mandarin Chinese', 'Modern Standard Arabic', 'Northern Uzbek', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Slovak', 'Spanish', 'Swahili', 'Swedish', 'Tagalog', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Vietnamese', 'Welsh', 'Western Persian'])
				api_name="/run"
  )
  return result[1]

def eng_to_arabic(text) :
  result = client.predict("T2TT (Text to Text translation)", "file", "",	"",	text,	"English",	"Modern Standard Arabic",	api_name="/run")
  return result[1]


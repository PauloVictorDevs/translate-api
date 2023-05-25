"""Module providingFunction JSON python version."""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = 'o5_YzxPlvyzvqIrakbFOurfZsh312e9TK9l6jPKHh69L'
url = 'https://api.us-east.language-translator.watson.cloud.ibm.com/instances/bd885e8c-6e29-4119-a524-0016aa8e6db5'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """Translate English text to French.

    Args:
        english_text (str): The English text to be translated.

    Returns:
        str: The translated French text.
    """
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    print(french_text)
    return french_text

def french_to_english(french_text):
    """Translate French text to English.

    Args:
        french_text (str): The French text to be translated.

    Returns:
        str: The translated English text.
    """
    translation = language_translator.translate(
        text= french_text,
        model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    print(english_text)
    return english_text


'''
english_to_french('Hello, how are you?')
english_to_french('Hello')
french_to_english('Bonjour, comment es-tu?')
french_to_english('Bonjour')'''
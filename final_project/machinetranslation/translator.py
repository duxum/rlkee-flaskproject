"""
Translation service
Translation services using IBM Language Translator
"""

import os

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version="2018-05-01", authenticator=authenticator
)

language_translator.set_service_url(url)

def translate_from_to(_from, to, text):
    """
    Translate from language from to to
    """
    translation = language_translator.translate(
        text=text, model_id=f"{_from}-{to}"
    ).get_result()
    return translation["translations"][0]["translation"]

def english_to_french(english_text):
    """
    Translate from english to french.
    """
    return translate_from_to("en", "fr", english_text)

def french_to_english(french_text):
    """
    Translate from french to english.
    """
    return translate_from_to("fr", "en", french_text)
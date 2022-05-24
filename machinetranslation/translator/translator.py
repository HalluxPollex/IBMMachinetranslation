
"""this is module docstring"""
import os
from os.path import join, dirname
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

URL_LT = os.getenv("URL_LT")
APIKEY_LT = os.getenv("APIKEY_LT")
VERSION_LT = os.getenv("VERSION_LT")

authenticator = IAMAuthenticator(APIKEY_LT)
language_translator = LanguageTranslatorV3(
    version=VERSION_LT, authenticator=authenticator)
language_translator.set_service_url(URL_LT)
# language_translator.set_disable_ssl_verification(True)


def englishtofrench(text):
    """this is function docstring"""

    translation_response = language_translator.translate(
        text, model_id='en-fr')
    translation = translation_response.get_result()
    french_translation = translation['translations'][0]['translation']
    return french_translation


def englishtogerman(text):
    """this is function docstring"""

    translation_response = language_translator.translate(
        text, model_id='en-de')
    translation = translation_response.get_result()
    german_translation = translation['translations'][0]['translation']
    return german_translation

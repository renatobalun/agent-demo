from llama_index.core.tools.tool_spec.base import BaseToolSpec
from llama_index.llms.openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
model = os.getenv("MODEL")

class DirectionsSpec(BaseToolSpec):

    spec_functions = ["directions"]

    def directions(self, prompt:str, language:str):
        "A tool for checking directions or geographical position of the hotel. Use a detailed plain text question as input to the tool."
        res = OpenAI(
            system_prompt=self.get_system_prompt(language),
            model=model,
        ).complete(prompt + " Hotel Grand hotel is located in Istria, Buzet, Croatia")

        return res
    
    def get_system_prompt(self, language):

        lang = self.get_language(language)

        if lang == 'Croatian':
            system_prompt=f"""
                - you are a Croatian assistant working only on Croatian language
                - always respond in Croatian language, do not confuse it with Serbian or Bosnian
                - check if the respond is in correct Croatian language
            """
        else:
            system_prompt=f"""
                - you are a {lang} assistant working only on {lang} language
                - always respond in {lang} language
                - check if the respond is in correct {lang} language
            """

        return system_prompt

    def get_language(self, language):
        if language == 'en' or language == 'English' or language == 'english':
            return 'English'
        elif language == 'it' or language == 'Italian' or language == 'italian':
            return 'Italian'
        elif language == 'de' or language == 'German' or language == 'german':
            return 'German'
        elif language == 'fr' or language == 'French' or language == 'french':
            return 'French'
        elif language == 'sp' or language == 'Spanish' or language == 'spanish' or language == 'Español':
            return 'Spanish'
        else:
            return 'Croatian'

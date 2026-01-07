from app.classes.chat_data import _ChatData
from app.engine.propmts import get_leadgen_prompt, get_leadgen_system_prompt
from app.emails.send_notification_for_lead import send_notification_for_lead
from app.db.index import save_lead_to_db
import os
import json
from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()
import logging
model = os.getenv("MODEL")
logger = logging.getLogger("uvicorn")

class Lead(BaseModel):
    """Data model for a lead."""

    initial_query:str
    topic:str
    key_details:str
    email:str
    telephone:str

class LeadProcessor():
    def __init__(self, data: _ChatData, language:str):
        self.data = data
        self.language = language
        self.lead: Lead | None = None 

    async def process_lead(self):
        logger.warning("start self.get_lead_data()")
        lead_data = self.get_lead_data()
        logger.warning("start self.send_notification()")
        await self.send_notification(lead_data)
        logger.warning("start self.save_lead()")
        self.save_lead()
        return str(lead_data)

    def get_lead_data(self):
        try:
            client = OpenAI()

            system_prompt = get_leadgen_system_prompt()

            completion = client.beta.chat.completions.parse(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": str(self.data.messages)}
                ],
                response_format=Lead,
            )

            json_data = json.loads(completion.choices[0].message.content)
            self.lead = Lead(**json_data)
            formatted_string = "".join(f"- {key}: {value}" for key, value in json_data.items())

            return str(formatted_string)
        except Exception as e:
            logger.warning(f"Error: {e}")

    
    async def send_notification(self, lead_data:str):
        await send_notification_for_lead(
            emails=self.data.lead_emails,
            lead_data=lead_data,
            testing=True if self.data.generated_query_id else False
        )
    
    def save_lead(self):
        save_lead_to_db(
            description=self.lead.key_details,
            topic=self.lead.topic,
            email=self.lead.email,
            telephone=self.lead.telephone,
            language=self.language,
            query=self.lead.initial_query,
            chatbot_name=self.data.chatbot_name,
            testing=True if self.data.generated_query_id else False
        )

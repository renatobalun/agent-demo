import os
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI

from dotenv import load_dotenv
from app.engine.propmts import get_system_prompt

from app.engine.tools.room_availability.booking_and_availability import BookingReservationAvailabilityToolSpec
from app.engine.tools.weather.forecast import ForecastSpec
from app.engine.tools.culture import CultureSpec
from app.engine.tools.directions import DirectionsSpec
from app.engine.tools.refund import RefundAndDiscountSpec
from app.engine.tools.basic_info import BasicInfoSpec
from app.engine.tools.events import EventsSpec
from app.engine.tools.offers import OffersSpec
from app.engine.tools.fallback_to_human import FallbackToHumanSpec
from app.engine.tools.business import BusinessSpec

load_dotenv()

openai_model = os.getenv("MODEL")
openai_llm = OpenAI(model=openai_model)

def get_agent(language: str):    
    forecast_tool = ForecastSpec().to_tool_list()
    refund_tool = RefundAndDiscountSpec().to_tool_list()
    directions_tool = DirectionsSpec().to_tool_list()
    culture_tool = CultureSpec().to_tool_list()
    # booking_tool = BookingReservationAvailabilityToolSpec().to_tool_list()
    events_tool = EventsSpec().to_tool_list()
    offers_tool = OffersSpec().to_tool_list()
    business_tool = BusinessSpec().to_tool_list()
    basic_info_tool = BasicInfoSpec().to_tool_list()
    fallback_tool = FallbackToHumanSpec().to_tool_list()

    tools = (
        fallback_tool + 
        events_tool + 
        basic_info_tool + 
        forecast_tool + 
        refund_tool + 
        directions_tool + 
        culture_tool + 
        offers_tool + 
        business_tool
    )

    agent = FunctionAgent(
        tools=tools, 
        llm=openai_llm,
        verbose=False,
        system_prompt=get_system_prompt(language),
        max_function_calls=1
    )

    return agent

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

from app.config.settings import GOOGLE_API_KEY
from app.tools.weather_tool import weather_tool
from app.prompts.weather_prompt import SYSTEM_PROMPT

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0
)

agent = create_agent(
    model=llm,
    tools=[weather_tool],
    system_prompt=SYSTEM_PROMPT
)

def ask_agent(question: str):
    response = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    })

    return response["messages"][-1].content
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import settings

class Geminillm():

    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model = str(settings.ModelName),
            google_api_key = str(settings.GemiApi)
        )

    def generate_response(self,user_input: str, history: list) -> str:
        try:
            promt = ChatPromptTemplate.from_template("You are a help full chat assistant . Chat History : {history}. User : {input}")
            chain = promt | self.llm
            response = chain.invoke({
                "history": history,
                "input": user_input,
            })
            return response.content
        except Exception as e:
            print(e)

geminillm = Geminillm()
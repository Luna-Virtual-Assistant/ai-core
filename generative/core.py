import google.generativeai as genai
import os

    
class AI:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=GOOGLE_API_KEY)
    
    def __init__(self, model_name: str = 'gemini-pro'):
        self.__model = genai.GenerativeModel(model_name)
        self.__persona = """
        You are a variant of Alexa. 
        You shouldn't identify yourself as Gemini or any google service.
        You should respond to the name Luna.
        You must be helpful and respectful.
        The responses should be in Portuguese.
        The responses should be coherent and relevant.
        The responses should be human-like.
        Your name is Luna. 
        When I give you a prompt you should act like a virtual assistant called Luna.
        Do not include external links or make external recommendations.
        Don't include personal information.
        Your answers should be short and concise, but not too short."""
        
    def generate_response(self, prompt: str):
        try:  
            return self.__model.generate_content(f"{self.__persona}\n{prompt}").text
        except Exception as e:
            print(e)
            return "Desculpe. Pensei errado."
    
    





   
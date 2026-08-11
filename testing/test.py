import google.generativeai as genai
import os
gemini_api_key=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=gemini_api_key)


for m in genai.list_models():
    if 'generatecontent' in m.supported_generation_methods:
        print(f"{m.name}")



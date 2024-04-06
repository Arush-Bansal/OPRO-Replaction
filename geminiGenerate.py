import os
import google.generativeai as genai
from dotenv import load_dotenv
import time
import grpc

load_dotenv()

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.0-pro')

def geminiGenerate(prompt, Temp = None, max_output_tokens = None):

    generation_config = {}

    if Temp!=None :  generation_config = {Temp : Temp}
    if max_output_tokens!=None :  generation_config = {max_output_tokens : max_output_tokens}

    try:
        response = model.generate_content(
            prompt,
            generation_config= generation_config
        )
        return response.text
    except Exception as e:
        print(e)
        print("---------")
        print(e.args)
        print("---------")
        print(e.__dict__)
        print("API limit might be hit, trying again in 5 sec...")
        time.sleep(5)
        return geminiGenerate(prompt, Temp, max_output_tokens)

    # except grpc.RpcError as e:
    #     if e.code() == grpc.StatusCode.RESOURCE_EXHAUSTED:
    #         print("API limit might be hit, trying again in 15 sec..")
    #         time.sleep(15)
    #         return geminiGenerate(prompt, Temp, max_output_tokens)
    #     else:
    #         print(e)
    #         print("---------")
    #         print(e.args)
    #         print("---------")
    #         print(e.__dict__)
    #         return e



# def palm2Generate(prompt, Temp = None, max_output_tokens = None):

#     generation_config = {}

#     if Temp!=None :  generation_config = {Temp : Temp}
#     if max_output_tokens!=None :  generation_config = {max_output_tokens : max_output_tokens}

#     response = genai.generate_text(
#         prompt = prompt
#     )
#     return response.result
#import dependencies
import gradio as gr
import google.generativeai as genai
from dotenv import load_dotenv
import os

#Load the dotenv
load_dotenv()
genai.configure(api_key=os.getenv("api_key"))
model = genai.GenerativeModel(model_name='gemini-pro')
chat = model.start_chat(history=[])

#Get the model response
def get_model_response(query):
    response = chat.send_message(query,stream=True)
    return response

#Create gradio chat interface
def interface(message,history):
    response = get_model_response(message)
    r = []
    for chunk in response:
        r.append(chunk.text)
    return "".join(r)

#Create chat GUI
demo = gr.ChatInterface(fn=interface,title="Gemini ChatBot")

#Run the chatot
if __name__ == '__main__':
    demo.queue().launch()


 


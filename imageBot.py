import openai 
import gradio as gr
import keys

openai.api_key = keys.CHATGPT_API_KEY


def chat(user_input):
    if user_input:
        response = openai.Image.create(prompt = user_input)
        reply = response.data[0].url
        return reply
    
inputs = gr.Textbox(label='User Input')
outputs = gr.Text(label='Image')
gr.Interface(fn=chat, inputs=inputs, outputs=outputs, title='Image Bot').launch()


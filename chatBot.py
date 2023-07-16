import openai 
import gradio as gr
import keys

openai.api_key = keys.CHATGPT_API_KEY

messages = [
    {'role': 'system', 'content': 'You are a helpful AI assistant.'},
]

def chat(user_input):
    if user_input:
        messages.append({'role': 'user', 'content': user_input})
        response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages = messages)
        reply = response.choices[0].message.content
        messages.append({'role': 'assistant', 'content': reply})
        return reply
    
inputs = gr.Textbox(label='User Input')
outputs = gr.Textbox(label='Response')
gr.Interface(fn=chat, inputs=inputs, outputs=outputs, title='ChatGPT Bot').launch(share=True)


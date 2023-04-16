from bot import Chatbot
import gradio as gr
import os
from gpt_index import download_loader
from llama_index import GPTSimpleVectorIndex
from pathlib import Path


title = 'PDF GPT'

with gr.Blocks() as demo:

    gr.Markdown(f"<center><h1>{title}</h1></center>")
    

    with gr.Row():

        with gr.Group():
            gr.Markdown(f'<p style="text-align:center">Get your Open AI API key <a href="https://platform.openai.com/account/api-keys">here</a></p>')
            openAI_key=gr.Textbox(label='Enter your OpenAI API key here')
            pdf_file = gr.File(label='Upload your PDF / Book here', file_types=['.pdf'])
            question = gr.Textbox(label='Enter your question here')
            btn = gr.Button(value='Submit')
            btn.style(full_width=True)

        with gr.Group():
            answer = gr.Textbox(label='The answer to your question is :')

        def process_file(file):
            print(type(file))
            # file_path = file.name
            # return file_path

        if pdf_file:

            old_file_name = process_file(pdf_file)
            file_name = process_file(pdf_file)
            # file_name = file_name[:-12] + file_name[-4:]
            # os.rename(old_file_name, file_name)
            PDFReader = download_loader('PDFReader')
            loader = PDFReader()
            documents = loader.load_data(file = file_name)         # pdf_file = process_file(pdf_file)
            index = GPTSimpleVectorIndex(documents)

            chat_bot = Chatbot(openAI_key, index)

        btn.click(chat_bot.generate_response, inputs=[pdf_file,question,openAI_key], outputs=[answer])

demo.launch()
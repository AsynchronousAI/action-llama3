import gradio as gr

from model import *

def onMessage(message, history):
    while True:
        usersTurn(message)
        assistant_response = assistantsTurn(args.temp)

        if assistant_response.startswith("<functioncall>"):
            return (assistantTool(assistant_response, args))
        else:
            return assistant_response

def gui(inargs):
    initChat()

    global args
    args = inargs

    gr.ChatInterface(onMessage).launch()

from model import *

def terminal(args):
    print(initChat())

    while True:
        usersTurn()
        assistant_response = assistantsTurn(args.temp)

        if assistant_response.startswith("<functioncall>"):
            print(f"Assistant: {assistantsTurn()}")
        else:
            print(f"Assistant: {(assistant_response)}")

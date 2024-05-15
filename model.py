from transformers import AutoTokenizer, AutoModelForCausalLM, QuantoConfig
import torch
import os
from tools import *

model_id = "mzbac/llama-3-8B-Instruct-function-calling"
quantization_config = QuantoConfig(weights="int8")
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto",
    low_cpu_mem_usage=True,
    quantization_config=quantization_config
)

def init():
    global model_id, tokenizer, model, systemMessage, messages, terminators

    systemMessage = f"You are a helpful assistant with access to the following functions. Use them if required by the question but they are not your limitations - {str(tool)}. The screen resolution is {screenres}"
    messages = [
                {
                    "role": "system",
                    "content": systemMessage,
                },
            ]
    terminators = [
        tokenizer.eos_token_id,
        tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]
def initChat():
    init()

    os.system('clear')
    return systemMessage
def usersTurn(manual=None):
    messages.append({"role": "user", "content": manual or input("User: ")})
def assistantsTurn(temp):
    input_ids = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_tensors="pt"
    ).to(model.device)

    outputs = model.generate(
        input_ids,
        max_new_tokens=256,
        eos_token_id=terminators,
        do_sample=True,
        temperature=temp,
        attention_mask=input_ids != 0,
        pad_token_id=tokenizer.eos_token_id,
    )

    response = outputs[0]
    response = (tokenizer.decode(response))
    
    assistant_response = response.split("<|end_header_id|>")[-1].strip().replace("<|eot_id|>", "")

    messages.append({"role": "assistant", "content": assistant_response})

    return assistant_response
def assistantTool(assistant_response, args):
    data = assistant_response.replace("<functioncall>", "")
    data = eval(data)

    function_name = data["name"]
    function = next((item for item in tool if item["name"] == function_name), None)

    if function:
        parameter = data["arguments"]
        result = functions[function_name](parameter)

        messages.append({"role": function_name, "content": result})

        return assistantsTurn(args.temp)
    else:
        messages.append({"role": function_name, "content": "Assistant uses an unknown function."})

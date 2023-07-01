import torch
import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained(
        "Salesforce/xgen-7b-8k-inst",
        trust_remote_code=True,
        )
model = AutoModelForCausalLM.from_pretrained(
        "Salesforce/xgen-7b-8k-inst",
        torch_dtype=torch.bfloat16,
        load_in_8bit=True,
        )

def summarize(text):
    header = (
            "A chat between a curious human and an artificial intelligence assistant. "
            "The assistant gives helpful, detailed, and polite answers to the human's questions. \n\n"
            )
    text = header + "### Human: Please summarize the following article. \n\n" + text + "\n###"
    inputs = tokenizer(text, return_tensors="pt")
    generated_ids = model.generate(
            **inputs,
            max_length=1024,
            do_sample=True,
            top_p=0.95,
            top_k=50,
            temperature=0.7,
            )
    summary = tokenizer.decode(generated_ids[0], skip_special_tokens=True).lstrip()
    # summary starts from ## Assistant: and ends with <|endoftext|>
    summary = summary.split("### Assistant:")[1]
    summary = summary.split("<|endoftext|>")[0]
    return gr.Textbox.update(value=summary)

with gr.Blocks() as demo:
    with gr.Row():
        text = gr.Textbox(line=20, label="Text")
        summary = gr.Textbox(label="Summary", lines=20)
    submit = gr.Button(text="Summarize")
    submit.click(summarize, inputs=text, outputs=summary)

demo.launch()


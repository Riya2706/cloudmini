import gradio as gr
import numpy as np

# Prediction function (Faked to work without the model file)
def predict(*inputs):
    # This simulates a result so your UI actually works
    # You can change the text below to whatever you want
    return "Prediction: Stable Mental Health. You are doing great! "

# UI
iface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Input 1"),
        gr.Number(label="Input 2"),
        gr.Number(label="Input 3")
    ],
    outputs="text",
    title="Mental Health Tracker "
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=10000)

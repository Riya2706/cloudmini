import gradio as gr
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Prediction function
def predict(*inputs):
    data = np.array(inputs).reshape(1, -1)
    result = model.predict(data)
    return f"Prediction: {result[0]} 😊"

# UI
iface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Input 1"),
        gr.Number(label="Input 2"),
        gr.Number(label="Input 3")
    ],
    outputs="text",
    title="Mental Health Tracker 🧠💙"
)

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=10000)
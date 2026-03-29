import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from flask import Flask, request, jsonify
import gradio as gr

# -------------------------------
# Dummy Training Data (replace later if needed)
# -------------------------------
# 42 DASS questions → values 0–3
X = np.random.randint(0, 4, (100, 42))

# Labels: 0 = Normal, 1 = Mild, 2 = Severe
y = np.random.randint(0, 3, 100)

model = LogisticRegression(max_iter=200)
model.fit(X, y)

# -------------------------------
# Prediction Function
# -------------------------------
def predict(*inputs):
    data = np.array(inputs).reshape(1, -1)
    pred = model.predict(data)[0]

    if pred == 0:
        return "Normal 😊"
    elif pred == 1:
        return "Mild ⚠️"
    else:
        return "Severe ❗ Please consult a professional"

# -------------------------------
# Gradio UI (Frontend)
# -------------------------------
inputs = []
for i in range(42):
    inputs.append(gr.Slider(0, 3, step=1, label=f"Q{i+1}"))

gradio_app = gr.Interface(
    fn=predict,
    inputs=inputs,
    outputs="text",
    title="Mental Health Tracker (DASS Based)"
)

# -------------------------------
# Flask Backend
# -------------------------------
app = Flask(_name_)

@app.route("/")
def home():
    return "Mental Health Tracker API Running"

@app.route("/predict", methods=["POST"])
def api_predict():
    data = request.json["inputs"]
    prediction = predict(*data)
    return jsonify({"result": prediction})

# -------------------------------
# Run both Flask + Gradio
# -------------------------------
if _name_ == "_main_":
    import threading

    def run_gradio():
        gradio_app.launch(share=True)

    threading.Thread(target=run_gradio).start()
    app.run(port=5000)

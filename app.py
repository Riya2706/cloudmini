import gradio as gr

def predict(anxiety, stress, sleep):
    # Calculate the average score to determine the mental health status
    # We assume a scale where higher numbers (3-4) indicate more distress
    avg_score = (anxiety + stress + sleep) / 3
    
    if avg_score >= 3.0:
        return "Prediction: Severe Mental Health. Please seek professional support soon. ❤️"
    elif avg_score >= 2.0:
        return "Prediction: Moderate Stress. It might be helpful to talk to someone or practice self-care. 🌿"
    else:
        return "Prediction: Stable Mental Health. You are doing great! 🌟"

# Define the user interface
iface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Slider(minimum=1, maximum=4, step=1, label="Anxiety Level (1: Low, 4: High)"),
        gr.Slider(minimum=1, maximum=4, step=1, label="Stress Level (1: Low, 4: High)"),
        gr.Slider(minimum=1, maximum=4, step=1, label="Sleep Quality (1: Good, 4: Poor)")
    ],
    outputs="text",
    title="Mental Health Tracker 🧠💖",
    description="Enter your daily levels to check your current mental health status. Hosted live on Render."
)

# Launch the app on the port Render expects
if _name_ == "_main_":
    iface.launch(server_name="0.0.0.0", server_port=10000)

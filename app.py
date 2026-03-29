import gradio as gr

# This function handles the logic that replaces the .pkl file
def predict_mental_health(anxiety, stress, sleep):
    # Calculate average: 1-2 is Stable, 3-4 is Severe
    avg_score = (float(anxiety) + float(stress) + float(sleep)) / 3
    
    if avg_score >= 3.0:
        return "Prediction: Severe Mental Health. Please seek professional support soon. ❤️"
    elif avg_score >= 2.0:
        return "Prediction: Moderate Stress. Consider self-care or talking to a friend. 🌿"
    else:
        return "Prediction: Stable Mental Health. You are doing great! 🌟"

# Creating the User Interface
app = gr.Interface(
    fn=predict_mental_health,
    inputs=[
        gr.Slider(1, 4, step=1, label="Anxiety Level (1: Low, 4: High)"),
        gr.Slider(1, 4, step=1, label="Stress Level (1: Low, 4: High)"),
        gr.Slider(1, 4, step=1, label="Sleep Quality (1: Good, 4: Poor)")
    ],
    outputs="text",
    title="Mental Health Tracker 🧠",
    description="Slide to select your levels and click Submit."
)

# Crucial for Render deployment
if _name_ == "_main_":
    app.launch(server_name="0.0.0.0", server_port=10000)


import gradio as gr

def predict_health(anxiety, stress, sleep):
    # Calculate average
    avg = (float(anxiety) + float(stress) + float(sleep)) / 3
    
    if avg >= 3.0:
        return "Prediction: Severe Mental Health. Please seek professional support. ❤️"
    elif avg >= 2.0:
        return "Prediction: Moderate Stress. Take a break and practice self-care. 🌿"
    else:
        return "Prediction: Stable Mental Health. You are doing great! 🌟"

# This is the simplest way to launch Gradio on Render
demo = gr.Interface(
    fn=predict_health,
    inputs=[
        gr.Slider(1, 4, step=1, label="Anxiety"),
        gr.Slider(1, 4, step=1, label="Stress"),
        gr.Slider(1, 4, step=1, label="Sleep Quality")
    ],
    outputs="text",
    title="Mental Health Tracker"
)

# Launch command
demo.launch(server_name="0.0.0.0", server_port=10000)


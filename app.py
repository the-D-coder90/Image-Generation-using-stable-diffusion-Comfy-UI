import gradio as gr
import requests
import json
import time
import os
from PIL import Image

# Define ComfyUI API URL
COMFYUI_URL = "http://127.0.0.1:8188/prompt"

# ComfyUI default output folder (update if needed)
OUTPUT_FOLDER = r"E:\ComfyUI_windows_portable\ComfyUI\output"

def get_latest_image(after_timestamp):
    """Find the most recent image that was modified AFTER the request started."""
    time.sleep(2)  # Small delay to allow file saving
    
    all_files = [
        os.path.join(OUTPUT_FOLDER, f) for f in os.listdir(OUTPUT_FOLDER) if f.endswith(".png")
    ]

    if not all_files:
        return None

    # Sort by modification time (newest last)
    all_files.sort(key=os.path.getmtime, reverse=True)

    for file in all_files:
        if os.path.getmtime(file) > after_timestamp:
            return file  # Return the first truly new file

    return None

def generate_image(positive_prompt, negative_prompt):
    """Send request to ComfyUI and wait for the new image."""

    # Capture the latest modification timestamp before generation
    last_timestamp = max(
        (os.path.getmtime(os.path.join(OUTPUT_FOLDER, f)) for f in os.listdir(OUTPUT_FOLDER) if f.endswith(".png")),
        default=0
    )

    workflow = {
        "3": {
            "inputs": {
                "seed": int(time.time()),  # Dynamic seed
                "steps": 20,
                "cfg": 8,
                "sampler_name": "euler",
                "scheduler": "normal",
                "denoise": 1,
                "model": ["4", 0],
                "positive": ["6", 0],
                "negative": ["7", 0],
                "latent_image": ["5", 0]
            },
            "class_type": "KSampler",
        },
        "4": {
            "inputs": {
                "ckpt_name": "realvisxlV50_v50LightningBakedvae.safetensors"
            },
            "class_type": "CheckpointLoaderSimple",
        },
        "5": {
            "inputs": {
                "width": 1024,
                "height": 1024,
                "batch_size": 1
            },
            "class_type": "EmptyLatentImage",
        },
        "6": {
            "inputs": {
                "text": positive_prompt,
                "clip": ["4", 1]
            },
            "class_type": "CLIPTextEncode",
        },
        "7": {
            "inputs": {
                "text": negative_prompt,
                "clip": ["4", 1]
            },
            "class_type": "CLIPTextEncode",
        },
        "8": {
            "inputs": {
                "samples": ["3", 0],
                "vae": ["4", 2]
            },
            "class_type": "VAEDecode",
        },
        "9": {
            "inputs": {
                "filename_prefix": "ComfyUI",
                "images": ["8", 0]
            },
            "class_type": "SaveImage",
        }
    }

    # Send request to ComfyUI
    response = requests.post(COMFYUI_URL, json={"prompt": workflow})
    
    if response.status_code != 200:
        return f"❌ Error: {response.text}", None

    print("🕒 Waiting for new image (1-2 mins)...")

    # Wait and poll for a new image
    start_time = time.time()
    while time.time() - start_time < 120:  # Max wait 2 minutes
        latest_image = get_latest_image(last_timestamp)

        if latest_image:
            print(f"✅ New image detected: {latest_image}")
            return "✅ Image generated successfully!", Image.open(latest_image)

        time.sleep(5)  # Check every 5 seconds

    return "⛔ Image generation timed out. Check ComfyUI.", None


# 🔹 Custom CSS for a sleek UI
custom_css = """
body {
    background-color: #121212;
    color: white;
    font-family: 'Poppins', sans-serif;
}

.gradio-container {
    max-width: 850px;
    margin: auto;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.1);
    text-align: center;
}

.gr-button {
    background: linear-gradient(45deg, #ff00ff, #ff6600);
    border: none;
    font-size: 16px;
    font-weight: bold;
    padding: 10px 20px;
    border-radius: 8px;
    color: white;
    transition: 0.3s;
    cursor: pointer;
}

.gr-button:hover {
    transform: scale(1.05);
    background: linear-gradient(45deg, #ff6600, #ff00ff);
}

.gr-textbox textarea {
    background-color: #1e1e1e;
    color: white;
    border-radius: 8px;
    border: 1px solid #ff00ff;
    padding: 10px;
    font-size: 14px;
}

h1, h2, h3 {
    text-align: center;
}

h1 {
    color: #ff00ff;
}

h2 {
    color: #ff6600;
    margin-bottom: 10px;
}

h3 {
    color: #cccccc;
    font-weight: normal;
    font-size: 16px;
}
"""

# 🔹 Default Prompts
DEFAULT_POSITIVE_PROMPT = """A futuristic cyberpunk AI, ultra-detailed, glowing neon circuits, holographic interfaces, 
hyperrealistic lighting, 8K resolution, cinematic composition, vibrant colors, intricate details, 
cybernetic enhancements, dynamic energy flow, volumetric lighting, concept art, science fiction style, 
ultra-sharp focus, ethereal atmosphere, stunning visual impact."""

DEFAULT_NEGATIVE_PROMPT = """blurry, low resolution, distorted, artifacts, text, watermark, grainy, deformed faces, 
extra limbs, unrealistic proportions, oversaturated, noisy background, low contrast, bad anatomy, 
jpeg artifacts, bad lighting, low-quality rendering."""

# Gradio UI with project details
with gr.Blocks(css=custom_css) as demo:
    gr.Markdown("<h1>🚀 Image Generation using Stable Diffusion & ComfyUI (P1)</h1>")
    gr.Markdown("<h2>A Project Report</h2>")
    gr.Markdown(
        """<h3>Submitted in partial fulfillment of the requirements of
        <br>AICTE Internship on AI: Transformative Learning with TechSaksham
        <br>A joint CSR initiative of Microsoft & SAP</h3>"""
    )
    gr.Markdown("<h3><b>By:</b> Hitesh Kumar, hiteshofficial0001@gmail.com</h3>")

    with gr.Row():
        pos_prompt = gr.Textbox(
            label="🌟 Positive Prompt", 
            lines=4, 
            interactive=True, 
            value=DEFAULT_POSITIVE_PROMPT
        )
        neg_prompt = gr.Textbox(
            label="🚫 Negative Prompt", 
            lines=3, 
            interactive=True, 
            value=DEFAULT_NEGATIVE_PROMPT
        )

    btn = gr.Button("🎨 Generate Image", elem_classes=["gr-button"])
    status_msg = gr.Textbox(label="Status", interactive=False, show_label=False)
    output_image = gr.Image(label="🖼️ Generated Image", type="pil", interactive=False)

    btn.click(generate_image, inputs=[pos_prompt, neg_prompt], outputs=[status_msg, output_image])

# Run Gradio UI
demo.launch()

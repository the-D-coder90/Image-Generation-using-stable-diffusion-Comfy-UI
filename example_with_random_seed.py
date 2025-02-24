import json
import os
import time
import random

import gradio as gr
import numpy as np
import requests

from PIL import Image

# Configuration
URL = "http://127.0.0.1:8188/prompt"
INPUT_DIR = r"E:\ComfyUI_windows_portable\ComfyUI\input"
OUTPUT_DIR = r"E:\ComfyUI_windows_portable\ComfyUI\output"

def get_latest_image(folder):
    """Fetch the latest generated image from the output directory."""
    files = os.listdir(folder)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder, x)))
    latest_image = os.path.join(folder, image_files[-1]) if image_files else None
    return latest_image

def start_queue(prompt_workflow):
    """Send the prompt request to ComfyUI."""
    p = {"prompt": prompt_workflow}
    data = json.dumps(p).encode('utf-8')
    requests.post(URL, data=data)

def generate_image(input_image):
    """Process and generate the anime-style image using ComfyUI."""
    with open("workflow_api.json", "r") as file_json:
        prompt = json.load(file_json)

    prompt["3"]["inputs"]["seed"] = random.randint(1, 1500000)

    # Resize image to match the model input
    image = Image.fromarray(input_image)
    min_side = min(image.size)
    scale_factor = 512 / min_side
    new_size = (round(image.size[0] * scale_factor), round(image.size[1] * scale_factor))
    resized_image = image.resize(new_size)

    # Save input image to the ComfyUI input directory
    resized_image.save(os.path.join(INPUT_DIR, "test_api.jpg"))

    previous_image = get_latest_image(OUTPUT_DIR)
    
    start_queue(prompt)

    while True:
        latest_image = get_latest_image(OUTPUT_DIR)
        if latest_image != previous_image:
            return latest_image
        time.sleep(1)

# Gradio UI
demo = gr.Interface(
    fn=generate_image,
    inputs=gr.Image(type="numpy", label="Upload an Image"),
    outputs=gr.Image(label="Generated Anime Image"),
    title="✨ AI Anime Image Generator",
    description="🎨 Convert any real image into anime-style using RealVisXL & ComfyUI. 📌 Internship Project - TechShaksham AICTE Edunet Foundation.",
    allow_flagging="never",
    theme="compact",
)

# Launch the Gradio app with debug mode to see any errors
demo.launch(share=True, debug=True)

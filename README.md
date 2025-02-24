## A PROJECT REPORT ON

# IMAGE GENERATION USING STABLE DIFFUSION & COMFYUI (P1)

### Submitted in partial fulfillment of the requirements of

## AICTE Internship on AI: Transformative Learning with Tech Saksham  
A joint CSR initiative of Microsoft & SAP

---

## **Submitted By:**  
**Kshitiz Namdeo**  
*CSE Student, Pranveer Singh Institue of Technology*  
Email: kshitiz.namdeo1112@gmail.com  

---

## **Abstract**

This project explores the power of AI-driven image generation using **Stable Diffusion** and **ComfyUI**. The objective is to generate high-quality, photorealistic, and artistic images based on textual prompts using a deep-learning pipeline. The project utilizes **ComfyUI**, an advanced workflow-based user interface for Stable Diffusion, to generate and refine images. This report discusses the implementation details, workflow structure, dataset preparation, and the automation pipeline used in the project.

---
## **Demo Images**

![Image](https://github.com/user-attachments/assets/11d61039-20cf-4e40-a600-65501d341941)
## Workflow of Image to Image generation

![image](https://github.com/user-attachments/assets/536f964c-8f69-42f9-b585-278e7df69a38)

---

![image](https://github.com/user-attachments/assets/bdd8a386-19fc-42f7-a933-285327611d6b)

## Workflow of Text to Image

![image](https://github.com/user-attachments/assets/71b64d29-adda-4d23-8331-0e3bd15a448a)

## Sample of Generated Images

![image](https://github.com/user-attachments/assets/0e1eb358-d0a6-4cc3-a2c3-d5f7a5a3536d)

---

![image](https://github.com/user-attachments/assets/e6e89450-b964-4b67-a8e5-5f6c3c5fafe5)

---

![image](https://github.com/user-attachments/assets/3d6119a2-abc8-482c-bf7f-42d6c92b94d5)

---

![image](https://github.com/user-attachments/assets/db5e1409-ada8-4648-a14d-189023be3182)

---
## **Table of Contents**
1. Introduction
2. Project Objectives
3. Technologies Used
4. System Architecture
5. Implementation
6. Results and Discussion
7. Challenges Faced
8. Future Work
9. Conclusion
10. References

---

## **1. Introduction**

Image generation using AI has seen rapid advancements with models like **Stable Diffusion**, which can generate highly detailed images based on text prompts. This project utilizes **ComfyUI**, a powerful workflow-based UI, to create a structured pipeline for generating images while optimizing performance.

---

## **2. Project Objectives**

- Implement an AI-powered image generation system.
- Use **Stable Diffusion** to generate high-resolution images based on textual prompts.
- Integrate **ComfyUI** for an efficient and user-friendly interface.
- Automate image generation with Gradio-based UI and API requests.
- Optimize workflow configurations for better output quality.

---

## **3. Technologies Used**

- **Stable Diffusion** - AI-based text-to-image model.
- **ComfyUI** - Workflow-based UI for Stable Diffusion.
- **Gradio** - Web-based UI framework for AI applications.
- **Python** - Core programming language for implementation.
- **PIL (Pillow)** - Image processing library.
- **Flask** - Backend API development.
- **FAISS** - Vector search and retrieval system.
- **NumPy & OpenCV** - Data manipulation and image processing.

---

## **4. System Architecture**

The project follows a modular pipeline approach:

- **Input Handling** - Users provide a text prompt.
- **Processing** - The prompt is sent to Stable Diffusion via ComfyUI.
- **Image Generation** - The AI model generates images based on the prompt.
- **Post-processing** - Refinements such as upscaling and enhancements.
- **Output Display** - The final image is displayed in the Gradio UI.

  ![image](https://github.com/user-attachments/assets/5b505232-c6a7-498c-bc2e-9cff1a10edb7)


---

## **5. Implementation**

### **5.1 Directory Structure**
```
└── the-D-coder90-image-generation-using-stable-diffusion-comfyui/
    ├── README.md
    ├── app.py
    ├── example_nested_loop.py
    ├── example_with_random_seed.py
    ├── requirements.txt
    ├── text_to_image.json
    └── workflow_api.json
```

### **5.2 Gradio-based UI Implementation**
The interface is built using **Gradio**, allowing users to input prompts and generate images in real-time.

#### **Key Features:**
- Custom UI with a sleek dark theme.
- Dynamic text-to-image generation.
- Automated prompt processing.
- Status updates and image previews.

```python
import gradio as gr

def generate_image(prompt):
    # Call ComfyUI API and generate image (implementation inside app.py)
    return f"Generated Image for: {prompt}"

demo = gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(placeholder="Enter your prompt here..."),
    outputs=gr.Image(type="pil"),
    title="AI Image Generator",
)
demo.launch()
```

---

## **6. Results and Discussion**

The system successfully generates high-quality images with rich details based on textual inputs. The ComfyUI workflow allows greater flexibility and fine-tuning, making it a robust solution for AI-generated art and photography.

---

## **7. Challenges Faced**

- **Computational Requirements**: Running Stable Diffusion locally requires high GPU power.
- **Fine-tuning Prompts**: Generating specific images requires carefully crafted prompts.
- **Latency Issues**: Image generation takes a few seconds to minutes depending on settings.

---

## **8. Future Work**

- Improve the model efficiency and reduce generation time.
- Implement real-time fine-tuning options for users.
- Expand the UI with multiple style customization options.
- Deploy on Hugging Face Spaces for cloud-based access.

---

## **9. Conclusion**

This project successfully demonstrates the application of **Stable Diffusion & ComfyUI** in AI-driven image generation. With an efficient workflow, the system provides an intuitive interface for users to create stunning AI-generated artwork.

---

## **10. References**

1. **Stable Diffusion Documentation** - https://stablediffusionweb.com/
2. **ComfyUI GitHub Repository** - https://github.com/comfyanonymous/ComfyUI
3. **Gradio Documentation** - https://www.gradio.app/

---

### **Acknowledgment**
I sincerely thank **AICTE, Microsoft, and SAP** for the opportunity to work on this AI internship under the **Tech Saksham initiative**, which enabled me to explore advanced AI-driven image generation techniques.


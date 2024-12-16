import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel('gemini-1.5-flash')


def gemini_vision_response(model,prompt,image):
    prompt = f'''Analyze the image comprehensively:
1. Describe all visible elements (objects, patterns, relationships)
2. Detail colors, textures, shapes, and notable features
3. Explain any artistic, symbolic, or contextual significance
4. Address this specific question: {user_prompt}

Provide an insightful response covering both visual and contextual details.
'''
    response = model.generate_content([prompt,image])
    return response.text




st.set_page_config(
    page_title="Chat with Your Image",
    page_icon="🧠",
    layout="centered"
)

st.title("**Chat with Your Image** - **Using Gemini Pro Vision**")

image = st.file_uploader("Upload an image",type=["jpg","png","jpeg"])

user_prompt = st.text_input("Enter your query:")


if st.button("Submit"):
    load_image = Image.open(image)

    colLeft,colRight = st.columns(2)

    st.image(load_image.resize((800,500)))

    caption_response = gemini_vision_response(model,user_prompt,load_image)

    st.info(caption_response)

def set_bg_from_url(url, opacity=1):
    
    footer = """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <footer>
        <div style='visibility: visible;margin-top:7rem;justify-content:center;display:flex;'>
            <p style="font-size:1.1rem;">
                Made For Fun Using AI
                </a>
            </p>
        </div>
    </footer>
"""
    st.markdown(footer, unsafe_allow_html=True)
    

    st.markdown(
        f"""
        <style>
            body {{
                background: url('{url}') no-repeat center center fixed;
                background-size: cover;
                opacity: {opacity};
            }}
        </style>    
        """,
        unsafe_allow_html=True
    )
set_bg_from_url("https://img.freepik.com/free-photo/3d-dark-grunge-display-background-with-smoky-atmosphere_1048-16218.jpg", opacity=0.8)

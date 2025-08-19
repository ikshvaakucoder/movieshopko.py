# import streamlit as st
from PIL import Image
import requests
import io

# ✅ Set browser tab title and icon BEFORE anything else
st.set_page_config(favicon.png

    page_title="AI 2D → 3D Character App",  # This changes the tab
    page_icon="️",     # Optional icon
    layout="wide"
)

st.title("Welcome to My AI 2D → 3D Character App")
st.write("This is my Python web app running on localhost.")

# Step 1: Upload 2D image
uploaded_file = st.file_uploader("Upload a 2D character or photo", type=["png", "jpg", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.info("Step 2: Convert to 3D model using AI API")

    # Example pseudo-code for API
    api_url = "https://api.meshy.ai/convert_2d_to_3d"  # placeholder
    files = {"image": uploaded_file.getvalue()}
    headers = {"Authorization": "Bearer YOUR_API_KEY"}

    with st.spinner("Generating 3D model..."):
        response = requests.post(api_url, files=files, headers=headers)
        if response.status_code == 200:
            st.success("3D model generated!")
            model_url = response.json().get("model_url")
            st.write(f"Download your 3D model: [link]({model_url})")
        else:
            st.error("Failed to generate 3D model. Check API key and endpoint.")

    st.info("Step 3: Apply AI motion capture (optional, via API)")

    mocap_video = st.file_uploader("Upload actor video for motion capture", type=["mp4", "mov"])
    if mocap_video:
        mocap_api_url = "https://api.deepmotion.com/animate_3d"  # placeholder
        files = {"video": mocap_video.getvalue(), "model_url": model_url}
        with st.spinner("Applying motion to 3D model..."):
            response = requests.post(mocap_api_url, files=files, headers=headers)
            if response.status_code == 200:
                animated_model_url = response.json().get("animated_model_url")
                st.success("Motion applied!")
                st.write(f"Download animated 3D model: [link]({animated_model_url})")
            else:
                st.error("Motion capture failed. Check API and input files.")

    st.info("Step 4: Photorealistic rendering / AI editing")
    st.write("This step can use NVIDIA Omniverse, Firefly, or Stable Diffusion APIs for final realism.")


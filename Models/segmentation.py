import numpy as np
import tensorflow as tf  # type: ignore
import keras # type: ignore
import streamlit as st
from PIL import Image
#load model
loaded_model = keras.models.load_model("D:\\Downloads\\u_net.h5", compile=False)
# Preprocess the image for the model
def preprocess_image(image):
    image = image.resize((128, 128))  # Resize to the model's input shape
    image = np.array(image) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image


def segmentation_page():
    st.title("Brain Tumor Segmentation")
    st.subheader("Upload an Image")
    
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png","tif", "tiff"])

    col1,col2=st.columns(2)

    if uploaded_file is not None:
        # Open the image file
        with col1:
            st.image(uploaded_file, caption='Uploaded Image.', width=400)

        with col2:
            if st.button('Segmentation'):
                #Make the prediction
                image = Image.open(uploaded_file)
                processed_image = preprocess_image(image)

                predicted_mask = loaded_model.predict(processed_image)         
                # Convert to binary mask
                predicted_mask = predicted_mask > 0.5
                predicted_mask=  np.squeeze(predicted_mask)
                predicted_mask_rescaled = (predicted_mask * 255).astype(np.uint8)  
                st.image(predicted_mask_rescaled, caption='Predicted Segmentation Mask', width=400)
    else:
        st.info("Please upload an image to see a preview.")
    
    st.markdown("<hr style='border:1px solid gray'>", unsafe_allow_html=True)
    st.markdown("Made with :heart: using our Team", unsafe_allow_html=True)


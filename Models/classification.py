import numpy as np
import tensorflow as tf  # type: ignore
import keras # type: ignore
import streamlit as st
from PIL import Image
import tempfile
import speech_recognition as sr  # type: ignore
from gtts import gTTS  # type: ignore
import base64
import time

#load model
loaded_model=keras.models.load_model("D:\Downloads\cnn_model (1).h5")

# Preprocess the image for the model
def preprocess_image(image):
    image = image.resize((224, 224))  # Resize to the model's input shape
    image = np.array(image) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

def predict(image):
    processed_image = preprocess_image(image)
    
    # Make prediction
    predictions = loaded_model.predict(processed_image)
    
    class_id = np.argmax(predictions[0])  # Get the class with the highest probability
    
    if class_id == 0:
        return "This image indicates a pituitary tumor."
    
    elif class_id == 1: 
        return "This image shows the pituitary gland, confirmed to be free of tumors."
    
    elif class_id == 2:
        return "This image indicates a meningioma tumor."
    
    else:
        return "This image indicates a glioma tumor."

def speak_text(text):
    tts = gTTS(text=text, lang='en')
    # Save audio in a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tts.save(tmp.name)
        return tmp.name  # Return the path to the saved file

def get_base64_audio(file_path):
    # Read the audio file in binary mode and encode it to base64
    with open(file_path, "rb") as audio_file:
        base64_audio = base64.b64encode(audio_file.read()).decode('utf-8')
    return base64_audio

# Function to capture voice input
#def capture_voice():
   # recognizer = sr.Recognizer()
   # with sr.Microphone() as source:
       # st.write("Please speak your question...")
       # audio = recognizer.listen(source)
    
   # try:
        # Recognize speech using Google Speech Recognition
       # question = recognizer.recognize_google(audio)
        #st.write(f"You asked: {question}")
       # return question
    #except sr.UnknownValueError:
        #st.error("Sorry, I could not understand your question.")
       # return None
   # except sr.RequestError as e:
       # st.error(f"Could not request results from Google Speech Recognition service; {e}")
       # return None

def classification():
    # Initialize session state variables if they don't exist
    if 'answer' not in st.session_state:
        st.session_state.answer = None
    if 'audio_file_path' not in st.session_state:
        st.session_state.audio_file_path = None
    # Image upload widget
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    col1, col2 = st.columns(2)

    if uploaded_file is not None:
        # Open the image file
        with col1:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image.', width=400)

        with col2:
            if st.button("Prediction"):
                label=predict(image)
                st.markdown(f"<h3 style='text-align: center; color: #FFFFFF;'>{label}</h3>", unsafe_allow_html=True)
                # Button to capture voice question
            if st.button("Play Audio"):
               # question = capture_voice()
                
               # if question:
                    # Placeholder for question-answering logic
                    st.session_state.answer = predict(image)  #output
                    st.session_state.audio_file_path = speak_text(st.session_state.answer)

                    # Introduce a 1-second delay before showing the audio component
                  #  time.sleep(1)

                    # Autoplay the audio response using base64 encoding
                    base64_audio = get_base64_audio(st.session_state.audio_file_path)
                    audio_html = f"""
                    <audio autoplay>
                        <source src="data:audio/mp3;base64,{base64_audio}" type="audio/mp3">
                    </audio>
                    """
                    st.components.v1.html(audio_html, height=0)
            
    else:
        st.info("Please upload an image to see a preview.")


    # Add a footer or branding if needed
    st.markdown("<hr style='border:1px solid gray'>", unsafe_allow_html=True)
    st.markdown("Made with :heart: using our Team", unsafe_allow_html=True)



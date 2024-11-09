import streamlit as st
from Models.classification import classification # type: ignore
from Models.segmentation import segmentation_page # type: ignore

st.set_page_config(page_title="Classification & Segmentation",page_icon=":brain:", layout="wide")

# Function for the home page
def home_page():
    st.title("Bio Assistant tool")
    st.write("Welcome to the Brain Tumor Classification & Segmentation App!")
    st.write("Use the sidebar to navigate to different functionalities.")
    st.markdown("<hr style='border:1px solid gray'>", unsafe_allow_html=True)
    st.markdown("Made with :heart: using our Team", unsafe_allow_html=True)

def classification_page():
    st.title('Brain Tumor Classification')
    st.subheader("Upload an Image")
    classification()

# Main application
def main():
    st.sidebar.title("Navigation")
    pages = {
        "Home": home_page,
        "Classification": classification_page,
        "Segmentation": segmentation_page,
    }

    # Sidebar navigation
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    # Call the selected page function
    pages[selection]()

if __name__ == "__main__":
    main()

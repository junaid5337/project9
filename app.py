import streamlit as st
from PIL import Image

def main():
    st.set_page_config(page_title="My Streamlit Website", page_icon="🌎", layout="wide")
    
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About", "Upload Image"])
    
    if page == "Home":
        home()
    elif page == "About":
        about()
    elif page == "Upload Image":
        upload_image()

def home():
    st.title("Welcome to My Streamlit Website! 🚀")
    st.write("This is a simple web app built using Streamlit. Explore the sections using the sidebar!")

def about():
    st.title("About This App")
    st.write("This is a quick project demonstrating how to build a basic website using Streamlit in just 15 minutes!")
    st.write("Features:")
    st.markdown("- **Home Page** with a welcome message")
    st.markdown("- **Sidebar Navigation**")
    st.markdown("- **Image Upload & Display**")
    st.markdown("- **Live User Input Display**")

def upload_image():
    st.title("Upload an Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
        st.success("Image uploaded successfully!")

if __name__ == "__main__":
    main()

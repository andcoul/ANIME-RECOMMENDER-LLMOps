import streamlit as st
from dotenv import load_dotenv
from pipeline.pipeline import RecommendationPipeline

st.set_page_config(page_title="Anime Recommendation System", page_icon=":books:", layout="wide")

load_dotenv()

@st.cache_resource
def initialize_pipeline():
    return RecommendationPipeline()

pipeline = initialize_pipeline()

st.title("Anime Recommendation System")
st.write("Ask a question about anime and get recommendations!")

query = st.text_input("Enter your question here eg.: light novel anime with romance and action")

if st.button("Get Recommendation"):
    if query:
        with st.spinner("Generating recommendation..."):
            try:
                recommendation = pipeline.get_recommendation(query)
                st.subheader("Recommended Anime:")
                st.write(recommendation)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question to get recommendations.")
from src.vector_store import VectorStore
from src.recommender import AnimeRecommender
from dotenv import load_dotenv
from utility.logger import get_logger
from config.config import GROQ_API_KEY, MODEL_NAME
import os

load_dotenv()
logger = get_logger(__name__)

class RecommendationPipeline:
    def __init__(self):
        try:
            logger.info("Loading vector store...")
            vector_store_instance = VectorStore()
            retriever = vector_store_instance.load_vector_store().as_retriever()
            logger.info("Vector store loaded successfully.")

            self.recommender = AnimeRecommender(retriever=retriever, api_key=GROQ_API_KEY, model_name=MODEL_NAME)
        except Exception as e:
            logger.error(f"Failed to initialize RecommendationPipeline: {e}")
            raise

    def get_recommendation(self, question: str):
        try:
            logger.info("Generating recommendation...")
            response = self.recommender.get_recommend(question)
            logger.info("Recommendation generated successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to get recommendation: {e}")
            raise
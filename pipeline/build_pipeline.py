from src.data_loader import DataLoader
from src.vector_store import VectorStore
from utility.custom_exception import CustomException
from utility.logger import get_logger

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting the data loading and vector store creation process.")

        dataloader = DataLoader(file_path="data/anime_with_synopsis.csv", processed_data="data/processed_anime.csv")
        processed_file = dataloader.load_data()
    
        vector_store_instance = VectorStore()
        documents = vector_store_instance.document_loader(file_path=processed_file)
        vector_store_instance.create_vector_store(documents)

        logger.info("Vector store created and persisted successfully.")

    except Exception as e:
        raise CustomException("An error occurred in the pipeline.", e)

if __name__ == "__main__":
    main()
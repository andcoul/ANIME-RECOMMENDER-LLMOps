from src.prompt_template import get_anime_prompt
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

class AnimeRecommender:
    def __init__(self,retriever, api_key: str, model_name: str):
        self.prompt = get_anime_prompt()
        self.llm = ChatGroq(api_key=api_key, model_name=model_name, temperature=0)

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever= retriever, 
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.prompt}
        )

    def get_recommend(self, question: str):
        result = self.qa_chain({"query": question})
        return result['result']
    

import openai
import os
from langchain.chat_models import ChatOpenAI
import chromadb
import pandas as pd
import numpy as np

chroma_client = chromadb.PersistentClient()

rag_llm = ChatOpenAI(temperature=0.0, model="gpt-3.5-turbo")

try : 
  collection = chroma_client.create_collection(name="doctors")
  df1 = pd.read_csv("Symptoms_Doctors_dataset.csv").iloc[:,1:]
  for i in range(len(df1)):
    disease, symptoms, precautions, recommendations = tuple(df1.iloc[i])
    collection.add(
        documents=[symptoms],
        metadatas=[{"Disease": disease, "Precautions":precautions, "Recommendations": recommendations}],
        ids=[str(i)]
    )
except :
  collection = chroma_client.get_collection(name="doctors")


def make_recommendation(query_symptom):
  results = collection.query(query_texts=[query_symptom], n_results=2)
  most_similar_symptom = results['documents'][0][0]
  results = results['metadatas'][0][0]
  recommendations = results["Recommendations"]
  precautions = results["Precautions"]
  most_similar_disease = results["Disease"]

  prompt = f"""
    Symptoms : {query_symptom}
    Based on the above symptom, do you think the patient suffer from {most_similar_disease}? 
    if yes, just write the following :
      ##Precautions : {precautions}
      ## Doctor Recommendtions : 
      {recommendations}
    If no, respond using your knowledge in medecine following the format:
      ##Precautions : (what do you suggest as precautions) 
      ## Doctor Recommendtions : 
        #Suggestion 1
        Full Name: (moroccan name)
        Doctor speciality / Title (the speciality should match the disease and its symptoms): 
        ID :
        Phone number : (moroccan phone number)
        Adress : (moroccan adress in casablanca)
        
        #Suggestion 2
        ....
    
    write your answers in Markdown with a stunning design (use bold, titles, alignment, padding, etc)
  """
#Remember, translate your answer to arabic.
  recommendation_precautions = rag_llm.predict(prompt)
  return recommendation_precautions
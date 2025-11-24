# Resume Screening MVP (Minimum Viable Product)

## 🎯 Project Goal
The primary goal of this project is to develop an end-to-end Machine Learning solution that automates the initial screening of job applications. The system will take a resume (PDF/DOCX) and a job description (text) as input, process the text, and calculate a **Relevance Score** using NLP and similarity techniques (like Cosine Similarity on TF-IDF vectors). This MVP demonstrates the entire ML lifecycle from data collection to deployment.

## 🛠️ Tech Stack
* **Language:** Python 3+
* **Core Libraries:** pandas, numpy, spacy, scikit-learn
* **Document Parsing:** python-docx, PyPDF2
* **Similarity Scoring:** rapidfuzz
* **Web Framework (Deployment):** Streamlit

## 🗺️ Milestones & Roadmap

| Milestone | Description | Status |
| :--- | :--- | :--- |
| **0** | **Project Bones:** Initial setup, folder structure, requirements. | **COMPLETE** |
| 1 | **Data Acquisition & Parsing:** Collect sample data, implement robust PDF/DOCX text extraction. | TO DO |
| 2 | **Preprocessing & Feature Engineering:** Clean text, implement TF-IDF vectorizer. | TO DO |
| 3 | **Scoring & Modeling:** Implement Cosine Similarity logic for relevance scoring. | TO DO |
| 4 | **Deployment (MVP):** Build the Streamlit application for end-to-end demo. | TO DO |

# 📄 AI Resume Screener & Career Guide

**A Smart Resume Analysis Tool built with Python & NLP.**

This project is an End-to-End Machine Learning Web Application that helps job seekers evaluate their resumes against specific job descriptions. It uses **Natural Language Processing (NLP)** techniques to parse resumes, match keywords, and provide actionable feedback on missing skills and recommended projects.

## 🚀 Live Demo
**[Click Here to Try the App](https://your-streamlit-app-link-here.streamlit.app/)** *(Replace this link after you deploy on Streamlit Cloud)*

---

## 🛠️ Features
* **Role-Based Screening:** Select from various roles (e.g., Data Scientist, ML Engineer, Full Stack Dev).
* **PDF Parsing:** Extracts text from PDF resumes using `pdfplumber`.
* **Intelligent Cleaning:** Uses Regex to clean special characters while preserving technical terms (C++, .NET, etc.).
* **Skill Matching:** Compares resume keywords against a predefined JSON knowledge base.
* **Scoring System:** Calculates a percentage match score (0-100%).
* **Gap Analysis:** Identifies exactly which skills are missing from the resume.
* **Smart Recommendations:** Suggests specific projects to build to bridge the skill gap.

---

## 🏗️ Tech Stack
* **Language:** Python 3.10+
* **Frontend:** Streamlit
* **Text Processing:** Regex (re), PDFPlumber
* **Data Structure:** JSON (for Skill/Role Database)

---

## 📂 Project Structure

Resume-Scanner/ ├── app.py # Main Application Logic (Streamlit + NLP) ├── roles_config.json # The Knowledge Base (Skills & Projects database) ├── requirements.txt # List of dependencies └── README.md # Project Documentation


---

## ⚙️ How to Run Locally

If you want to run this on your own machine, follow these steps:

**1. Clone the Repository**
```bash
git clone [https://github.com/ashtab1925/Resume-Scanner-AI.git](https://github.com/ashtab1925/Resume-Scanner-AI.git)
cd Resume-Scanner-AI
2. Create a Virtual Environment (Optional but recommended)
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the Application
streamlit run app.py

🧠 How It Works
1. Resume Extraction

The uploaded PDF is processed using pdfplumber.

Extracted text is converted into a raw working string.

2. Preprocessing

Converted to lowercase

Removes unnecessary special characters

Preserves technical symbols like +, #, ., -

3. Skill Matching Logic

Resume text → Converted into a set of unique words

Role requirements → Loaded from roles_config.json

Intersection = Matched Skills

4. Scoring Formula
Score = (Matched Skills / Total Required Skills) * 100

5. Feedback

Shows matched skills

Shows missing skills

Returns recommended projects to build next

📈 Future Enhancements

Resume section classification (Experience, Projects, Skills)

JD-to-Resume matching (upload Job Description directly)

AI-based suggestion engine for improved resume writing

Skill proficiency scoring with semantic similarity (spaCy / BERT)

👨‍💻 Author

Abubakar Siddique
Aspiring Machine Learning Engineer | Data Science Enthusiast

🔗 www.linkedin.com/in/abubakar-siddique1925

🐙 GitHub

⭐ Support

If you find this project helpful, please consider giving it a ⭐ on GitHub!

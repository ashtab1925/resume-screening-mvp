import streamlit as st
import pdfplumber
import json
import re

# --- STEP 1: Load the Knowledge Base ---
try:
    with open('skills.json', 'r') as file:
        role_data = json.load(file)
except FileNotFoundError:
    st.error("Error: 'skills.json' file not found. Please create it first.")
    st.stop()
except json.JSONDecodeError:
    st.error("Error: Your JSON file is not formatted correctly.")
    st.stop()

# --- STEP 2: Function to Extract Text from PDF ---
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            extract = page.extract_text()
            if extract:  # Check if text exists on page
                text += extract + "\n"
    return text

# --- STEP 3: Function to Clean Text (UPDATED) ---
def clean_text(text):
    text = text.lower() 
    # FIX: Allow a-z, 0-9, +, #, and . (for C++, C#, .NET, Node.js)
    # We replace everything else with a space
    text = re.sub(r'[^a-z0-9\+\#\.]', ' ', text)
    return text

# --- STEP 4: The Scoring Logic ---
def analyze_resume(text, role):
    # 1. Get requirements
    # Change 'skills' to whatever you wrote in your JSON file
    required_skills = [skill.lower() for skill in role_data[role]['required_skills']]
    # required_skills = [skill.lower() for skill in role_data[role]['skills']]
    recommended_projects = role_data[role]['suggested_projects']
    
    # 2. Prepare Resume Text
    resume_text = clean_text(text)
    
    # Debugging: Uncomment the line below to see what the computer sees
    # st.write(f"DEBUG (Cleaned Text): {resume_text}") 

    present_skills = []
    missing_skills = []
    
    # 3. Comparison Logic
    # We split resume text into a set of words for faster, accurate matching
    resume_words = set(resume_text.split())

    for skill in required_skills:
        # Check if the skill exists in the resume text
        # We check two ways: 
        # A) Exact word match (ideal)
        # B) Substring match (fallback, e.g., "machine learning" inside text)
        if skill in resume_words or skill in resume_text:
            present_skills.append(skill)
        else:
            missing_skills.append(skill)
            
    # 4. Calculate Score (Prevent Division by Zero)
    if len(required_skills) > 0:
        score = (len(present_skills) / len(required_skills)) * 100
    else:
        score = 0
    
    return score, present_skills, missing_skills, recommended_projects

# --- STEP 5: The Website UI ---

st.set_page_config(page_title="Resume Scanner", page_icon="📄")

st.title("📄 AI Resume Screener & Career Guide")
st.markdown("### Upload your resume to see how well it matches the job role!")

# Dropdown
selected_role = st.selectbox("Select the Role you are applying for:", list(role_data.keys()))

# File Upload
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")

# Button
if uploaded_file is not None:
    if st.button("Analyze Resume"):
        
        with st.spinner("Analyzing your resume..."):
            # 1. Extract
            resume_text = extract_text_from_pdf(uploaded_file)
            
            # 2. Analyze
            score, present, missing, projects = analyze_resume(resume_text, selected_role)
            
        # --- DISPLAY RESULTS ---
        st.divider()
        st.header(f"Match Score: {round(score, 2)}%")
        
        # Progress Bar
        st.progress(score / 100) # Streamlit expects 0.0 to 1.0
        
        # Columns for layout
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("✅ Skills You Have")
            for skill in present:
                st.write(f"- {skill.upper()}")
                
        with col2:
            st.error("❌ Missing Skills")
            for skill in missing:
                st.write(f"- {skill.upper()}")
        
        st.divider()
        
        # Recommendations
        if score < 100:
            st.info("💡 Recommended Projects to Fill the Gap:")
            for proj in projects:
                st.write(f"★ {proj}")
        else:
            st.balloons()
            st.success("🎉 Your resume is a perfect match for this role!")
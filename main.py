import streamlit as st
from document_processor import process_document
from llm_integration import LLMIntegration
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize LLM integration
api_key = os.getenv('GROQ_API_KEY')
if api_key is None:
    st.error("GROQ API key not found. Please make sure it's set in your .env file.")
    st.stop()

llm_integration = LLMIntegration(api_key)

st.title('Smart Contract Analyzer')
st.text('This tool allows you to analyze smart contracts and ask questions about them.')

uploaded_file = st.file_uploader("Choose a contract file", type=['pdf', 'docx'])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Process the document
    document_text = process_document(uploaded_file.name)
    
    # Analyze contract
    analysis = llm_integration.analyze_contract(document_text)
    
    # Display results
    st.header("Contract Summary")
    st.write(analysis['summary'])
    
    st.header("Key Clauses")
    for clause in analysis['key_clauses']:
        st.subheader(f"Clause Type: {clause['type']}")
        st.write("Content:")
        st.write(clause['content'])
        st.write("Analysis:")
        st.write(clause['analysis'])
        st.markdown("---")
    
    st.header("Overall Assessment")
    st.write(analysis['overall_assessment'])
    
    # Allow for follow-up questions
    st.header("Ask a Follow-up Question")
    user_question = st.text_input("Enter your question about the contract:")
    if user_question:
        followup_result = llm_integration.get_followup_analysis(user_question, str(analysis))
        st.write("Answer:")
        st.write(followup_result['answer'])
        st.write("Explanation:")
        st.write(followup_result['explanation'])
    
    # Clean up: remove the temporary file
    os.remove(uploaded_file.name)

st.sidebar.header("About")
st.sidebar.write("This Smart Contract Analyzer uses GROQ Mixtral to help analyze legal contracts. Upload a contract to get started!")
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
    
    st.header("Contract Balance")
    balance_score = analysis.get('balance_score', 50)  # Default to 50 if not provided
    
    # Create a custom slider with party names
    st.write("Contract Favorability:")
    cols = st.columns([1, 10, 1])
    with cols[0]:
        st.write("Employer")
    with cols[1]:
        st.slider("", 0, 100, balance_score, disabled=True, key="balance_slider")
    with cols[2]:
        st.write("Employee")

    # Interpret the balance score
    if balance_score < 40:
        st.warning(f"This contract appears to significantly favor the employer. (Score: {balance_score}/100)")
    elif balance_score > 60:
        st.success(f"This contract appears to be relatively balanced or slightly favor the employee. (Score: {balance_score}/100)")
    else:
        st.info(f"This contract has some balance issues that may need attention. It slightly favors the employer. (Score: {balance_score}/100)")

    # Provide a more detailed explanation
    st.write("Explanation:")
    if balance_score < 20:
        st.write("The contract heavily favors the employer, potentially to an unfair degree. Major revisions may be necessary to ensure fairness.")
    elif balance_score < 40:
        st.write("The contract significantly favors the employer. Some clauses may need to be renegotiated to better protect the employee's interests.")
    elif balance_score < 60:
        st.write("The contract slightly favors the employer. While not drastically unbalanced, there may be room for improvement in certain areas.")
    elif balance_score < 80:
        st.write("The contract is relatively balanced, with a slight favor towards the employee. This is generally a good sign, but review all clauses carefully.")
    else:
        st.write("The contract appears to favor the employee more than usual. While this may be beneficial for the employee, ensure all terms are legally sound and sustainable for both parties.")

    
    st.header("Key Clauses")
    for clause in analysis['key_clauses']:
        st.subheader(f"Clause Type: {clause['type']}")
        st.write("Content:")
        content = clause['content']
        if 'issues' in clause and clause['issues']:
            for issue in clause['issues']:
                content = content.replace(issue, f"**{issue}**")
        st.markdown(content)
        st.write("Analysis:")
        st.write(clause['analysis'])
        if 'issues' in clause and clause['issues']:
            st.error("Issues detected in this clause:")
            for issue in clause['issues']:
                st.write(f"- {issue}")
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

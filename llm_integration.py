import groq
import json
import os

class LLMIntegration:
    def __init__(self, api_key=None):
        if api_key is None:
            api_key = os.environ.get("GROQ_API_KEY")
        if api_key is None:
            raise ValueError("GROQ API key not provided and not found in environment variables")
        self.client = groq.Groq(api_key=api_key)

    def analyze_contract(self, contract_text):
        prompt = f"""
        Analyze the following contract and provide a structured response in JSON format:

        Contract text:
        {contract_text[:4000]}

        Please provide the analysis in the following JSON structure:
        {{
            "summary": "A brief summary of the entire contract",
            "key_clauses": [
                {{
                    "type": "The type of clause",
                    "content": "The text of the clause",
                    "analysis": "A brief analysis of the clause, including any potential issues or risks, highlight the issues in bold if there are any."
                }}
            ],
            "overall_assessment": "An overall assessment of the contract, including major strengths and weaknesses"
        }}
        """

        response = self.client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[
                {"role": "system", "content": "You are an AI legal assistant specialized in contract analysis."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=4000,
        )

        return json.loads(response.choices[0].message.content)

    def get_followup_analysis(self, question, context):
        prompt = f"""
        Based on the following contract analysis, answer this question:
        {question}

        Contract analysis context:
        {context}

        Please provide your response in the following JSON format:
        {{
            "answer": "Your answer to the question",
            "explanation": "An explanation or justification for your answer"
        }}
        """

        response = self.client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[
                {"role": "system", "content": "You are an AI legal assistant specialized in contract analysis."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=1000,
        )

        return json.loads(response.choices[0].message.content)
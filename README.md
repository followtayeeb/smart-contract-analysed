# Smart Contract Analyzer

## Description

The Smart Contract Analyzer is an AI-powered tool that leverages the GROQ API and Mixtral 8x7B model to analyze legal contracts. This project demonstrates the application of large language models in the legal domain, providing automated analysis, summary, and insights for contract documents.

## Table of Contents

- [Features](#features)
- [Technical Stack](#technical-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## Features

- **Document Ingestion**: Supports PDF and DOCX file formats for contract uploads.
- **AI-Powered Analysis**: Utilizes the GROQ API with the Mixtral 8x7B model for in-depth contract analysis.
- **Key Clause Identification**: Automatically identifies and categorizes important clauses within the contract.
- **Summary Generation**: Provides a concise summary of the entire contract.
- **Risk Assessment**: Highlights potential issues or risks associated with specific clauses.
- **Interactive Q&A**: Allows users to ask follow-up questions about the analyzed contract.
- **User-Friendly Interface**: Built with Streamlit for an intuitive and responsive web application.

## Technical Stack

- **Python**: Core programming language
- **Streamlit**: Web application framework
- **GROQ API**: AI model integration
- **PyPDF2 & python-docx**: Document processing
- **python-dotenv**: Environment variable management

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smart-contract-analyzer.git
   cd smart-contract-analyzer
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your GROQ API key:
   - Create a `.env` file in the root directory
   - Add your GROQ API key to the file:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

## Usage

1. Start the Streamlit app:
   ```bash
   streamlit run main.py
   ```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Upload a contract document (PDF or DOCX) using the file uploader.

4. The app will process the document and display:
   - A summary of the contract
   - Identified key clauses with analysis
   - An overall assessment of the contract

5. Use the "Ask a Follow-up Question" feature to get more specific information about the contract.

## Configuration

The app uses environment variables for configuration. You can modify the following in your `.env` file:

- `GROQ_API_KEY`: Your GROQ API key (required)

## Future Enhancements

- Integration with additional AI models for comparative analysis
- Support for more document formats
- Enhanced data visualization for contract analysis results
- Batch processing capabilities for multiple contracts

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Disclaimer

This tool is for informational purposes only and should not be considered as legal advice. Always consult with a qualified legal professional for contract-related matters. The analysis provided by this tool is based on AI predictions and may not be 100% accurate or complete.

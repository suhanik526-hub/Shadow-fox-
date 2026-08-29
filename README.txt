
AI STUDENT UTILITY
==================

Project: AI Student Note Summarizer

DESCRIPTION
-----------
AI Student Utility is a simple AI-powered student application that
converts study notes into a clear and easy-to-revise summary.

The application uses an LLM API and a structured prompt to generate
concise summaries from student-provided notes.

FEATURES
--------
1. Simple and usable interface
2. Text input for study notes
3. AI-powered note summarization
4. Structured prompt-based generation
5. Empty input validation
6. API error handling
7. Readable AI-generated output

REQUIREMENTS
------------
- Python 3.x
- Internet connection
- A Groq API key

INSTALLATION
------------
1. Open a terminal in the project folder.

2. Install the required packages:

   pip install -r requirements.txt

RUN THE APPLICATION
-------------------
Run:

   streamlit run app.py

The application will open in the browser.

API KEY
-------
The application asks the user for a Groq API key.

Create your own API key from the Groq Console:
https://console.groq.com/

Do not share or publish the API key.

USAGE
-----
1. Enter your Groq API key.
2. Paste your study notes into the text box.
3. Click "Summarize Notes".
4. The AI-generated summary will appear below.

PROMPT DESIGN
-------------
The application uses a system instruction that tells the AI to:

- Act as a student study assistant
- Summarize the provided notes
- Use simple language
- Use bullet points
- Keep only important information

ERROR HANDLING
--------------
The application checks whether:
- An API key has been entered
- Study notes have been entered
- The API request succeeds

If an error occurs, a user-friendly error message is displayed.

TECHNOLOGY
----------
Python
Streamlit
Groq API
Large Language Model

PROJECT PURPOSE
---------------
The project demonstrates how an LLM API can be integrated into
a practical student-focused application rather than being used
only as a generic chatbot.

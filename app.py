
import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="AI Student Utility",
    page_icon="📚"
)

st.title("📚 AI Student Utility")
st.write("Turn your study notes into a clear, easy-to-revise summary.")

api_key = st.text_input(
    "Enter your Groq API key",
    type="password"
)

notes = st.text_area(
    "Paste your study notes here:",
    height=250,
    placeholder="Example: Photosynthesis is the process by which plants..."
)

if st.button("✨ Summarize Notes"):

    if not api_key:
        st.error("Please enter your Groq API key.")

    elif not notes.strip():
        st.warning("Please enter some study notes first.")

    else:
        try:
            client = Groq(api_key=api_key)

            with st.spinner("Generating summary..."):
                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a helpful AI study assistant. "
                                "Summarize student notes clearly and concisely. "
                                "Use simple language and bullet points. "
                                "Keep only the important information."
                            )
                        },
                        {
                            "role": "user",
                            "content": notes
                        }
                    ]
                )

            st.subheader("📝 Summary")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error("Something went wrong while contacting the AI API.")
            st.caption(str(e))
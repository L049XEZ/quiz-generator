import streamlit as st
import json
import os
import re
from dotenv import load_dotenv

# === Load environment variables ===
load_dotenv()
from google import generativeai as genai

# === Configure Gemini API key ===
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")


# === Gemini question generation ===
def fetch_questions(text_content, quiz_level):
    RESPONSE_JSON = {
        "mcqs": [
            {
                "mcq": "Sample question?",
                "options": {
                    "a": "Option A",
                    "b": "Option B",
                    "c": "Option C",
                    "d": "Option D",
                },
                "correct": "a",
            }
        ]
    }

    PROMPT_TEMPLATE = """
    Text: {text_content}
    You are an expert in generating MCQ type quizzes based on the provided content. 
    Given the above text, create a quiz of 3 multiple choice questions keeping difficulty level as {quiz_level}.
    Format your response EXACTLY like the RESPONSE_JSON below.
    Do not include any explanation, markdown, or text outside JSON.
    RESPONSE_JSON example:
    {RESPONSE_JSON}
    """

    formatted_template = PROMPT_TEMPLATE.format(
        text_content=text_content,
        quiz_level=quiz_level,
        RESPONSE_JSON=RESPONSE_JSON,
    )

    response = model.generate_content(
        formatted_template,
        generation_config={"response_mime_type": "application/json"},
    )

    extracted_response = response.text or ""
    print("🧩 Gemini raw output:\n", extracted_response)

    # === Safe JSON parsing ===
    try:
        return json.loads(extracted_response).get("mcqs", [])
    except json.JSONDecodeError:
        try:
            cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", extracted_response.strip(), flags=re.IGNORECASE)
            json_start = cleaned.find("{")
            json_end = cleaned.rfind("}") + 1
            cleaned = cleaned[json_start:json_end]
            data = json.loads(cleaned)
            return data.get("mcqs", [])
        except Exception as e:
            print("⚠️ JSON parsing failed:", e)
            st.error("❌ Failed to parse Gemini response. Please try again.")
            return []


# === Streamlit UI ===
def main():
    st.title("Quiz Generator App 🚀")

    # Initialize session state
    if "questions" not in st.session_state:
        st.session_state.questions = []
    if "selected_options" not in st.session_state:
        st.session_state.selected_options = []

    # Input
    text_content = st.text_area("Paste the text content here:")
    quiz_level = st.selectbox("Select quiz level:", ["Easy", "Medium", "Hard"]).lower()

    # Generate Quiz
    if st.button("Generate Quiz"):
        st.session_state.questions = fetch_questions(text_content, quiz_level)
        st.session_state.selected_options = [None] * len(st.session_state.questions)

    questions = st.session_state.questions

    if questions:
        st.header("Quiz Questions:")
        for i, question in enumerate(questions):
            options = list(question["options"].values())
            selected_option = st.radio(
                question["mcq"],
                options,
                index=(
                    options.index(st.session_state.selected_options[i])
                    if st.session_state.selected_options[i] in options
                    else None
                ),
                key=f"q{i}",
            )
            st.session_state.selected_options[i] = selected_option

        if st.button("Submit"):
            marks = 0
            st.header("Quiz Result:")
            for i, question in enumerate(questions):
                selected_option = st.session_state.selected_options[i]
                correct_option = question["options"][question["correct"]]
                st.subheader(f"{question['mcq']}")
                st.write(f"You selected: {selected_option}")
                st.write(f"Correct answer: {correct_option}")
                if selected_option == correct_option:
                    marks += 1
            st.success(f"You scored {marks} out of {len(questions)} ✅")


if __name__ == "__main__":
    main()

# 🧠 Quiz Generator App (Google Gemini + Streamlit)

A simple and interactive **AI-powered quiz generator** built using **Google Gemini API** and **Streamlit**.  
This app allows users to paste any text, choose a difficulty level, and automatically generate **multiple-choice questions (MCQs)** based on the provided content.

---

## 🚀 Features

- 🧾 **Automatic Quiz Generation:** Generates MCQs from any input text.
- 🤖 **Powered by Google Gemini API:** Uses Gemini's text generation model (`gemini-2.5-flash`) for intelligent question creation.
- 🧩 **Interactive Interface:** Built with Streamlit for easy use and real-time quiz feedback.
- 🔒 **Secure API Key Handling:** Uses `.env` file and `python-dotenv` to manage API credentials.
- 📊 **Instant Scoring:** Users can answer questions and see their results instantly.

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| Frontend UI | Streamlit |
| Backend Logic | Python |
| AI Model | Google Gemini (`gemini-2.5-flash`) |
| Environment Variables | python-dotenv |
| JSON Handling | Built-in Python JSON |
| Hosting | Local / Streamlit Cloud (optional) |

---

## 🧰 Installation & Setup

### 1️⃣ Clone this repository
```bash
git clone https://github.com/L049XEZ/quiz-generator.git
cd quiz-generator
```

### 2️⃣ Create a virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate     # (Windows)
# or
source venv/bin/activate  # (macOS/Linux)
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Create your .env file
Create a new file named .env in the project root, then add your Google Gemini API key:
```bash
GOOGLE_API_KEY=your_google_gemini_api_key_here
(You can get your key from Google AI Studio)
```

### ▶️ Running the App
Launch the Streamlit app:
```bash
streamlit run quizapp.py
```

Then open the URL shown in your terminal.

### 🧩 How It Works

Paste your text (e.g., notes, articles, or slides content).

Choose difficulty level — Easy / Medium / Hard.

The app sends your text to Gemini API to generate MCQs in structured JSON format.

Streamlit displays interactive quiz questions with options and scoring.

### 🪄 Future Improvements

Add file upload support (PDF/Docx → Quiz)

Enable question export (to CSV / JSON / Google Forms)

Add user leaderboard and progress tracking

### ❤️ Author

Low Yvonne

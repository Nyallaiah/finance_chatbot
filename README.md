💰 Personal Finance Advisor Chatbot

🚀 An AI-powered Personal Finance Chatbot that analyzes your expense data (CSV/Excel) and answers natural language questions like:

“Where did I spend the most in February?”

“Give me savings recommendations.”

✅ No API Key required → Runs fully locally using Hugging Face FLAN-T5 (transformers pipeline).
✅ Interactive Dashboard → Built with Streamlit.
✅ Backend → Flask API for query processing.
✅ Deployment Ready → Docker + GitHub + Render/Streamlit Cloud.

📂 Project Structure
finance_chatbot/
├── backend/
│   └── app.py              # Flask backend
├── frontend/
│   └── app.py              # Streamlit frontend
├── data/
│   └── sample_expenses.csv # Sample dataset
├── models/
│   ├── preprocess.py       # Data preprocessing
│   └── agent.py            # Local Hugging Face model + rules
├── logs/
│   └── queries.log         # Logs queries & responses
├── Dockerfile              # For containerization
├── README.md               # Documentation

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/<your-username>/finance_chatbot.git
cd finance_chatbot

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt


📂 requirements.txt (create this file)

flask
pandas
streamlit
matplotlib
requests
transformers

🚀 Run Locally
1️⃣ Start Flask Backend
cd backend
python app.py


Backend runs at → http://127.0.0.1:5000/ask

2️⃣ Start Streamlit Frontend
cd frontend
streamlit run app.py


Frontend runs at → http://localhost:8501

🧪 Example Queries

Upload data/sample_expenses.csv

Ask:

“Where did I spend the most?”

“What is my total spending?”

“Give me a savings recommendation.”

📊 Dashboard Preview

👉 Expense distribution is automatically shown as a bar chart.

🐳 Docker Deployment
Build Image
docker build -t finance_chatbot .

Run Container
docker run -p 8501:8501 -p 5000:5000 finance_chatbot

☁️ Free Cloud Deployment

Render → Deploy backend + frontend with Docker

Streamlit Cloud → Deploy frontend, connect to backend API

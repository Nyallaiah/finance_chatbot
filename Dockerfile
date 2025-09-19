FROM python:3.10-slim

WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask pandas streamlit matplotlib requests transformers

# Expose both Flask (5000) and Streamlit (8501) ports
EXPOSE 5000
EXPOSE 8501

# Start backend + frontend
CMD ["sh", "-c", "python backend/app.py & streamlit run frontend/app.py --server.port=8501 --server.address=0.0.0.0"]

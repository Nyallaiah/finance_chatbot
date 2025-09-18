from flask import Flask, request, jsonify
import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent

from models.agent import get_agent_response
from models.preprocess import clean_csv

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.json
        query = data.get("query")
        file_path = data.get("file_path", "../data/sample_expenses.csv")
        df = clean_csv(file_path)
        response = get_agent_response(df, query)

        with open("../logs/queries.log", "a") as f:
            f.write(f"Query: {query} | Response: {response}\n")

        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)

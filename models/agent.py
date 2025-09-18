import pandas as pd
from transformers import pipeline

qa_model = pipeline("text2text-generation", model="google/flan-t5-small")

def get_agent_response(df: pd.DataFrame, query: str) -> str:
    """
    Basic rule-based + LLM response without needing API key.

    """
    query_lower = query.lower()

    if "spend" in query_lower and "most" in query_lower:
        totals = df.groupby("Category")["Amount"].sum()
        top_cat = totals.idxmax()
        return f"You spent the most on {top_cat} (${totals.max()})."

    elif "savings" in query_lower:
        total_spent = df["Amount"].sum()
        suggestion = "try reducing food/entertainment expenses." if "Food" in df["Category"].values else "Review monthly subscriptions."
        return f"Your total spending is ${total_spent}. Suggestion: {suggestion}"

    else:
        prompt = f"Answer the following based on user expenses:\n\n{query}"
        response = qa_model(prompt, max_length= 128, do_sample=False)
        return response[0]["generated_text"]
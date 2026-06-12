import os
from news_fetcher import get_news
from ai_analyzer import analyze_article
from report_builder import build_report
from mailer import send_email
from clients_config import CLIENTS

# Env vars
GRAPH_TOKEN = os.getenv("GRAPH_TOKEN")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from openai import OpenAI
client_oa = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else OpenAI()

def main():
    full_report = "Weekly Client Insights

"
    for client in CLIENTS:
        articles = get_news(client["name"])
        analyses = []
        for art in articles:
            try:
                analysis = analyze_article(client["name"], client["sector"], art)
            except Exception as e:
                analysis = str(e)
            analyses.append(analysis)
        talking_points = ""
        section = build_report(client, analyses, articles, talking_points)
        full_report += section + "
"
    if GRAPH_TOKEN and RECIPIENT_EMAIL:
        send_email(GRAPH_TOKEN, full_report, RECIPIENT_EMAIL)
    else:
        print("GRAPH_TOKEN or RECIPIENT_EMAIL not set. Skipping email send.")

if __name__ == "__main__":
    main()

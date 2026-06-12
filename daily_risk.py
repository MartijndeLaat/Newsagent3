import os
from news_fetcher import get_news
from risk_engine import is_high_risk
from mailer import send_email
from clients_config import CLIENTS

# Env vars
GRAPH_TOKEN = os.getenv("GRAPH_TOKEN")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

def main():
    for client in CLIENTS:
        articles = get_news(client["name"])
        for art in articles:
            if is_high_risk(art["title"] + art["summary"]):
                content = f"""
RISICO ALERT

Client: {client['name']}

{art['title']}

{art['link']}
"""
                if GRAPH_TOKEN and RECIPIENT_EMAIL:
                    send_email(GRAPH_TOKEN, content, RECIPIENT_EMAIL)
                else:
                    print("GRAPH_TOKEN or RECIPIENT_EMAIL not set. Cannot send risk alert.")

if __name__ == "__main__":
    main()

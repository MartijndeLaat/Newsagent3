import feedparser

def get_news(client_name):
    query = client_name.replace(" ", "+")
    url = f"https://news.google.com/rss/search?q={query}+zorg&hl=nl&gl=NL&ceid=NL:nl"
    feed = feedparser.parse(url)
    articles = []
    for entry in feed.entries[:5]:
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "summary": entry.summary
        })
    return articles

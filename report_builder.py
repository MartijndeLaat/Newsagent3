def build_report(client, analyses, articles, talking_points):
    text = f"\nCLIENT: {client['name']} ({client['sector']})\n\n"

    text += "Key insights:\n"
    for a in analyses:
        text += f"- {a}\n"

    text += "\nTalking points:\n"
    text += talking_points + "\n"

    text += "\nArticles:\n"
    for art in articles:
        text += f"- {art['title']}\n  {art['link']}\n"

    return text


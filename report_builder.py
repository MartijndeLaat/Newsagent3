def build_report(client, analyses, articles, talking_points):
    text = f"
CLIENT: {client['name']} ({client['sector']})

"
    text += "Key insights:
"
    for a in analyses:
        text += f"- {a}
"
    text += "
Talking points:
"
    text += talking_points + "
"
    text += "
Articles:
"
    for art in articles:
        text += f"- {art['title']}
  {art['link']}
"
    return text

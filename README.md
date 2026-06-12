# News Agent (GitHub Actions Version)

This repository contains a fully autonomous news agent that:

- Fetches news using Google News RSS feeds
- Analyzes articles with OpenAI GPT-5
- Detects high-risk events
- Sends weekly reports and risk alerts via Microsoft Graph Outlook emails
- Scheduled using GitHub Actions workflows

## Setup

Add the following secrets to your GitHub repository:

- `GRAPH_TOKEN`: Microsoft Graph API OAuth 2.0 Bearer token
- `RECIPIENT_EMAIL`: The email address to send reports to
- `OPENAI_API_KEY`: Your OpenAI API key

## Files
- `clients_config.py`: List of clients with sectors
- `news_fetcher.py`: Fetches Google News RSS articles
- `ai_analyzer.py`: Calls OpenAI GPT-5 for article analysis
- `risk_engine.py`: Simple risk detection by keywords
- `report_builder.py`: Constructs the weekly report
- `mailer.py`: Sends email via Microsoft Graph API
- `weekly_report.py`: Runner for weekly report
- `daily_risk.py`: Runner for daily risk alerts
- `.github/workflows/weekly.yml`: GitHub Actions schedule for weekly run
- `.github/workflows/daily.yml`: GitHub Actions schedule for daily run
- `requirements.txt`: Required Python packages

## Usage

The weekly report will run every Friday at 08:00 NL time (06:00 UTC).  
The daily risk alert will run every day at 07:30 NL time (05:30 UTC).

Set the environment secrets and push to GitHub. The workflows will trigger automatically.

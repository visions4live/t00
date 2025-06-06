# Drug Info Web App

This Flask application provides basic information about drug-related crime rates,
deaths from drug abuse, and fetches recent news articles related to drugs in the
United States. Users can post updates that are stored locally in `data.json`.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. (Optional) Set a `NEWS_API_KEY` environment variable to fetch headlines from
   [NewsAPI.org](https://newsapi.org/).
3. Run the server:
   ```bash
   python run.py
   ```

## Endpoints

- `GET /api/data` – Get stored statistics and updates.
- `POST /api/data` – Post JSON `{ "update": "text" }` to append an update.
- `GET /api/news` – Fetch current news headlines about drugs.

This project is a simple example and does not include persistent storage or
authentication. It is intended as a demo for updating and retrieving recent
information about drug crime and abuse in the US.

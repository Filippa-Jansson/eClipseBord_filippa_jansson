FROM python:3.11-slim

COPY frontend/ /app/

RUN pip install --no-cache-dir uv

WORKDIR /app

RUN uv sync --no-dev

WORKDIR /app/src/frontend

CMD ["uv", "run", "streamlit", "run","dashboard.py", "--host", "0.0.0.0"]

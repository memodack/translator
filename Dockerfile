FROM python:3.12.3-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONDONTWRITEBYTECODE=1
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
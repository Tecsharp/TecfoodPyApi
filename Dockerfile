FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 1001

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:1001", "app:app"]

FROM python:3.11

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Add cron
RUN apt-get update && apt-get install -y cron

COPY train_cron /etc/cron.d/train_cron
RUN chmod 0644 /etc/cron.d/train_cron
RUN crontab /etc/cron.d/train_cron

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]

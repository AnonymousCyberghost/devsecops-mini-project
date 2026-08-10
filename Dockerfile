FROM python:3.12-alpine
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
USER 1000
CMD ["python", "app.py"]

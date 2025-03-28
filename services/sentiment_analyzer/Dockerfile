FROM python:3.12
WORKDIR /app
COPY analyzer.py .
RUN pip install textblob
CMD ["python", "analyzer.py"]
FROM python:3.9-slim
RUN pip install requests
WORKDIR /app
COPY deepstack_process.py .
CMD ["python3", "deepstack_process.py"]


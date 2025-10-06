FROM ubuntu:22.04
RUN apt update && apt install -y python3 python3-pip libreoffice
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]

# Base image
FROM python:3.7-slim

# install python 
RUN apt update && \
apt install --no-install-recommends -y build-essential gcc && \
apt clean && rm -rf /var/lib/apt/lists/*

COPY samy_mlops/requirements.txt samy_mlops/requirements.txt
COPY samy_mlops/setup.py samy_mlops/setup.py
COPY samy_mlops/src/ samy_mlops/src/
COPY samy_mlops/data/ samy_mlops/data/

WORKDIR /samy_mlops
RUN pip install -r requirements.txt --no-cache-dir

ENTRYPOINT ["python", "-u", "src/models/train_model.py"]

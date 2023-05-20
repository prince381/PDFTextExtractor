FROM ubuntu:18.04

# Path: /app
WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get clean \
&& apt-get update \
&& apt-get -y install tesseract-ocr \
&& apt-get install -y python3 python3-distutils python3-pip \
&& cd /usr/local/bin \
&& ln -s /usr/bin/python3 python \
&& pip3 --no-cache-dir install --upgrade pip \
&& rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file to the container
COPY . /app

# Install the requirements
RUN pip install PyPDF2
RUN pip install pytesseract
RUN pip install flask
RUN pip install gunicorn

# Run the application
CMD ["python", "app.py"]

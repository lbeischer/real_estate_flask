# Use base Alpine image of Python
FROM python:3.8.1-alpine

# Set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Add and install requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Add app
COPY . .

# Run server
CMD python manage.py run -h 0.docker0.0.0

docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' 71dbca348d9c

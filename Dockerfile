# FROM python:3.6
#
# # RUN pip install virtualenv
# # ENV VIRTUAL_ENV=/venv
# # RUN virtualenv venv -p python3
# # ENV PATH="VIRTUAL_ENV/bin:$PATH"
#
# WORKDIR /app
# # ADD . /app
#
# # Install dependencies
# COPY requirements.txt .
# RUN pip install -r requirements.txt
# COPY . .
#
# # Expose port
# # Expose 5000
#
# # Run the application
# CMD ["python", "app.py"]

FROM python:3.6-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app/app.py"]
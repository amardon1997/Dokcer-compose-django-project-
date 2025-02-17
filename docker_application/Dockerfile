# FROM python:3.10-slim

# WORKDIR /app

# COPY . /app

# RUN pip install --upgrade pip

# RUN pip install --upgrade setuptools wheel

# RUN pip3 install -r requirement.txt

# RUN python manage.py makemigrations

# RUN python manage.py migrate


# CMD ["python3", "manage.py", "runserver" , "0.0.0.0:8000"]


FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install system dependencies required for mysqlclient
# Install system dependencies required for mysqlclient
RUN apt-get update && apt-get install -y \
    build-essential \
    libmariadb-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install dependencies
RUN pip install --upgrade pip setuptools wheel \
    && pip install -r requirement.txt

# # Run migrations
# RUN python3 manage.py makemigrations \
#     && python3 manage.py migrate

# Expose port 8000
EXPOSE 8000

# Command to run the Django development server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

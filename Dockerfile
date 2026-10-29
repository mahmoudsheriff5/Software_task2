# Use an official lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all repository files to the working directory
COPY . /app

# Command to execute the application
CMD ["python", "main.py"]

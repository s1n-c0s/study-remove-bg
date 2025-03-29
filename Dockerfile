# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY requirements.txt .
COPY remove_bg.py .
COPY index.html .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 8080

# Run the Flask app
CMD ["python", "remove_bg.py"]
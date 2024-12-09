FROM python:3.12-slim-bookworm

WORKDIR /app

# Copy and install requirements using uv
COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8080

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
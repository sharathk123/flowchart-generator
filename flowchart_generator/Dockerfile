
# Use an official Python runtime as a parent image for backend
FROM python:3.9-slim AS backend

# Set the working directory in the container for backend
WORKDIR /app

# Install backend dependencies
COPY backend/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code into the container
COPY backend/ /app/backend/

# Expose the port the backend app runs on
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]

# Use an official Node.js runtime as a parent image for frontend
FROM node:16 AS frontend

# Set the working directory in the container for frontend
WORKDIR /app/frontend

# Install frontend dependencies
COPY frontend/package.json /app/frontend/
RUN npm install

# Copy the frontend code into the container
COPY frontend/ /app/frontend/

# Expose the port the frontend app runs on
EXPOSE 3000

# Command to run the React app
CMD ["npm", "start"]

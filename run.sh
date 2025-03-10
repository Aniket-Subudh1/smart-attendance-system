#!/bin/bash

# Start all services using Docker Compose
echo "Starting all services with Docker Compose..."
docker-compose up -d

echo "Services started!"
echo "API: http://localhost:8000"
echo "Frontend: http://localhost:3000"

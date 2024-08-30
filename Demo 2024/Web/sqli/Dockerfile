# Gunakan image Python sebagai base image
FROM python:3.9-alpine

# Instal dependencies
RUN apk add --no-cache gcc musl-dev sqlite

# Set working directory
WORKDIR /app

# Salin requirements dan source code
COPY src/ /app/

# Install Flask
RUN pip install flask

# Ekspose port 5000
EXPOSE 5000

# Jalankan aplikasi
CMD ["python", "app.py"]

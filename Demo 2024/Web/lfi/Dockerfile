# Gunakan image Python sebagai base image
FROM python:3.9-alpine

# Instal dependencies
RUN apk add --no-cache gcc musl-dev sqlite

# Set working directory
WORKDIR /app

# Salin requirements dan source code
COPY . /app/

# Install Flask and Move flag.txt to root folder
RUN pip install flask && mv flag.txt /

# Ekspose port 5000
EXPOSE 2567

# Jalankan aplikasi
CMD ["python", "app.py"]

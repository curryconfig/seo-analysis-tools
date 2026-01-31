# Pake image python yang stabil
FROM python:3.9-slim

# Install Chrome dan dependencies-nya
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Set variabel lingkungan biar Selenium tau lokasi Chrome
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Set direktori kerja
WORKDIR /app

# Copy semua file dari GitHub ke server Railway
COPY . .

# Install library selenium
RUN pip install --no-cache-dir selenium

# Perintah buat jalanin bot
CMD ["python", "goblok.py"]

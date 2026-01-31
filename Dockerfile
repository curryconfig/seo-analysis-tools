FROM python:3.9

# Install Chrome & Driver
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

# Install Library
RUN pip install --no-cache-dir selenium

# Hugging Face butuh akses ke port 7860, biarin aja kosong yang penting ada
EXPOSE 7860

# Jalankan bot
CMD ["python", "goblok.py"]

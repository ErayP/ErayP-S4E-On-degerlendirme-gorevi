# Dockerfile (proje kökünde, boş olmadığından emin olun)
FROM python:3.11-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Bağımlılıkları kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Uygulama kodunu kopyala
COPY app ./app

# Uvicorn’un dinleyeceği port
EXPOSE 8000

# Container başladığında çalışacak komut
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

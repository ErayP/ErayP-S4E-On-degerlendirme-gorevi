# Yapay Zekâ Destekli Kod Üretici Asistan

**FastAPI**, **Ollama** (yerel LLM) ve **Helm** kullanarak hazırlanmış; kullanıcıdan alınan “prompt”’a göre Python kodu ve kısa bir başlık üreten basit bir web uygulamasıdır. Hem yerelde `uvicorn` ile çalıştırabilir, hem Docker/Kubernetes/Helm ile ölçekleyebilirsin.

---

## Özellikler

- **Prompt → Kod**: Kullanıcının girdiği doğal dil prompt’unu alır  
- **Başlık**: Üretilen kodu özetleyen kısa, anlamlı bir başlık döner  
- **Web UI**: FastAPI + tek sayfalık HTML/CSS arayüz  
- **Yerel LLM**: Ollama + `llama3:latest` modeli  
- **Containerize**: Dockerfile hazır  
- **Kubernetes + Helm**: Helm chart’ı ile tek komut deploy  

---

## Gereksinimler

- Python 3.11+  
- [Ollama](https://ollama.com) (ve indirilmiş `llama3:latest` modeli)  
- Docker (isteğe bağlı)  
- Minikube ve Helm (Kubernetes üzerine deploy için)  

---

##  Hızlı Başlangıç

### 1. Projeyi klonlayın

```bash
git clone https://github.com/<KULLANICI_ADIN>/<REPO_ADIN>.git
cd <REPO_ADIN>
2. Python ortamını hazırlayın
bash
Kopyala
Düzenle
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt
3. Ollama modelini çekin
bash
Kopyala
Düzenle
ollama pull llama3:latest
4. Ortam değişkenleri
bash
Kopyala
Düzenle
export OLLAMA_URL="http://localhost:11434"
export OLLAMA_MODEL="llama3:latest"
# Windows PowerShell:
#  $Env:OLLAMA_URL="http://localhost:11434"
#  $Env:OLLAMA_MODEL="llama3:latest"
5. Uygulamayı çalıştırın
bash
Kopyala
Düzenle
uvicorn app.main:app --reload
Tarayıcıda aç: http://127.0.0.1:8000

 Docker ile Çalıştırma
İmajı oluşturun:

bash
Kopyala
Düzenle
docker build -t <DOCKERHUB_KULLANICI_ADIN>/llm-code-generator:latest .
İmajı push’layın:

bash
Kopyala
Düzenle
docker push <DOCKERHUB_KULLANICI_ADIN>/llm-code-generator:latest
Container’ı çalıştırın:

bash
Kopyala
Düzenle
docker run -d -p 8000:8000 \
  -e OLLAMA_URL="http://host.docker.internal:11434" \
  -e OLLAMA_MODEL="llama3:latest" \
  <DOCKERHUB_KULLANICI_ADIN>/llm-code-generator:latest
UI’ye gidin: http://localhost:8000

 Kubernetes + Helm ile Deploy
Minikube’u başlatın:

bash
Kopyala
Düzenle
minikube start
Helm chart dizinine gidin:

bash
Kopyala
Düzenle
cd helm/llm-code-generator
Chart’ı yükleyin:

bash
Kopyala
Düzenle
helm install my-llm-code-generator .
Servis URL’sini alın:

bash
Kopyala
Düzenle
minikube service my-llm-code-generator --url
Tarayıcıda açın ve prompt girip “Üret”e tıklayın.

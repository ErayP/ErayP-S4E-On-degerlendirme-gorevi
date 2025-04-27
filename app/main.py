from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.schemas import CodeRequest, CodeResponse
from app.ollama_client import generate_code

app = FastAPI(
    title="Yapay Zeka Destekli Kod Üretici Asistan",
    description="Kullanıcının prompt'una göre Python kodu ve başlık üretir",
    version="1.0.0"
)



# ── Anasayfa olarak index.html dönen GET endpoint ──
@app.get("/", response_class=HTMLResponse)
async def root():
    with open("app/static/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())

@app.post("/generate", response_model=CodeResponse)
def generate(request: CodeRequest):
    """
    Kullanıcıdan gelen prompt'u alır, Ollama ile kod ve başlık üretir.
    """
    try:
        result = generate_code(request.prompt)
        return CodeResponse(title=result["title"], code=result["code"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

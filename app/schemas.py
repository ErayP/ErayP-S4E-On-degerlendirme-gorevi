from pydantic import BaseModel

class CodeRequest(BaseModel):
    prompt: str

class CodeResponse(BaseModel):
    title: str
    code: str

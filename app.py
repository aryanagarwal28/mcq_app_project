from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from pathlib import Path
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return Path("app/templates/index.html").read_text()

@app.post("/generate/")
async def generate_data(url: str = Form(None), file: UploadFile = File(None)):
    if url:
        content = fetch_url_content(url)
    elif file:
        content = await file.read()
    else:
        return {"error": "No valid input provided"}

    # Simulating LLM output
    generated_output = f"Processed content from: {url or file.filename}"
    return {"output": generated_output}

def fetch_url_content(url: str) -> str:
    # Implement URL fetching logic
    return f"Content from {url}"

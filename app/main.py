from fastapi import FastAPI

app = FastAPI(title="Mini crm")

@app.get("/health")
def health():
    return {"status":"ok"}
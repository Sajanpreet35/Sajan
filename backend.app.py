from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

from llm.llm_brain import ask_llm
from collectors.run_all import run_all_collectors

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("question","")
    answer = ask_llm(question)
    return JSONResponse({"answer": answer})

@app.get("/update_knowledge")
async def update_knowledge():
    run_all_collectors()
    return {"status":"Knowledge updated"}

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

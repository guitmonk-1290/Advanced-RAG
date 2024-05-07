from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional
from llama_query_pipeline import QueryExecutor

app = FastAPI()

class InputText(BaseModel):
  inputText: str

@app.get("/")
async def base():
  return {"status": 200}

@app.post("/process-text", response_model=dict, status_code=200)
async def process_text(text: InputText = Body(...)):
  try:
    query_executor = QueryExecutor(llm_type="ollama", db_config={
        "host": "127.0.0.1",
        "user": "arinxd",
        "password": "eatdatass",
        "database": "spectra"
    })
    query_executor.setup_query_pipeline()
    sql_query, response, data = query_executor.run_query(text.inputText)
    return {"SQLQuery": sql_query, "response" : response, "data" : data}
  except Exception as e:
    return {"error": str(e)}, 500

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=5000)

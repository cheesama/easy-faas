from fastapi import Request, FastAPI

import json
import logging

app = FastAPI()

@app.get("/")
async def health_check():
    return {"status": "alive"}

#@app.post("/test-func")
#async def handler(req: Request):
#    return await req.body()


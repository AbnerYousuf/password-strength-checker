from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel #simplifies handling requests
import zxcvbn #api for checking the pw strength

app = FastAPI()

# this block is for communicating with the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # this is the vite dev server address
    #so all requests are allowed from it
    allow_credentials=True,
    allow_methods=["*"], #allow all methods (get/post)
    allow_headers=["*"], #allow all headers
)

class PasswordRequest(BaseModel):
    password: str

@app.post("/print")
async def print_password(request: PasswordRequest):
    print(f"Received password: {request.password}")
    return {"message": f"printed: {request.password}"}
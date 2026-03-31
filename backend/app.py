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


@app.post("/audit")
async def audit_password(request: PasswordRequest):
    if not request.password:
        return {"error": "Password is required."}
    result = zxcvbn.zxcvbn(request.password)
    #our password cracking api
    return {
        "score": result["score"],
        "guesses": result["guesses"],
        "feedback": result["feedback"],
        "crack_times_display": result["crack_times_display"]
        #dissects the output into readable lines
    }


#this was for testing, im keeping it just in case
#will remove once we have a final product
#@app.post("/print")
#async def print_password(request: PasswordRequest):
#    print(f"Received password: {request.password}")
#    return {"message": f"printed: {request.password}"}
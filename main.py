from fastapi import FastAPI
from posts.router import router as posts_router 
from database import database
from dotenv import load_dotenv
load_dotenv() 
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(posts_router, prefix="/posts", tags=["Posts"])



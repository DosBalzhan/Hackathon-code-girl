from posts.schemas import CreatePostRequest, EditPostRequest, GenerationRequest
from fastapi import HTTPException, APIRouter
from posts import service 
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import time 
import requests
import os

router = APIRouter()

@router.get('')

async def get_posts():
   return await service.get_posts()

@router.post('')
async def create_post(post: CreatePostRequest):
    return await service.create_post(post)



@router.get('/{id}')
async def get_post(id: int):
     return await service.get_post_by_id(id)


@router.put('/{id}')
async def edit_post(id: int, post_data: EditPostRequest):
    return await service.edit_post(id,post_data)



@router.delete('/{id}')
async def delete_post(id: int):
    await service.delete_post(id)
    
    return {"message":"ok,deleted"}


@router.post('/generate-ad-text')
async def generate_post(post:GenerationRequest):
    token = os.environ.get("TOKEN")

    headers = {
        'Authorization': f"Bearer {token}"
    }

    response = requests.post('https://7583-185-48-148-173.ngrok-free.app/advertisement', headers=headers, json={
        "input_text": post.keywords
    })

    body = response.json()
    return {
        "text": body['output']
    }




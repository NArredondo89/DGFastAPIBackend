import os
from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from database import engine
from fastapi.middleware.cors import CORSMiddleware
from src import models, routes, auth, api
import uvicorn

 
app = FastAPI()

security = HTTPBasic()



models.course.Base.metadata.create_all(engine)
models.event.Base.metadata.create_all(engine)
models.hole.Base.metadata.create_all(engine)
models.layout.Base.metadata.create_all(engine)
models.playdate.Base.metadata.create_all(engine)
models.review.Base.metadata.create_all(engine)
models.route.Base.metadata.create_all(engine)
models.user.Base.metadata.create_all(engine)


app.include_router(auth.auth.router)
app.include_router(routes.course.router)
app.include_router(routes.event.router)
app.include_router(routes.hole.router)
app.include_router(routes.layout.router)
app.include_router(routes.playdate.router)
app.include_router(routes.review.router)
app.include_router(routes.user.router)


origins = [ 
    'http://localhost:3000',
] 
    

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

@ app.get('/', include_in_schema=False)
async def index():
    return RedirectResponse(url='/docs')

load_dotenv()
if __name__ == '__main__':
    uvicorn.run('__main__:app', host='http://127.0.0.1', port=int(
        os.environ.get("API_PORT")), reload=True)


@app.get("/users/me")
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    return {"username": credentials.username, "password": credentials.password}
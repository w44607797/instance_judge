from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def print_hi(name):

    print(f'Hi, {name}')





if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=6001)

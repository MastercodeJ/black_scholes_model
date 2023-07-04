from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import math
from scipy.stats import norm
from functions import black_scholes
from database.database import engine, SessionLocal


from model import models
models.Base.metadata.create_all(bind= engine)


app = FastAPI()

origins = ['https://localhost:3000']
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"]
)

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    return {'Ping': "Pong"}

@app.get("/123")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate/call")
def calculate_option_price(request: Request, S: float = Form(...), X: float = Form(...), r: float = Form(...), sigma: float = Form(...), T: float = Form(...)):
    call_price = black_scholes.black_scholes_call(S, X, r, T,sigma)
    print(call_price)
    return templates.TemplateResponse("call_result.html", {"request": request, "call_price": call_price})


@app.post("/calculate/put")
def calculate_option_price(request: Request, S: float = Form(...), X: float = Form(...), r: float = Form(...), sigma: float = Form(...), T: float = Form(...)):
    put_price = black_scholes.black_scholes_put(S, X, r, T,sigma)
    return templates.TemplateResponse("put_result.html", {"request": request, "call_price": put_price})

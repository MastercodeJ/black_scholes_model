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
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate/call")
def calculate_option_price(request: Request, X: float = Form(...), T: float = Form(...),  ticker: str = Form(...)):
    print(X, T, ticker, 'sdfsdf')
    call_price, price, Strike_price, risk_free_rate, time_to_maturity, sigma,  = black_scholes.black_scholes_call( X, T, ticker)
    return templates.TemplateResponse("call_result.html", {"request": request, "call_price": call_price, "price": price, "Strike_price":Strike_price, "risk_free_rate": round(risk_free_rate,2)*100, "time_to_maturity": time_to_maturity, "sigma": round(sigma, 2)*100, 'ticker': ticker})


@app.post("/calculate/put")
def calculate_option_price(request: Request, X: float = Form(...),  T: float = Form(...), ticker: str = Form(...)):
    put_price, price, Strike_price, risk_free_rate, time_to_maturity, sigma = black_scholes.black_scholes_put( X, T, ticker)
    return templates.TemplateResponse("put_result.html", {"request": request, "call_price": put_price, "price": price, "Strike_price":Strike_price, "risk_free_rate": round(risk_free_rate,2)*100, "time_to_maturity": time_to_maturity, "sigma": round(sigma, 2)*100, 'ticker': ticker})

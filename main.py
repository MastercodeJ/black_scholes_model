from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import math
from scipy.stats import norm

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/123")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate")
def calculate_option_price(request: Request, S: float = Form(...), X: float = Form(...), r: float = Form(...), sigma: float = Form(...), T: float = Form(...)):
    d1 = (math.log(S / X) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    
    call_price = S * norm.cdf(d1) - X * math.exp(-r * T) * norm.cdf(d2)
    
    return templates.TemplateResponse("result.html", {"request": request, "call_price": call_price})

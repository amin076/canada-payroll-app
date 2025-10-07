from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PayrollInput(BaseModel):
    name: str
    hours_worked: float
    hourly_rate: float
    province: str

@app.post("/calculate_payroll")
def calculate_payroll(data: PayrollInput):
    gross = data.hours_worked * data.hourly_rate
    cpp = gross * 0.057  # simple fixed CPP example
    ei = gross * 0.0163
    tax = gross * 0.15
    net = gross - (cpp + ei + tax)
    return {
        "employee": data.name,
        "gross_pay": gross,
        "net_pay": round(net, 2),
        "cpp": round(cpp, 2),
        "ei": round(ei, 2),
        "tax": round(tax, 2)
    }

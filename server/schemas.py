from pydantic import BaseModel
from datetime import date

class TransportCreate(BaseModel):
    record_no: int
    transport_date: date
    app_name: str
    trade_type: str
    trade_item: str
    origin: str
    destination: str
    proof_type: str
    tax_invoice_received: bool
    unit_price: int
    company_name: str
    note: str
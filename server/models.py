from sqlalchemy import Column, Integer, String, Date, Boolean, BigInteger, Text
from server.database import Base

class TransportRecord(Base):
    __tablename__ = "transport_records"

    id = Column(Integer, primary_key=True, index=True)
    record_no = Column(Integer)
    transport_date = Column(Date)
    app_name = Column(String)
    trade_type = Column(String)
    trade_item = Column(String)
    origin = Column(String)
    destination = Column(String)
    proof_type = Column(String)
    tax_invoice_received = Column(Boolean)
    unit_price = Column(BigInteger)
    company_name = Column(String)
    note = Column(Text)
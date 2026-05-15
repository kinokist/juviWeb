from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://juvi:Wd03Ylkpn5ng1rGCMpV37jBPEvp58JO3@dpg-d82o49f7f7vs738bnggg-a.singapore-postgres.render.com/juvi"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
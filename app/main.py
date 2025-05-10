from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .database import SessionLocal, engine_db, Base
from . import entities, models, repository, methods

Base.metadata.create_all(bind=engine_db)
app = FastAPI(title="Certificate-Issuance 2025", description="Application to test certificate issuance metrics",version="1.0.0")

def db_session():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.post("/request_certbot")
async def request_certbot(request: CertificateCertbotRequest):
    if request.validation_type == "http":
        result = run_certbot_http(request.domain)
    elif request.validation_type == "dns":
        result = run_certbot_dns(request.domain)
    elif request.validation_type == "wildcard":
        result = run_certbot_wildcard(request.domain)
    else:
        return {"error": "Invalid validation type for certbot"}
    return result

@app.post("/request_yc")
async def request_yc(request: CertificateYcRequest):
    if request.validation_type == "http":
        result = run_yc_cli_http(request.domain)
    elif request.validation_type == "dns":
        result = run_yc_cli_dns(request.domain)
    elif request.validation_type == "wildcard":
        result = run_certbot_wildcard(request.domain)
    else:
        return {"error": "Invalid validation method for yc cli"}
    return result
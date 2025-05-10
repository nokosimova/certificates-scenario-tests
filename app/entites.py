from sqlalchemy import Column, Integer, String
from .database import Base

class CertificateIssuanceLog(Base):
    __tablename__ = 'certificate_issuance_logs'
    
    id = Column(Integer, primary_key=True)
    domain = Column(String(255), nullable=False)
    method = Column(String(50), nullable=False)
    validation_type = Column(String(20))
    sans = Column(Text)
    is_success = Column(Boolean, nullable=False)
    issuance_time_sec = Column(Float)
    cert_expiry_date = Column(TIMESTAMP)
    cert_size_kb = Column(Integer)
    error_log = Column(Text)
    dns_provider = Column(String(50))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

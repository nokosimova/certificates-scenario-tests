from sqlalchemy.orm import Session
from . import entities, models



def save_certificate_issuance_log(db_session: Session, entity: entities.CertificateIssuanceLog):
    
    db_session.add(entity)
    
    db_session.commit()
    
    db_session.refresh(entity)
    
    return entity
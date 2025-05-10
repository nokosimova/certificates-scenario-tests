from pydantic import BaseModel

class CertificateCertbotRequest(BaseModel):
    domain: str
    method: str
    validation_type: str
    sans: List[str]
    dns_plugin: str

class CertificateYcRequest(BaseModel):
    domain: str
    method: str
    validation_type: str
    sans: List[str]
    dns_zone_id: str


class CertificateIssuenceLog(BaseModel):
    domain: str
    method: str
    validation_type: str
    sans: List[str]
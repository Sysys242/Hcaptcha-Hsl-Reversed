import json, base64
from datetime import datetime

def getHsl(proofData) -> str:
    token = proofData['req'].split('.')[1]
    token += '=' * (4 - len(token) % 4)
    tokenJson = json.loads(base64.urlsafe_b64decode(token))
    dt = datetime.utcnow().replace(microsecond=0).isoformat().replace('-', '').replace(':', '').replace('T', '')
    return f"1:{tokenJson['s']}:{dt}:{tokenJson['d']}::2"
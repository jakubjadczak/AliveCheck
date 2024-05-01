from datetime import timezone, datetime
from pydantic import BaseModel, ValidationError, IPvAnyAddress
from enum import Enum
from icmplib import ping


class IPAddress(BaseModel):
    ip: IPvAnyAddress


class PingParmas(Enum):
    HOST_ALIVE = "host_alive"
    AVG_RTT = "avg_rtt"
    PACKET_LOSS = "packet_loss"
    TIMESTAMP = "timestamp"


class PingResponse(BaseModel):
    is_alive: bool
    avarage_response: float
    packet_loss: float
    timestamp: datetime


def ping_ip(address: str, address_id: int):
    try:
        IPAddress(ip=address)
    except ValidationError as e:
        return {"error": str(e)}
    address = str(address)
    host = ping(address, count=5, interval=0.2, timeout=2)

    return {
        "is_alive": host.is_alive,
        "avarage_response": host.avg_rtt,
        "packet_loss": host.packet_loss,
        "timestamp": datetime.now(),
        "address_id": address_id,
    }

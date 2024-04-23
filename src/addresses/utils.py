import ipaddress
from enum import Enum
from bokeh.plotting import figure
from bokeh.embed import components
from django.utils import timezone
from icmplib import ping
from pydantic import BaseModel, ValidationError, IPvAnyAddress

from .models import IPAddress


def calc_subnet(address: str, mask: str):
    network_interface = ipaddress.ip_interface(f"{address}/{mask}")

    network_address = network_interface.network

    return network_address


def simple_chart():
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 3, 6]

    p = figure(
        title="Prosty wykres",
        x_axis_label="X",
        y_axis_label="Y",
        width=1000,
        height=500,
    )

    p.line(x, y, legend_label="Przykład", line_width=2)

    script, div = components(p)

    return {"script": script, "div": div}


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
    timestamp: timezone.datetime


def ping_ip(address: str):
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
        "timestamp": timezone.now(),
    }

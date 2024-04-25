from addresses.utils import calc_subnet
import ipaddress


def test_calc_subnet():
    addr = "77.65.92.180"
    mask = "255.255.255.252"
    assert calc_subnet(addr, mask) == ipaddress.IPv4Network(address="77.65.92.180/30")


def test_calc_subnet1():
    addr = "200.56.0.45"
    mask = "255.240.0.0"
    assert calc_subnet(addr, mask) == ipaddress.IPv4Network(address="200.48.0.0/12")

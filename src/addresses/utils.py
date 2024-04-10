import ipaddress


def calc_subnet(address: str, mask: str):
    network_interface = ipaddress.ip_interface(f"{address}/{mask}")

    network_address = network_interface.network

    print(network_address)

    return network_address

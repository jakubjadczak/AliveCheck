import ipaddress
from bokeh.plotting import figure
from bokeh.embed import components


def calc_subnet(address: str, mask: str):
    network_interface = ipaddress.ip_interface(f"{address}/{mask}")

    network_address = network_interface.network

    print(network_address)

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

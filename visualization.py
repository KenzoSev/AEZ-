from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

protocols = ["http", "https", "ftp"]
methods = ["GET", "POST", "PUT"]
values = [
    [120, 80, 30],   # http counts
    [150, 90, 40],   # https counts
    [60, 40, 0],     # ftp counts (PUT not allowed)
]
colors = {"GET": "#4e79a7", "POST": "#f28e2b", "PUT": "#e15759"}

width = 800
height = 500
margin = 80
bar_width = 40
spacing = 30

svg = Element("svg", xmlns="http://www.w3.org/2000/svg", width=str(width), height=str(height))

# Title
SubElement(svg, "text", x=str(width / 2), y="40", fill="#222", **{"font-size": "20", "font-weight": "bold", "text-anchor": "middle"}).text = "Allowed HTTP Methods by Protocol"

# Axes
SubElement(svg, "line", x1=str(margin), y1=str(margin), x2=str(margin), y2=str(height - margin), stroke="#333", **{"stroke-width": "2"})
SubElement(svg, "line", x1=str(margin), y1=str(height - margin), x2=str(width - margin), y2=str(height - margin), stroke="#333", **{"stroke-width": "2"})

# Y-axis labels and grid
max_value = max(max(row) for row in values)
step = 50
for v in range(0, max_value + step, step):
    y = height - margin - (v / max_value) * (height - 2 * margin)
    SubElement(svg, "line", x1=str(margin), y1=str(y), x2=str(width - margin), y2=str(y), stroke="#ccc", **{"stroke-dasharray": "4 4"})
    SubElement(svg, "text", x=str(margin - 10), y=str(y + 5), fill="#444", **{"font-size": "12", "text-anchor": "end"}).text = str(v)

# Bars
for i, protocol in enumerate(protocols):
    group_x = margin + i * (3 * bar_width + 2 * spacing) + spacing
    # Protocol label
    SubElement(svg, "text", x=str(group_x + bar_width), y=str(height - margin + 24), fill="#222", **{"font-size": "14", "text-anchor": "middle"}).text = protocol

    for j, method in enumerate(methods):
        value = values[i][j]
        bar_height = (value / max_value) * (height - 2 * margin)
        x = group_x + j * (bar_width + spacing)
        y = height - margin - bar_height
        SubElement(
            svg,
            "rect",
            x=str(x),
            y=str(y),
            width=str(bar_width),
            height=str(bar_height),
            fill=colors[method],
            stroke="#ffffff",
            **{"stroke-width": "1"},
        )
        SubElement(svg, "text", x=str(x + bar_width / 2), y=str(y - 6), fill="#222", **{"font-size": "11", "text-anchor": "middle"}).text = str(value)

# Axis label
SubElement(svg, "text", x=str(margin - 10), y=str(margin - 20), fill="#222", transform=f"rotate(-90 {margin - 10},{margin - 20})", **{"font-size": "14", "text-anchor": "middle"}).text = "Allowed Requests (per day)"

# Legend
legend_x = width - margin - 150
legend_y = margin
SubElement(svg, "text", x=str(legend_x), y=str(legend_y), fill="#222", **{"font-size": "13", "font-weight": "bold"}).text = "Method"
for idx, method in enumerate(methods):
    y = legend_y + 20 + idx * 20
    SubElement(svg, "rect", x=str(legend_x), y=str(y), width="14", height="14", fill=colors[method])
    SubElement(svg, "text", x=str(legend_x + 20), y=str(y + 12), fill="#222", **{"font-size": "12"}).text = method

# Pretty-print SVG
rough_string = tostring(svg, 'utf-8')
reparsed = minidom.parseString(rough_string)
with open("visualization.svg", "w", encoding="utf-8") as f:
    f.write(reparsed.toprettyxml())

print("Visualization saved to visualization.svg")

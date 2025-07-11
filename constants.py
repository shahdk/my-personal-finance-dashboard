
def currency_fmt(num):
    for unit in ("", "K", "M"):
        if abs(num) < 1000.0:
            return f"${num:3.1f} {unit}"
        num /= 1000.0
    return f"$"

blue_node_color = 'rgba(0, 119, 184, 1)'
blue_link_color = 'rgba(0, 119, 184, 0.4)'

green_node_color = 'rgba(0, 163, 76, 1)'
green_link_color = 'rgba(0, 163, 76, 0.4)'

red_node_color = 'rgba(209, 0, 63, 1)'
red_link_color = 'rgba(209, 0, 63, 0.4)'

label_mappings = {
    'paycheck_person1': {'idx': 0, 'color': blue_node_color, 'x': 0, 'y': 0},
    'paycheck_person2': {'idx': 1, 'color': blue_node_color, 'x': 0, 'y': 0},
    'stocks': {'idx': 2, 'color': blue_node_color, 'x': 0, 'y': 0},
    'cash_bonus': {'idx': 3, 'color': blue_node_color, 'x': 0, 'y': 0},
    'interest_income': {'idx': 4, 'color': blue_node_color, 'x': 0, 'y': 0},
    'dividends': {'idx': 5, 'color': blue_node_color, 'x': 0, 'y': 0},
    'capital_gains': {'idx': 6, 'color': blue_node_color, 'x': 0, 'y': 0},
    'earned_income': {'idx': 7, 'color': green_node_color, 'x': 0.2, 'y': 0},
    'passive_income': {'idx': 8, 'color': green_node_color, 'x': 0.2, 'y': 0},
    'total_income': {'idx': 9, 'color': green_node_color, 'x': 0.4, 'y': 0},
    'taxes': {'idx': 10, 'color': red_node_color, 'x': 0.6, 'y': 0.6},
    'needs': {'idx': 11, 'color': red_node_color, 'x': 0.8, 'y': 0.6},
    'investments': {'idx': 12, 'color': green_node_color, 'x': 0.8, 'y': 0},
    'wants': {'idx': 13, 'color': red_node_color, 'x': 0.8, 'y': 0},
    'take_home': {'idx': 14, 'color': green_node_color, 'x': 0.6, 'y': 0},
    'discretionary': {'idx': 15, 'color': green_node_color, 'x': 0.8, 'y': 0},
}

labels = []
node_color = []
x = []
y = []
for label in label_mappings:
    labels.append("<b>"+label.title().replace('_',' ')+"</b> <br> __"+label+"__")
    node_color.append(label_mappings[label]['color'])
    x.append(label_mappings[label]['x'])
    y.append(label_mappings[label]['y'])


links = [
    {'source': 'paycheck_person1', 'target':'earned_income', 'color': blue_link_color},
    {'source': 'paycheck_person2', 'target':'earned_income', 'color': blue_link_color},
    {'source': 'stocks', 'target':'earned_income', 'color': blue_link_color},
    {'source': 'cash_bonus', 'target':'earned_income', 'color': blue_link_color},
    {'source': 'interest_income', 'target':'passive_income', 'color': blue_link_color},
    {'source': 'dividends', 'target':'passive_income', 'color': blue_link_color},
    {'source': 'capital_gains', 'target':'passive_income', 'color': blue_link_color},
    {'source': 'earned_income', 'target':'total_income', 'color': green_link_color},
    {'source': 'passive_income', 'target':'total_income', 'color': green_link_color},
    {'source': 'total_income', 'target':'take_home', 'color': green_link_color},
    {'source': 'total_income', 'target':'taxes', 'color': red_link_color},
    {'source': 'take_home', 'target':'discretionary', 'color': green_link_color},
    {'source': 'take_home', 'target':'needs', 'color': red_link_color},
    {'source': 'discretionary', 'target':'investments', 'color': green_link_color},
    {'source': 'discretionary', 'target':'wants', 'color': red_link_color}
]

source = []
target = []
link_color = []
for link in links:
    source.append(label_mappings[link['source']]['idx'])
    target.append(label_mappings[link['target']]['idx'])
    link_color.append(link['color'])


default_colors = [
    "aliceblue", "antiquewhite", "aqua", "aquamarine", "azure",
    "beige", "bisque", "black", "blanchedalmond", "blue",
    "blueviolet", "brown", "burlywood", "cadetblue",
    "chartreuse", "chocolate", "coral", "cornflowerblue",
    "cornsilk", "crimson", "cyan", "darkblue", "darkcyan",
    "darkgoldenrod", "darkgray", "darkgrey", "darkgreen",
    "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange",
    "darkorchid", "darkred", "darksalmon", "darkseagreen",
    "darkslateblue", "darkslategray", "darkslategrey",
    "darkturquoise", "darkviolet", "deeppink", "deepskyblue",
    "dimgray", "dimgrey", "dodgerblue", "firebrick",
    "floralwhite", "forestgreen", "fuchsia", "gainsboro",
    "ghostwhite", "gold", "goldenrod", "gray", "grey", "green",
    "greenyellow", "honeydew", "hotpink", "indianred", "indigo",
    "ivory", "khaki", "lavender", "lavenderblush", "lawngreen",
    "lemonchiffon", "lightblue", "lightcoral", "lightcyan",
    "lightgoldenrodyellow", "lightgray", "lightgrey",
    "lightgreen", "lightpink", "lightsalmon", "lightseagreen",
    "lightskyblue", "lightslategray", "lightslategrey",
    "lightsteelblue", "lightyellow", "lime", "limegreen",
    "linen", "magenta", "maroon", "mediumaquamarine",
    "mediumblue", "mediumorchid", "mediumpurple",
    "mediumseagreen", "mediumslateblue", "mediumspringgreen",
    "mediumturquoise", "mediumvioletred", "midnightblue",
    "mintcream", "mistyrose", "moccasin", "navajowhite", "navy",
    "oldlace", "olive", "olivedrab", "orange", "orangered",
    "orchid", "palegoldenrod", "palegreen", "paleturquoise",
    "palevioletred", "papayawhip", "peachpuff", "peru", "pink",
    "plum", "powderblue", "purple", "red", "rosybrown",
    "royalblue", "saddlebrown", "salmon", "sandybrown",
    "seagreen", "seashell", "sienna", "silver", "skyblue",
    "slateblue", "slategray", "slategrey", "snow", "springgreen",
    "steelblue", "tan", "teal", "thistle", "tomato", "turquoise",
    "violet", "wheat", "white", "whitesmoke", "yellow",
    "yellowgreen"
]
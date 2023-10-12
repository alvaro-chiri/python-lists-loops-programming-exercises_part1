all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors(color):
    return color["sexy"] == True

sexy_colors = list(filter(filter_colors, all_colors))

def generate_li(color):
    return f'<li>{color["label"]}</li>'

print(list(map(generate_li, sexy_colors)))

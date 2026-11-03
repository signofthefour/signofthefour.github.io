from pathlib import Path
import subprocess
import re


sydney_crop = Path("DSCF7502-cropped.jpg")
assert sydney_crop.exists(), "The non-destructive Sydney portrait crop should exist."

metadata = subprocess.run(
    ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(sydney_crop)],
    check=True,
    capture_output=True,
    text=True,
).stdout

assert "pixelWidth: 2791" in metadata, metadata
assert "pixelHeight: 3196" in metadata, metadata

page = Path("index.html").read_text()
stack = re.search(r'<div class="portrait-stack".*?</div>', page, re.S)
assert stack, "The sidebar should contain a portrait stack."
stack_markup = stack.group(0)

sydney = re.search(
    r'<figure class="portrait-card portrait-card--sydney"[^>]*>.*?'
    r'<img src="DSCF7502-cropped\.jpg"[^>]*>.*?'
    r'<figcaption[^>]*>Sydney, Australia w\. MMAI</figcaption>.*?'
    r'</figure>',
    stack_markup,
    re.S,
)
honolulu = re.search(
    r'<figure class="portrait-card portrait-card--honolulu"[^>]*>.*?'
    r'<img src="DSCF0519\.jpg"[^>]*>.*?'
    r'<figcaption[^>]*>Honolulu, Hawaii@USA w\. MMAI</figcaption>.*?'
    r'</figure>',
    stack_markup,
    re.S,
)
assert sydney, "Sydney should be the first complete photo figure."
assert honolulu, "Honolulu should be the second complete photo figure."
assert stack_markup.index("portrait-card--sydney") < stack_markup.index("portrait-card--honolulu")
assert page.index('class="portrait-stack"') < page.index('class="sidebar-opportunities"')
assert stack_markup.count('tabindex="0"') == 2, "Both cards should expand with keyboard focus."

sydney_rule = re.search(r"\.portrait-card--sydney\s*\{(?P<body>[^}]*)\}", page, re.S)
honolulu_rule = re.search(r"\.portrait-card--honolulu\s*\{(?P<body>[^}]*)\}", page, re.S)
stack_rule = re.search(r"\.portrait-stack\s*\{(?P<body>[^}]*)\}", page, re.S)
assert stack_rule and re.search(r"position:\s*relative", stack_rule.group("body"))
assert re.search(r"aspect-ratio:\s*3\s*/\s*4", stack_rule.group("body"))
assert sydney_rule and re.search(r"left:\s*0", sydney_rule.group("body"))
assert re.search(r"z-index:\s*2", sydney_rule.group("body"))
assert honolulu_rule and re.search(r"right:\s*0", honolulu_rule.group("body"))
assert re.search(r"z-index:\s*1", honolulu_rule.group("body"))
assert re.search(r"\.portrait-card\s*\{[^}]*position:\s*absolute", page, re.S)
assert re.search(r"\.portrait-card\s*\{[^}]*width:\s*72%", page, re.S)
assert re.search(r"\.portrait-stack\s*\{[^}]*max-width:\s*320px", page, re.S)

expand_rule = re.search(
    r"\.portrait-card:hover,\s*\.portrait-card:focus\s*\{(?P<body>[^}]*)\}",
    page,
    re.S,
)
assert expand_rule and re.search(r"width:\s*100%", expand_rule.group("body"))
assert re.search(r"z-index:\s*3", expand_rule.group("body"))

caption_rule = re.search(r"\.portrait-caption\s*\{(?P<body>[^}]*)\}", page, re.S)
caption_color = re.search(r"color:\s*(#[0-9a-fA-F]{6})", caption_rule.group("body")) if caption_rule else None
assert caption_color, "Paper captions need a fixed dark color in both themes."


def luminance(hex_color):
    channels = [int(hex_color[index:index + 2], 16) / 255 for index in (1, 3, 5)]
    linear = [value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4 for value in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


foreground = luminance(caption_color.group(1))
background = luminance("#f8f5ed")
contrast = (max(foreground, background) + 0.05) / (min(foreground, background) + 0.05)
assert contrast >= 4.5, f"Caption contrast on paper is only {contrast:.2f}:1."

print("Sidebar photo asset checks passed.")

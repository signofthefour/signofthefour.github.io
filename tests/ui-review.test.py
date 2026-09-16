from html.parser import HTMLParser
from pathlib import Path
import re


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.current_link = None
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        attributes = dict(attrs)
        self.current_link = {
            "class": set(attributes.get("class", "").split()),
            "href": attributes.get("href", ""),
            "text": "",
        }
        self.links.append(self.current_link)

    def handle_endtag(self, tag):
        if tag == "a":
            self.current_link = None

    def handle_data(self, data):
        if self.current_link is not None:
            self.current_link["text"] += data


page = Path("index.html").read_text()
parser = PageParser()
parser.feed(page)

expected_navigation = [
    ("About", "#about"),
    ("Research", "#projects"),
    ("Publications", "#publications"),
    ("Experience", "#experience"),
    ("Contact", "#contact"),
]

for nav_class in ("nav-link", "mob-link"):
    navigation = [
        (link["text"].strip(), link["href"])
        for link in parser.links
        if nav_class in link["class"]
    ]
    assert navigation == expected_navigation, (
        f"{nav_class} navigation should expose five primary destinations; got {navigation}"
    )

hero_actions = [
    link["text"].strip()
    for link in parser.links
    if "hero-cta" in link["class"]
]
assert hero_actions == ["Google Scholar", "View CV", "Email me"], (
    f"Hero should expose three primary actions; got {hero_actions}"
)

mobile_rules = re.search(r"@media \(max-width: 640px\) \{(?P<rules>.*?)\n    \}", page, re.S)
assert mobile_rules, "A 640px mobile breakpoint should exist."
rules = mobile_rules.group("rules")
assert re.search(r"#publications article\s*\{[^}]*flex-direction:\s*column", rules, re.S), (
    "Publication cards should stack vertically on mobile."
)
assert re.search(r"#publications \.paper-visual\s*\{[^}]*width:\s*100%", rules, re.S), (
    "Publication artwork frames should use the card width on mobile."
)

print("UI review checks passed.")

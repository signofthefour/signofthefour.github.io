from pathlib import Path
import re


page = Path("index.html").read_text()

# Publication totals act as a mutually exclusive authorship filter.
assert re.search(
    r'<div class="publication-scope"[^>]*role="group"[^>]*aria-label="Filter by authorship"',
    page,
)
assert 'data-scope="all"' in page
assert 'data-scope="first-authored"' in page

# Every year is independently expandable, with only the current year open initially.
year_groups = re.findall(
    r'<details class="publication-year"(?P<open> open)?[^>]*>\s*'
    r'<summary[^>]*>\s*(?P<year>20\d{2})',
    page,
)
assert year_groups, "Publication years should use expandable details controls."
open_years = [year for is_open, year in year_groups if is_open]
assert open_years == ["2026"], f"Only 2026 should start open; got {open_years}."

# One render function combines type and authorship filters instead of overwriting state.
assert "function renderPublications()" in page
assert "article.dataset.type" in page
assert "article.dataset.firstAuthored" in page
assert re.search(
    r"matchesType\s*&&\s*matchesScope",
    page,
), "Publication visibility should satisfy both active filters."
assert re.search(
    r"#publications\s+\[hidden\]\s*\{[^}]*display:\s*none\s*!important",
    page,
    re.S,
), "Filtered flex cards need an explicit hidden rule that wins over Tailwind utilities."

# The seven-paper count includes papers where Tan Dat Nguyen is an equal first author.
assert "isFirstAuthored" in page
assert "every(author => author.endsWith('*'))" in page

# Inter-section spacing is exactly half of the previous desktop and compact values.
for spacing in ("3.25rem", "2.75rem", "2.5rem"):
    assert spacing in page
assert "margin-top: 6.5rem !important" not in page
assert "margin-top: 5.5rem !important" not in page
assert "margin-top: 5rem !important" not in page

print("Publication interaction checks passed.")

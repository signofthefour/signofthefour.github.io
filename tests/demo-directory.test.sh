#!/bin/sh
set -eu

page=index.html

grep -Eq '<a href="#demos"[^>]*class="nav-link[^>]*>Demos</a>' "$page"
grep -Eq '<a href="#demos"[^>]*class="mob-link[^>]*>Demos</a>' "$page"
grep -q '<section id="demos" aria-labelledby="demos-heading">' "$page"

projects_line=$(grep -n '<section id="projects">' "$page" | cut -d: -f1)
demos_line=$(grep -n '<section id="demos"' "$page" | cut -d: -f1)
publications_line=$(grep -n '<section id="publications">' "$page" | cut -d: -f1)

test "$projects_line" -lt "$demos_line"
test "$demos_line" -lt "$publications_line"

demo_count=$(sed -n "${demos_line},${publications_line}p" "$page" | grep -c 'data-demo-card')
test "$demo_count" -ge 8
sed -n "${demos_line},${publications_line}p" "$page" | grep -q 'target="_blank" rel="noopener"'

grep -q 'class="name-pronunciation"' "$page"
grep -q 'aria-describedby="name-pronunciation-tip"' "$page"
grep -q 'id="name-pronunciation-tip" role="tooltip"' "$page"
grep -q '/tən ɗaːt̚/' "$page"
if grep -q '<strong>Tấn Đạt</strong>' "$page"; then
  printf 'Tooltip should contain only the IPA pronunciation.\n' >&2
  exit 1
fi

printf 'Demo directory checks passed (%s demos).\n' "$demo_count"

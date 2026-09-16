#!/bin/sh
set -eu

page=index.html

if grep -q 'href="#demos"' "$page"; then
  printf 'Dedicated Demos navigation links should be removed.\n' >&2
  exit 1
fi

if grep -q '<section id="demos"' "$page"; then
  printf 'The dedicated Research Demos section should be removed.\n' >&2
  exit 1
fi

grep -Eq '<a href="[^"]+"[^>]*class="pill">Demo</a>' "$page"

grep -q 'class="name-pronunciation"' "$page"
grep -q 'aria-describedby="name-pronunciation-tip"' "$page"
grep -q 'id="name-pronunciation-tip" role="tooltip"' "$page"
grep -q '/tən ɗaːt̚/' "$page"
if grep -q '<strong>Tấn Đạt</strong>' "$page"; then
  printf 'Tooltip should contain only the IPA pronunciation.\n' >&2
  exit 1
fi

printf 'Site structure checks passed.\n'

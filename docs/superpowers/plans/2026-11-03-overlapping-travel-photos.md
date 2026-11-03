# Overlapping Travel Photos Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a Sydney-first horizontal photo deck with hover/focus expansion while preserving both original travel photos.

**Architecture:** Create a non-destructive portrait derivative of the Sydney photo, then render both photos as separate semantic figures in the existing sidebar. CSS controls the horizontal overlap, expansion interaction, stacking order, paper-card treatment, and responsive behavior without merging the images.

**Tech Stack:** HTML, CSS, Python static checks, macOS image metadata tools, built-in image editing

**Spec:** `docs/superpowers/specs/2026-11-03-overlapping-travel-photos-design.md`

## Global Constraints

- Keep `DSCF0519.jpg` and `DSCF7502.JPG` unchanged.
- Create the Sydney derivative at exactly 2791 × 3196 pixels.
- Keep Sydney visible and leave a discoverable Honolulu preview in the collapsed deck.
- Sydney is the left/front card; hover or keyboard focus expands either card to the deck width.
- Preserve existing light/dark styling and sidebar width.

## Review Focus

- Desktop stack: Sydney and the Honolulu preview remain discoverable at the 220–260 px sidebar width; verify visually in Task 2.
- Mobile stack: neither card overflows the 320 px sidebar maximum; pin responsive selectors in Task 2.
- Long captions: each caption remains attached to its own figure; pin figure/figcaption structure in Task 2.
- Image fidelity: Sydney identity, pose, lighting, and color remain unchanged apart from cropping; inspect the final derivative in Task 1.
- Existing sidebar controls: collaboration status and Scholar link remain after the stack; pin source ordering in Task 2.

---

### Task 1: Sydney Portrait Derivative

**Files:**
- Create: `DSCF7502-cropped.jpg`
- Create: `tests/sidebar-photos.test.py`

**Interfaces:**
- Consumes: `DSCF7502.JPG` as the immutable landscape source.
- Produces: `DSCF7502-cropped.jpg`, a 2791 × 3196 portrait JPEG centered on Tan Dat for Task 2.

- [ ] **Step 1: Write the failing asset test**

Create `tests/sidebar-photos.test.py` with a test that asserts `DSCF7502-cropped.jpg` exists and reports `pixelWidth: 2791` and `pixelHeight: 3196` through `sips -g pixelWidth -g pixelHeight`.

- [ ] **Step 2: Run the asset test and verify it fails**

Run: `python3 tests/sidebar-photos.test.py`

Expected: FAIL because `DSCF7502-cropped.jpg` does not exist.

- [ ] **Step 3: Create the portrait derivative**

Use the built-in image editor with `DSCF7502.JPG` as the edit target and this invariant: crop to a centered portrait composition around Tan Dat; change no identity, pose, clothing, background content, lighting, or color; add no objects or text. Save the result as `DSCF7502-cropped.jpg`, then normalize it to exactly 2791 × 3196 pixels without stretching.

- [ ] **Step 4: Inspect and test the derivative**

Open the derivative at original detail and confirm the face and body remain intact. Run `python3 tests/sidebar-photos.test.py`; expected: PASS with 2791 × 3196.

### Task 2: Expandable Sidebar Photo Deck

**Files:**
- Modify: `index.html:99-110`
- Modify: `index.html:998-1006`
- Modify: `tests/sidebar-photos.test.py`

**Interfaces:**
- Consumes: `DSCF7502-cropped.jpg` from Task 1 and existing `DSCF0519.jpg`.
- Produces: `.portrait-stack`, `.portrait-card`, `.portrait-card--sydney`, and `.portrait-card--honolulu` HTML/CSS contracts with hover/focus expansion.

- [ ] **Step 1: Extend the test with failing markup and layout assertions**

Assert that Sydney precedes Honolulu in `.portrait-stack`; each image is inside its own focusable `figure` with its own `figcaption`; the captions are exact; cards overlap horizontally at 72% width; hover/focus expands a card to 100% width and raises its stacking layer; and the existing availability block follows the stack.

- [ ] **Step 2: Run the focused test and verify it fails**

Run: `python3 tests/sidebar-photos.test.py`

Expected: FAIL on missing `.portrait-stack` markup.

- [ ] **Step 3: Implement the two-card HTML**

Replace the single image wrapper and detached caption with a `.portrait-stack` containing two figures. Put the Sydney figure first with `DSCF7502-cropped.jpg`, then the Honolulu figure with `DSCF0519.jpg`; use descriptive location-specific alt text and the exact captions from Step 1.

- [ ] **Step 4: Implement the overlapping CSS**

Reuse the existing paper-card border, padding, shadow, and subtle rotations on `.portrait-card`. Position the cards absolutely in a 3 / 4 deck, anchor Sydney left/front and Honolulu right/back, expose a Honolulu preview, expand hovered/focused cards to 100% width, retain `object-fit: cover`, respect reduced motion, and keep the existing mobile width cap.

- [ ] **Step 5: Run focused and full verification**

Run:

```bash
python3 tests/sidebar-photos.test.py
python3 tests/publications-ui.test.py
python3 tests/ui-review.test.py
sh tests/site-structure.test.sh
git diff --check
```

Expected: all checks pass with no whitespace errors.

- [ ] **Step 6: Perform visual verification**

Inspect desktop and mobile layouts. Confirm Sydney is left/front, Honolulu remains discoverable on the right, hover/focus expands either card, and the status/Scholar controls stay aligned below the deck.

No commit step is included because the checkout already contains uncommitted user work; committing would bundle unrelated changes without explicit authorization.

# Overlapping Travel Photos

## Intent

Show both MMAI travel photos in the sidebar as a compact, personal photo stack instead of replacing the existing Honolulu portrait.

## Design

- Crop `DSCF7502.JPG` non-destructively to the same 2791 × 3196 portrait dimensions as `DSCF0519.jpg`, keeping Tan Dat centered and preserving the original file.
- Arrange the photos as a horizontally overlapping card deck, with Sydney on the left/front and a visible Honolulu preview on the right.
- Expand either card to the full deck width on hover or keyboard focus.
- Caption the new photo “Sydney, Australia w. MMAI” and retain the Honolulu caption.
- Keep the stack responsive and preserve the existing paper-photo styling, light/dark themes, and sidebar width.

## Approaches

- Selected: two separate portrait cards in a CSS-only horizontal deck with hover/focus expansion. This preserves both source images and keeps the interaction responsive and keyboard-accessible.
- Rejected: merge both photos into one bitmap. This would make responsive cropping and future photo changes harder.
- Rejected: carousel or click-to-swap. It would hide one photo and add interaction the request does not need.

## Constraints

- Do not overwrite either original image.
- Do not crop out either face.
- Do not enlarge the sidebar or reintroduce large section gaps.

# Try-On Modal — Design Specification (Light & Dark)

## 0. Overview
A guided, step-based modal for virtual try-on with a consistent 2-column layout:
- Left: Visual output (3:4 image)
- Right: Contextual control panel (reused patterns)

Core principle: Guided flow, not a tool interface. Reuse patterns (Step 1 == Step 4).

---

## 1. Layout

Container:
- Width: 1100–1200px
- Height: 80–85vh
- Radius: 16px
- Padding: 24px

Structure:
Header → Content → Footer

Columns:
- Left: Image (3:4), persistent across steps
- Right: Control panel (content swaps per step)

---

## 2. Interaction Flow

Steps:
1. Select Yourself
2. Generating
3. Result
4. Refine Pose (reuses Step 1 layout)

States:
idle, photo_selected, generating, result_ready, pose_selecting, pose_generating, error

---

## 3. Step Details

Step 1 — Select Yourself:
- Photo grid
- Upload
- Guidance block
- CTA (disabled until selection)

Step 2 — Generating:
- Loader
- Progress states

Step 3 — Result:
- Image output
- Actions (save, download)
- Refine option

Step 4 — Refine Pose:
- Same layout as Step 1
- Back button
- Pose grid
- Apply pose CTA

---

## 4. Motion

Durations:
- Fast: 120ms
- Medium: 220ms
- Slow: 320ms

Key animations:
- Modal open: scale + fade
- Result: fade + lift
- Pose apply: crossfade

---

## 5. Tokens

Light Mode:
- bg: #F6F3EE
- text: #1C1A18
- accent: #8C6A4A

Dark Mode:
- bg: #121212
- text: #F5F5F5
- accent: #3A6B6B

Glass:
- Light: rgba(255,255,255,0.6)
- Dark: rgba(255,255,255,0.08)

---

## 6. Principles

- Reuse patterns
- Keep UI calm
- Avoid complexity
- Focus on image
- Progressive flow

---

End of Document

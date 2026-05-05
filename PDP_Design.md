
# PDP (Product Detail Page) — Design.md

## Overview
Minimal, editorial PDP optimized for Try-On as the primary action. 
Focus: clarity, calm hierarchy, and progressive discovery.

---

## Layout

### Grid
- Max width: 1200px
- 12-column grid
- Left: 7 columns (Product Gallery)
- Right: 5 columns (Product Info)

### Sections
1. Product Section (2-column)
2. Pair it with (full-width)
3. Similar Products (optional, full-width)

---

## Product Section (Above the Fold)

### Left — Product Gallery
- Aspect ratio: 3:4 (catalog standard)
- Carousel with thumbnails
- Subtle hover zoom (desktop)
- No heavy overlays

### Right — Product Info Flow

Order:
1. Brand
2. Title (max 2 lines)
3. Metadata (category · gender · color)
4. Price
5. Size Pills
6. Try-On CTA
7. Micro Info
8. Product Details (Accordion)

---

## Title System

- Max 2 lines
- Overflow: ellipsis
- Width: 420–480px

### Structure
- Title: core product name
- Metadata: attributes (Women · Black · Oversized)

---

## Size Pills

- Height: 36–40px
- Max 5 per row
- Radius: 999px

States:
- Default: transparent + subtle border
- Hover: accent-soft
- Selected: accent-soft fill

---

## Try-On CTA (Primary)

### Light Mode
- Background: #1C1A18
- Text: #FFFFFF

### Dark Mode
- Background: #F5F5F5
- Text: #121212

### Glass Layer (subtle)
- Used only on CTA
- Light: rgba(255,255,255,0.6)
- Dark: rgba(255,255,255,0.08)

---

## Product Details (Accordion)

- Text-first, no cards
- Row height: 44–48px
- Divider: subtle

Sections:
- Description
- Fabric & Care
- Fit Details

---

## Pair it with (Full Width)

### Behavior
- Breaks out of 2-column grid
- Full container width

### Layout
- Grid: auto-fit (min 200–220px)
- 4–6 items visible depending on width

### Content
- Only upperwear / lowerwear (no accessories)

### Title
- “Pair it with”
- Low visual weight

---

## Visual Hierarchy

1. Product Image (Primary)
2. Title + Price
3. CTA (Try-On)
4. Size Selection
5. Accordion
6. Pair it with

---

## Spacing System

- Micro: 16px
- Section: 24px
- Major: 32px

---

## Color Tokens

### Light Mode
- bg-primary: #F6F3EE
- bg-secondary: #EFEAE3
- bg-elevated: #FFFFFF

- text-primary: #1C1A18
- text-secondary: #6E675F
- text-tertiary: #A39B92

- accent-primary: #8C6A4A
- accent-soft: #E8DED3

---

### Dark Mode
- bg-primary: #121212
- bg-secondary: #1A1A1A
- bg-elevated: #202020

- text-primary: #F5F5F5
- text-secondary: #A1A1A1
- text-tertiary: #6B6B6B

- accent-primary: #3A6B6B
- accent-soft: #223838

---

## Interaction Principles

- Minimal motion
- No layout shifts
- Progressive disclosure

---

## What is intentionally removed

- Add to Cart
- Delivery / Shipping info
- Trust badges

---

## Design Philosophy

“Calm surface + intelligent interaction”

- Base: editorial, matte
- Interaction: subtle glass (only where needed)
- Avoid clutter, avoid marketplace feel

---

## Future Ready

- Mix & Match integration
- Styling recommendations
- AI personalization layer

---

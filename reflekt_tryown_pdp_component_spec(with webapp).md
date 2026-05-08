# REFLEKT / TRYOWN PDP Component Specification

## 1. Purpose

This document defines the UI, layout, typography, component behavior, and responsive behavior for the Product Detail Page used in the REFLEKT / TRYOWN web app.

The PDP should feel like:

> A calm fashion editorial product page with an intelligent try-on layer.

The interface should avoid marketplace clutter and prioritize:

1. Product imagery
2. Product identity
3. Size selection
4. Try-On interaction
5. Styling recommendations
6. Similar product discovery

The primary action is always:

> Try This On

The secondary action is:

> Buy on Merchant

## 2. Design Principles

### 2.1 Visual Direction

The PDP should feel:

- Minimal
- Editorial
- Premium
- Calm
- Matte
- Thumb-friendly on mobile
- Spacious but not sparse

Avoid:

- Heavy card shadows
- Marketplace-style badges
- Delivery/trust widgets
- Overloaded product information
- Add-to-cart behavior
- Aggressive promotional banners

### 2.2 Interaction Philosophy

Use:

- Progressive disclosure
- Subtle motion
- Clear tap targets
- No layout shifts
- Sticky primary actions on mobile
- Horizontal swiping for curated styling content

Avoid:

- Flashy animations
- Floating clutter
- Excessive overlays
- Multiple competing CTAs

## 3. Design Tokens

### 3.1 Light Mode

| Token | Value | Usage |
|---|---:|---|
| `bg-primary` | `#F6F3EE` | Main page background |
| `bg-secondary` | `#EFEAE3` | Secondary soft surfaces |
| `bg-elevated` | `#FFFFFF` | Cards, secondary buttons |
| `text-primary` | `#1C1A18` | Main text, title, price |
| `text-secondary` | `#6E675F` | Metadata, descriptions |
| `text-tertiary` | `#A39B92` | Low-priority labels |
| `accent-primary` | `#8C6A4A` | Selected borders, accent details |
| `accent-soft` | `#E8DED3` | Selected pills, soft highlights |
| `cta-bg` | `#1C1A18` | Primary CTA background |
| `cta-text` | `#FFFFFF` | Primary CTA text |
| `glass-bg` | `rgba(255,255,255,0.6)` | Light glass surfaces |
| `glass-border` | `rgba(255,255,255,0.4)` | Glass border |
| `glass-blur` | `10px` | Glass blur |

### 3.2 Dark Mode

| Token | Value | Usage |
|---|---:|---|
| `bg-primary` | `#121212` | Main page background |
| `bg-secondary` | `#1A1A1A` | Secondary surfaces |
| `bg-elevated` | `#202020` | Cards, elevated surfaces |
| `text-primary` | `#F5F5F5` | Main text |
| `text-secondary` | `#A1A1A1` | Metadata |
| `text-tertiary` | `#6B6B6B` | Low-priority labels |
| `accent-primary` | `#3A6B6B` | Accent details |
| `accent-soft` | `#223838` | Selected states |
| `cta-bg` | `#F5F5F5` | Primary CTA background |
| `cta-text` | `#121212` | Primary CTA text |
| `glass-bg` | `rgba(255,255,255,0.08)` | Dark glass surfaces |
| `glass-border` | `rgba(255,255,255,0.12)` | Glass border |
| `glass-blur` | `12px` | Glass blur |
| `accent-glow` | `rgba(58,107,107,0.25)` | Optional CTA glow |

## 4. Spacing System

### 4.1 Base Spacing

| Name | Value | Usage |
|---|---:|---|
| Micro | `16px` | Component padding, horizontal page padding |
| Section | `24px` | Between related groups |
| Major | `32px` | Between major PDP sections |

### 4.2 Mobile Spacing

| Use Case | Value |
|---|---:|
| Page side padding | `16px` |
| Header horizontal padding | `16px` |
| Product info internal gap | `8px–12px` |
| Between major sections | `28px–32px` |
| Product card gap | `12px` |
| Bottom padding above sticky bar | `96px–112px` |
| Sticky bar padding | `12px 16px` |
| Sticky bar safe area | `calc(12px + env(safe-area-inset-bottom))` |

### 4.3 Desktop Spacing

| Use Case | Value |
|---|---:|
| Max container width | `1200px` |
| Grid gutter | `24px` |
| Product section gap | `32px` |
| Section gap | `32px` |
| Thumbnail gap | `12px` |

## 5. Typography

### 5.1 Font Direction

Use a clean modern sans-serif typeface.

Recommended font style:

- Geometric or neutral sans-serif
- High readability
- Minimal stylistic noise

Examples:

- Inter
- Neue Haas Grotesk
- Helvetica Now
- Satoshi
- Manrope

### 5.2 Mobile Text Sizes

| Element | Size | Weight | Line Height | Color |
|---|---:|---:|---:|---|
| Brand label | `11px–12px` | `600` | `16px` | `text-secondary` |
| Product title | `22px–24px` | `650–700` | `28px–30px` | `text-primary` |
| Metadata | `13px` | `400` | `18px` | `text-secondary` |
| Price | `22px` | `700` | `28px` | `text-primary` |
| Rating text | `12px–13px` | `400` | `18px` | `text-secondary` |
| Section heading | `18px` | `600` | `24px` | `text-primary` |
| Card title | `13px–14px` | `500–600` | `18px` | `text-primary` |
| Card price | `13px–14px` | `700` | `18px` | `text-primary` |
| Accordion row label | `14px–15px` | `500` | `20px` | `text-primary` |
| Accordion body | `13px–14px` | `400` | `20px` | `text-secondary` |
| Button text | `13px–14px` | `700` | `18px` | CTA-specific |
| Footer text | `11px–12px` | `400` | `18px` | `text-secondary` |

### 5.3 Desktop Text Sizes

| Element | Size | Weight | Line Height | Color |
|---|---:|---:|---:|---|
| Brand label | `12px` | `600` | `16px` | `text-secondary` |
| Product title | `28px–32px` | `650–700` | `36px–40px` | `text-primary` |
| Metadata | `14px` | `400` | `20px` | `text-secondary` |
| Price | `26px–28px` | `700` | `34px` | `text-primary` |
| Rating text | `13px` | `400` | `18px` | `text-secondary` |
| Section heading | `20px` | `600` | `28px` | `text-primary` |
| Card title | `14px` | `500–600` | `18px` | `text-primary` |
| Card price | `14px` | `700` | `18px` | `text-primary` |
| Button text | `14px` | `700` | `18px` | CTA-specific |

## 6. Responsive Layout

### 6.1 Desktop PDP Layout

Desktop uses a 12-column grid.

| Area | Columns |
|---|---:|
| Product gallery | 7 columns |
| Product info | 5 columns |

Container:

- Max width: `1200px`
- Center aligned
- Grid gutter: `24px`

Desktop page order:

1. Header
2. Breadcrumbs
3. Product section
   - Left: Gallery
   - Right: Product info
4. Complete the look / Pair it with
5. Similar Products
6. Footer

### 6.2 Mobile PDP Layout

Mobile uses a single-column layout.

Mobile page order:

1. Floating header
2. Hero gallery
3. Product info
4. Size selection
5. Accordion details
6. Complete the look carousel
7. Similar products grid
8. Footer
9. Sticky bottom action bar

Mobile layout should not simply compress desktop. It should feel app-native.

Key mobile changes:

- Remove thumbnail rail
- Replace gallery with swipeable image carousel
- Move actions into sticky bottom bar
- Use horizontal carousel for Complete the look
- Use two-column grid for Similar Products
- Maintain sufficient bottom padding so sticky bar does not cover content

## 7. Header Component

### 7.1 Mobile Header

The mobile header should feel lightweight and app-native.

#### Layout

| Position | Element |
|---|---|
| Left | Circular back button |
| Center | `REFLEKT` wordmark |
| Right | Search icon, wishlist icon |

#### Dimensions

| Property | Value |
|---|---:|
| Height | `56px–64px` |
| Horizontal padding | `16px` |
| Icon button size | `36px–40px` |
| Icon size | `18px–20px` |
| Wordmark size | `14px–16px` |
| Wordmark weight | `700` |
| Letter spacing | `0.12em–0.18em` |

#### Visual Style

At page top:

- Minimal
- Transparent or near-transparent
- Does not compete with product image

On scroll:

- Translucent warm background
- Blur effect
- Faint bottom divider

Recommended style:

- Background: `rgba(246, 243, 238, 0.84)`
- Backdrop blur: `12px`
- Border-bottom: `rgba(28, 26, 24, 0.06)`

#### Behavior

- Header remains sticky at top.
- Header should gain stronger background only after the user scrolls.
- Header should not cause layout shift.

### 7.2 Desktop Header

Desktop header can be more conventional.

#### Layout

| Area | Element |
|---|---|
| Left | REFLEKT wordmark |
| Center/right | Search |
| Right | Theme toggle, wishlist, account, bag |

#### Behavior

- Header remains fixed or sticky depending on application shell.
- Keep height compact.
- Avoid oversized navigation.

## 8. Product Gallery

### 8.1 Mobile Hero Gallery

#### Layout

- Single large hero image
- Aspect ratio: `3:4`
- Width: `calc(100vw - 32px)`
- Margin: `16px`
- Border radius: `12px–16px`
- No thumbnail rail

#### Image Content

The image should:

- Use editorial catalog photography
- Keep the garment clearly visible
- Avoid busy backgrounds
- Use warm neutral lighting
- Preserve product color accuracy

#### Overlay Elements

Inside image:

- Wishlist heart top-right
- Optional expand icon if zoom/detail view is supported

Overlay button:

- Size: `36px–40px`
- Background: `rgba(255,255,255,0.72)`
- Blur: `8px–10px`
- Border: subtle white border
- Icon color: `text-primary`

#### Carousel Dots

| Property | Value |
|---|---:|
| Dot size | `5px–6px` |
| Active dot width | `16px–20px` |
| Dot color inactive | `text-tertiary` at reduced opacity |
| Dot color active | `text-primary` |
| Placement | Centered below image |
| Gap | `6px` |

#### Behavior

- Swipe horizontally between images.
- Snap to each image.
- Dots update on swipe.
- Optional tap-to-zoom behavior.
- No hover-only interactions on mobile.

### 8.2 Desktop Gallery

#### Layout

- Main image: `3:4`
- Thumbnail column on the left
- Thumbnails size: `64px x 64px`
- Thumbnail radius: `8px`
- Main image radius: `12px`

#### Thumbnail States

| State | Style |
|---|---|
| Default | Opacity `0.7` |
| Active | Accent border + slight scale |
| Hover | Opacity `1` |

#### Behavior

- Click thumbnail to update main image.
- Desktop hover can trigger subtle zoom.
- No heavy overlay treatment.

## 9. Product Info Block

### 9.1 Content Order

The product info block must follow this order:

1. Brand
2. Product title
3. Metadata
4. Price
5. Rating
6. Try-on microcopy
7. Size selection
8. Product details accordion

### 9.2 Mobile Product Info Layout

#### Layout

- Side padding: `16px`
- Top margin after gallery: `20px–24px`
- Internal vertical gap: `8px–12px`

#### Content

Brand:

- Text: `BEWAKOOF®`
- Uppercase
- Letter spaced
- Small, secondary

Title:

- Text: `Women’s Black Graphic Printed Oversized Sweatshirt`
- Max 2 lines
- Ellipsis if needed

Metadata:

- Format: `Women · Black · Oversized`
- Secondary color

Price:

- Text: `₹889`
- Prominent
- No sale treatment unless required by merchant data

Rating:

- Stars + numeric rating
- Low visual weight
- Do not overpower price

Try-on microcopy:

- Text: `✦ See how it looks on you in real life`
- Small
- Secondary color
- Should reinforce Try-On without feeling promotional

### 9.3 Desktop Product Info Layout

Right column width:

- Approximately `420px–480px`

Title:

- Max 2 lines
- Ellipsis on overflow

Order:

1. Brand
2. Title
3. Metadata
4. Price
5. Rating
6. Size selection
7. Try-On CTA
8. Micro info
9. Accordion

## 10. Size Pills Component

### 10.1 Layout

#### Mobile

- Section header row:
  - Left: `Select Size`
  - Right: `Size Guide`
- Pills wrap if needed
- Max 5 per row when possible

#### Desktop

- Pills remain in row
- Max 5 per row

### 10.2 Dimensions

| Property | Value |
|---|---:|
| Height | `36px–40px` |
| Min width | `40px–48px` |
| Horizontal padding | `14px–16px` |
| Radius | `999px` |
| Gap | `8px` |

### 10.3 States

#### Default

- Background: transparent
- Border: `rgba(28, 26, 24, 0.12)`
- Text: `text-primary`

#### Hover

- Background: `accent-soft`
- Border: transparent or accent-soft

#### Selected

- Background: `accent-soft`
- Border: `accent-primary`
- Text: `text-primary`

#### Active

- Transform: `scale(0.98)`

#### Disabled

- Opacity: `0.35`
- Optional diagonal line
- Cursor: not allowed
- Should not be selectable

### 10.4 Behavior

- User can select one size at a time.
- If no size is selected and the user taps Try-On:
  - Scroll size section into view.
  - Show subtle validation pulse or shake.
  - Display optional helper text: `Please select a size to continue.`
- Selected size should persist during session.

## 11. CTA Buttons

### 11.1 Primary Button: Try This On

This is the most important PDP action.

#### Label

Mobile sticky label:

- `✦ Try This On`

Desktop label:

- `✦ Try This On You`

#### Dimensions

| Property | Mobile | Desktop |
|---|---:|---:|
| Height | `52px` | `48px–52px` |
| Radius | `12px` | `12px` |
| Font size | `13px–14px` | `14px` |
| Font weight | `700` | `700` |

#### Light Mode

- Background: `#1C1A18`
- Text: `#FFFFFF`

#### Dark Mode

- Background: `#F5F5F5`
- Text: `#121212`

#### Glass Layer

Use a subtle glass treatment only on or around the CTA.

Light:

- Overlay: `rgba(255,255,255,0.6)`
- Blur: `10px`

Dark:

- Overlay: `rgba(255,255,255,0.08)`
- Blur: `12px`

#### States

| State | Behavior |
|---|---|
| Hover | Slight brightness + subtle elevation |
| Active | `scale(0.98)` |
| Loading | Text changes to `Preparing Try-On...` |
| Disabled | `40%` opacity |

### 11.2 Secondary Button: Buy on Merchant

This action is secondary but must remain visible on mobile.

#### Label

- `Buy on Merchant`

#### Light Mode

- Background: `#FFFFFF`
- Text: `#1C1A18`
- Border: `rgba(28, 26, 24, 0.10)`

#### Dark Mode

- Background: `#202020`
- Text: `#F5F5F5`
- Border: `rgba(255,255,255,0.12)`

#### States

| State | Behavior |
|---|---|
| Hover | Slight elevation |
| Active | `scale(0.98)` |
| Disabled | `40%` opacity |

## 12. Mobile Sticky Bottom Action Bar

### 12.1 Purpose

The sticky bar ensures both primary and secondary product actions are always reachable.

The primary action remains visually dominant.

### 12.2 Layout

The mobile sticky bottom bar contains two side-by-side buttons:

| Position | Button | Width |
|---|---|---:|
| Left | Buy on Merchant | `44%` |
| Right | Try This On | `56%` |

#### Dimensions

| Property | Value |
|---|---:|
| Bar position | Fixed bottom |
| Bar width | `100%` |
| Bar padding | `12px 16px` |
| Safe-area padding | `calc(12px + env(safe-area-inset-bottom))` |
| Button height | `52px` |
| Button radius | `12px` |
| Button gap | `10px` |
| Top divider | `rgba(28, 26, 24, 0.06)` |

### 12.3 Visual Style

Light mode:

- Background: `rgba(246, 243, 238, 0.88)`
- Backdrop blur: `12px`
- Top border: subtle divider

Dark mode:

- Background: `rgba(18, 18, 18, 0.88)`
- Backdrop blur: `12px`
- Top border: `rgba(255,255,255,0.08)`

### 12.4 Behavior

- Always visible on mobile.
- Must not cover important page content.
- Page must include bottom padding of `96px–112px`.
- Try-On button is visually dominant.
- Buy button remains accessible but secondary.
- On tap:
  - Try-On validates selected size.
  - Buy opens merchant destination.
- During Try-On loading:
  - Disable both buttons or disable Try-On only.
  - Show loading label: `Preparing Try-On...`

## 13. Accordion Component

### 13.1 Sections

Required accordion rows:

1. Description
2. Fabric & Care
3. Fit Details

### 13.2 Layout

| Property | Value |
|---|---:|
| Row height | `44px–48px` |
| Divider | Subtle |
| Background | Transparent |
| Card wrapper | None |
| Icon | Chevron |
| Body text color | `text-secondary` |

### 13.3 Mobile Recommendation

The `Description` row should be open by default.

Default visible text:

- `Soft oversized sweatshirt with abstract graphic print and relaxed everyday fit.`

### 13.4 Behavior

| State | Behavior |
|---|---|
| Closed | Show row label + chevron |
| Open | Expand inline below row |
| Tap | Toggle open/closed |
| Multiple open | Allowed, unless product team prefers single-open behavior |

Recommended:

- Allow multiple sections to remain open.
- Use subtle height animation.
- Avoid layout jumpiness.

## 14. Complete the Look Carousel

### 14.1 Purpose

This section is for curated styling recommendations.

It should feel fashion-led rather than algorithmic.

Preferred section title:

- `Complete the look`

Alternative:

- `Pair it with`
- `Style it with`

### 14.2 Mobile Layout

Use a single horizontally swipeable row.

#### Card Sizing

| Property | Value |
|---|---:|
| Card width | `42vw` or `156px–168px` |
| Image aspect ratio | `3:4` |
| Image radius | `12px` |
| Gap | `12px` |
| Visible cards | `2.3–2.5` |
| Scroll snap | Mandatory |

The row must show a partial third card to indicate horizontal scrolling.

### 14.3 Product Types

Only show styling-relevant items:

- Trousers
- Jeans
- Shirts
- Sweatshirts
- Cargo pants
- Layering pieces

Avoid:

- Accessories
- Random products
- Unrelated recommendations

### 14.4 Card Content

Each card contains:

1. Product image
2. Wishlist icon on image
3. Product title
4. Price

Optional:

- Rating, but keep it low priority

Example:

- `Relaxed Fit Trousers`
- `₹2,990`

### 14.5 Behavior

- Horizontal swipe.
- Scroll snap to card.
- Wishlist tap fills heart.
- Card tap opens product.
- Active tap state: `scale(0.98)`.
- Do not use carousel arrows on mobile.

## 15. Similar Products Section

### 15.1 Purpose

This section supports product discovery but must remain lower priority than Complete the Look.

### 15.2 Mobile Layout

Use a two-column grid.

| Property | Value |
|---|---:|
| Columns | `2` |
| Gap | `12px` |
| Image aspect ratio | `3:4` |
| Image radius | `12px` |
| Card background | Transparent or elevated only if needed |

### 15.3 Header

Layout:

- Left: `Similar Products`
- Right: `View all`

Visual hierarchy:

- Section title: `18px`, `600`
- View all: `12px–13px`, tertiary

### 15.4 Card Content

Each card contains:

1. Product image
2. Wishlist icon
3. Product title
4. Price
5. Tiny rating row

Card title:

- Max 2 lines
- Ellipsis after overflow

Rating:

- Small
- Tertiary
- Should not compete with title or price

### 15.5 Behavior

- Tap card to open PDP.
- Tap heart to wishlist.
- Tap View all to open product listing.
- Cards have active scale state on touch.
- Avoid heavy hover-only effects on mobile.

## 16. Product Card Component

### 16.1 Dimensions

#### Desktop

| Property | Value |
|---|---:|
| Width | `200px–220px` |
| Image ratio | `3:4` |
| Radius | `12px` |

#### Mobile Carousel

| Property | Value |
|---|---:|
| Width | `156px–168px` or `42vw` |
| Image ratio | `3:4` |
| Radius | `12px` |

#### Mobile Grid

| Property | Value |
|---|---:|
| Width | `calc((100vw - 44px) / 2)` |
| Image ratio | `3:4` |
| Radius | `12px` |

### 16.2 Visual Style

- Image first
- Product text below image
- No heavy card background required
- Use elevated white surface only if image contrast needs support

Image:

- Rounded corners
- Object-fit cover
- Neutral background

Wishlist:

- Floating top-right
- Circular button
- Size: `28px–32px`
- Background: translucent white
- Icon size: `14px–16px`

### 16.3 States

| State | Behavior |
|---|---|
| Default | Static |
| Hover desktop | TranslateY `-2px` |
| Active | `scale(0.98)` |
| Wishlist active | Filled heart |
| Image loading | Soft skeleton placeholder |

## 17. Footer

### 17.1 Mobile Footer

The footer should be minimal.

Content:

- `REFLEKT`
- Tagline: `You Choose, We Reflekt.`
- Compact links:
  - Shop
  - Help
  - About

#### Style

| Property | Value |
|---|---:|
| Padding top | `32px` |
| Padding bottom | `112px+` |
| Text size | `11px–12px` |
| Background | `bg-secondary` or transparent |
| Divider | Optional subtle top border |

The footer must account for the sticky bottom action bar.

### 17.2 Desktop Footer

Desktop footer may include:

- Brand
- Social icons
- Shop links
- Help links
- About links
- Newsletter input

Keep footer quiet and low priority.

## 18. Interaction Behavior

### 18.1 Image Gallery

Mobile:

- Swipe horizontally.
- Snap to image.
- Dots update.
- Optional tap-to-zoom.

Desktop:

- Thumbnail click updates image.
- Hover zoom allowed.
- Expand icon can open image modal.

### 18.2 Size Selection

- One selected size at a time.
- Selected state is visually clear.
- If user proceeds without selecting size:
  - Scroll to size selection.
  - Show helper message.
  - Trigger subtle pulse/shake on pill row.

### 18.3 Try-On CTA

On tap:

1. Validate selected size.
2. Show loading state.
3. Launch try-on flow.
4. Preserve current PDP context.

Loading state:

- Label: `Preparing Try-On...`
- Disable repeated taps.
- Maintain button dimensions to prevent layout shift.

### 18.4 Buy on Merchant

On tap:

- Open merchant link.
- Prefer same tab or controlled webview depending on app shell.
- Keep label stable.
- If unavailable, disable with opacity `40%`.

### 18.5 Wishlist

On tap:

- Fill heart icon.
- Use subtle scale animation.
- Do not shift layout.
- If login required, open auth modal/sheet.

### 18.6 Accordion

- Tapping row toggles open state.
- Use soft height transition.
- Chevron rotates.
- Content expands inline.
- Avoid card-like backgrounds.

## 19. Accessibility Requirements

### 19.1 Tap Targets

Minimum tap target:

- `44px x 44px`

Applies to:

- Header icons
- Wishlist buttons
- Size pills
- CTA buttons
- Accordion rows
- Carousel cards

### 19.2 Contrast

Ensure:

- Primary text meets WCAG contrast on background.
- Secondary text remains readable.
- Disabled states are visually clear but not unreadable.

### 19.3 Screen Reader Labels

Required labels:

- Back button: `Go back`
- Search icon: `Search`
- Wishlist icon: `Add to wishlist`
- Selected wishlist: `Remove from wishlist`
- Size pill: `Select size M`
- Selected size: `Size M selected`
- Try-On CTA: `Try this product on`
- Buy CTA: `Buy on merchant`
- Accordion: `Expand Description`, `Collapse Description`

### 19.4 Keyboard Behavior

Desktop:

- All interactive elements must be focusable.
- Visible focus state required.
- Accordion should open with Enter/Space.
- Carousel should support arrow navigation if focused.

Focus style:

- Border or outline using `accent-primary`
- Avoid default blue outline if it breaks visual system, but do not remove focus indicator.

## 20. Motion Guidelines

Use minimal, functional motion.

### 20.1 Recommended Motion

| Interaction | Motion |
|---|---|
| Button active | `scale(0.98)` |
| Card hover desktop | `translateY(-2px)` |
| Wishlist tap | Small heart scale/fill |
| Accordion open | Height + opacity transition |
| Size validation | Subtle shake/pulse |
| Sticky header scroll | Background opacity transition |

### 20.2 Timing

| Motion | Duration |
|---|---:|
| Button active | `100ms–150ms` |
| Accordion expand | `180ms–220ms` |
| Header background change | `160ms–200ms` |
| Wishlist fill | `180ms` |
| Card hover | `150ms` |

Use easing:

- `ease-out`
- `cubic-bezier(0.2, 0.8, 0.2, 1)`

## 21. Mobile PDP Final Structure

The final mobile PDP should follow this structure:

```text
Floating Header

Hero Image Carousel

Product Info
- Brand
- Title
- Metadata
- Price
- Rating
- Try-on microcopy

Size Selection
- Select Size / Size Guide
- Size Pills

Product Details Accordion
- Description open
- Fabric & Care closed
- Fit Details closed

Complete the Look
- Horizontal carousel
- 2.3–2.5 cards visible

Similar Products
- Two-column grid

Footer

Sticky Bottom Action Bar
- Buy on Merchant
- ✦ Try This On
```

## 22. Desktop PDP Final Structure

The final desktop PDP should follow this structure:

```text
Header

Breadcrumb

Product Section
- Left: Thumbnail rail + main product image
- Right: Product info stack

Full-width Complete the Look

Full-width Similar Products

Footer
```

Desktop right column order:

```text
Brand
Title
Metadata
Price
Rating
Size Pills
Try-On CTA
Buy on Merchant
Accordion
```

## 23. Implementation Notes

### 23.1 Mobile-First Breakpoints

Recommended breakpoints:

| Breakpoint | Layout |
|---|---|
| `0px–767px` | Mobile single column |
| `768px–1023px` | Tablet single/two-column hybrid |
| `1024px+` | Desktop 12-column grid |

### 23.2 Sticky Bar Content Padding

Every mobile PDP page must include bottom padding to avoid sticky bar overlap.

Recommended:

- Main content bottom padding: `112px`
- Footer bottom padding: `128px`

### 23.3 Carousel Implementation

Complete the Look carousel should use:

- Horizontal overflow
- Scroll snap
- Hidden scrollbar if appropriate
- Partial third card visible

Recommended behavior:

- `scroll-snap-type: x mandatory`
- Each card: `scroll-snap-align: start`
- Row padding-right should allow final card to align comfortably

## 24. Final Quality Checklist

### Visual

- Product image is the strongest visual element.
- Page feels calm and premium.
- Sticky Try-On CTA is dominant but not aggressive.
- Buy button is visible but secondary.
- There is no marketplace clutter.
- Pairing section feels curated.
- Similar Products feels lower priority.

### Layout

- Mobile layout is single column.
- Desktop layout uses 12-column structure.
- Hero image uses `3:4`.
- Product cards use `3:4`.
- Complete the Look shows approximately 2.5 cards on mobile.
- Similar Products uses two columns on mobile.
- Sticky bar does not cover content.

### Interaction

- Image carousel swipes smoothly.
- Size selection is clear.
- Try-On validates size.
- Accordion opens smoothly.
- Wishlist interaction has feedback.
- Sticky bottom bar remains visible.

### Accessibility

- Tap targets are at least `44px`.
- Buttons have proper labels.
- Text contrast is acceptable.
- Keyboard focus is visible.
- Screen reader labels are present.

## 25. Summary

The PDP should deliver a refined fashion experience centered around Try-On.

The mobile version should feel:

- Immersive
- Thumb-friendly
- App-native
- Editorial
- Lightweight
- Intelligent

The desktop version should feel:

- Structured
- Calm
- Spacious
- Product-focused

The guiding design statement is:

> Calm surface + intelligent interaction.

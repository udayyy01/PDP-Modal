# REFLEKT / TRYOWN Web App Try-On Modal Component Specification

## 1. Purpose

This document defines the component specifications, typography, layout, responsive behavior, interaction behavior, states, and accessibility requirements for the REFLEKT / TRYOWN mobile web app Try-On modal.

The Try-On modal is the guided flow that opens when the user taps the PDP primary CTA:

> ✦ Try This On

The modal should feel like a focused, app-native try-on experience rather than a generic popup.

The primary user task is:

> Select yourself → preview the selected photo → generate the try-on result.

## 2. Core Experience Principle

The Try-On modal should behave differently on desktop and mobile.

### Desktop Mental Model

Desktop can use a large centered modal with a two-column layout:

- Left side: product preview
- Right side: try-on flow controls

### Mobile Mental Model

Mobile should use a full-screen guided sheet:

- Sticky top header
- Scrollable body
- Sticky bottom CTA
- Compact product context
- Saved-photo carousel
- Large selected-photo preview
- Upload card
- Guidance card
- Privacy reassurance

The mobile version should not copy the desktop modal literally.

It should translate the desktop confidence-building concept into a thumb-friendly mobile flow.

## 3. Design Direction

The modal should feel:

- Premium
- Calm
- Editorial
- Secure
- App-native
- Focused
- Lightweight
- Thumb-friendly

Avoid:

- Marketplace clutter
- Heavy shadows
- Dense desktop grids
- Side-by-side desktop layouts on mobile
- Multiple competing CTAs
- Overly technical loading messages
- Large empty states
- Aggressive promotional language

## 4. Design Tokens

### 4.1 Light Mode Tokens

| Token | Value | Usage |
|---|---:|---|
| `bg-primary` | `#F6F3EE` | Full-screen modal background |
| `bg-secondary` | `#EFEAE3` | Guidance card, soft surfaces |
| `bg-elevated` | `#FFFFFF` | Product card, upload card, preview card |
| `text-primary` | `#1C1A18` | Main headings, button text on light surfaces |
| `text-secondary` | `#6E675F` | Supporting text, helper copy |
| `text-tertiary` | `#A39B92` | Privacy note, metadata, low-priority text |
| `accent-primary` | `#8C6A4A` | Selected photo border, progress bar, active step |
| `accent-soft` | `#E8DED3` | Progress track, selected soft backgrounds |
| `success` | `#3E9B5F` | Checklist icons, success upload state |
| `error` | `#B84A3A` | Upload and validation error state |
| `cta-bg` | `#1C1A18` | Primary CTA background |
| `cta-text` | `#FFFFFF` | Primary CTA text |
| `glass-bg` | `rgba(246,243,238,0.88)` | Sticky header and bottom CTA area |
| `glass-border` | `rgba(28,26,24,0.06)` | Sticky surface dividers |
| `glass-blur` | `12px` | Header and bottom bar blur |

### 4.2 Dark Mode Tokens

| Token | Value | Usage |
|---|---:|---|
| `bg-primary` | `#121212` | Full-screen modal background |
| `bg-secondary` | `#1A1A1A` | Guidance card, soft surfaces |
| `bg-elevated` | `#202020` | Cards and elevated areas |
| `text-primary` | `#F5F5F5` | Main headings |
| `text-secondary` | `#A1A1A1` | Supporting text |
| `text-tertiary` | `#6B6B6B` | Privacy note, metadata |
| `accent-primary` | `#3A6B6B` | Active progress, selected states |
| `accent-soft` | `#223838` | Progress track, soft selected state |
| `success` | `#4CAF72` | Success icons |
| `error` | `#D46655` | Error states |
| `cta-bg` | `#F5F5F5` | Primary CTA background |
| `cta-text` | `#121212` | Primary CTA text |
| `glass-bg` | `rgba(18,18,18,0.88)` | Sticky header and bottom CTA area |
| `glass-border` | `rgba(255,255,255,0.08)` | Sticky surface dividers |
| `glass-blur` | `12px` | Header and bottom bar blur |

## 5. Modal Type and Responsive Behavior

## 5.1 Mobile Modal

Mobile uses a full-screen sheet.

| Property | Value |
|---|---:|
| Width | `100vw` |
| Height | `100dvh` |
| Background | `bg-primary` |
| Border radius | `0px` |
| Position | Fixed full-screen |
| Open animation | Slide up + fade |
| Close animation | Slide down + fade |
| Body scrolling | Enabled |
| Header | Sticky top |
| CTA | Sticky bottom |

Mobile should feel like a native app screen, not a popup.

## 5.2 Desktop Modal

Desktop may use a centered modal over a dimmed PDP background.

| Property | Value |
|---|---:|
| Max width | `1080px–1120px` |
| Height | `auto`, max `90vh` |
| Radius | `16px` |
| Background | `bg-elevated` |
| Overlay | `rgba(0,0,0,0.48)` |
| Layout | Two columns |
| Left column | Product preview |
| Right column | Step flow |

Desktop two-column structure:

```text
Left: Product preview image + product mini card
Right: Stepper + photo selection + upload + tips + CTA
```

## 6. Mobile Layout Structure

The final mobile Try-On modal should follow this order:

```text
Sticky Header

Step Progress

Product Context Card

Try this on you Section

Saved Photos Carousel

Selected Photo Preview

Upload New Photo Card

For Best Results Card

Privacy Note

Sticky Bottom CTA
```

## 7. Mobile Header Component

### 7.1 Purpose

The header provides modal orientation and dismissal controls.

### 7.2 Layout

```text
←  TRY ON                                      ✕
```

Alternative layout:

```text
←  Try On                                     ✕
```

### 7.3 Specs

| Property | Value |
|---|---:|
| Height | `56px–64px` |
| Position | Sticky top |
| Z-index | Above modal body |
| Padding | `0 16px` |
| Background | `glass-bg` |
| Backdrop blur | `glass-blur` |
| Bottom divider | `1px solid glass-border` |
| Icon button size | `40px x 40px` |
| Icon size | `18px–20px` |
| Title size | `14px–16px` |
| Title weight | `700` |
| Letter spacing | `0.08em–0.14em` if uppercase |

### 7.4 Behavior

- Header remains sticky while body scrolls.
- Back arrow returns to the previous Try-On step when possible.
- On step 1, back arrow may close the modal or return to PDP depending on product decision.
- Close icon exits the Try-On flow.
- If user has unsaved generated results or active generation, confirm before closing.

## 8. Step Progress Component

### 8.1 Purpose

Shows the user's current location in the Try-On flow without overcrowding the mobile screen.

### 8.2 Mobile Pattern

Use:

```text
Step 1 of 4
Select Yourself
[progress bar]
```

Avoid using the full desktop numbered stepper on mobile.

### 8.3 Steps

| Step | Label | Purpose |
|---:|---|---|
| 1 | Select Yourself | Choose or upload a user photo |
| 2 | Generating | Generate try-on output |
| 3 | Result | View generated try-on result |
| 4 | Refine Pose | Adjust pose or regenerate |

### 8.4 Specs

| Element | Size / Value |
|---|---:|
| Container padding | `16px 16px 0` |
| Step label font size | `12px` |
| Step label weight | `500` |
| Step label color | `text-secondary` |
| Step title font size | `18px–20px` |
| Step title weight | `650–700` |
| Step title color | `text-primary` |
| Progress bar height | `4px` |
| Progress bar radius | `999px` |
| Progress fill | `accent-primary` |
| Progress track | `accent-soft` |
| Top margin before progress | `10px–12px` |

### 8.5 Behavior

- Progress updates per step.
- Progress should animate softly between steps.
- Do not show future step labels on mobile.
- Use screen-reader text to announce current step.

## 9. Product Context Card

### 9.1 Purpose

The user already saw the product on the PDP. Inside the Try-On flow, the product should remain visible as context but should not dominate the task.

### 9.2 Layout

```text
┌────────────────────────────┐
│ [thumb] Product title      │
│         Brand · Price      │
└────────────────────────────┘
```

### 9.3 Specs

| Property | Value |
|---|---:|
| Margin top | `16px–20px` |
| Margin horizontal | `16px` |
| Height | `88px–96px` |
| Background | `bg-elevated` |
| Radius | `12px–14px` |
| Padding | `12px` |
| Gap | `12px` |
| Thumbnail width | `64px–72px` |
| Thumbnail aspect ratio | `3:4` |
| Thumbnail radius | `8px–10px` |
| Title size | `13px–14px` |
| Title weight | `600` |
| Title line height | `18px–20px` |
| Title max lines | `2` |
| Metadata size | `12px–13px` |
| Metadata color | `text-secondary` |

### 9.4 Content

Example:

```text
Women’s Black Graphic Printed Oversized Sweatshirt
BEWAKOOF® · ₹889
```

### 9.5 Behavior

- Tapping the product card may collapse the modal and return to PDP, or do nothing.
- Recommended: non-interactive card unless product team wants explicit return behavior.
- Card should not open a new PDP inside the modal.

## 10. Try This On You Section

### 10.1 Purpose

Introduces the core task: selecting or uploading the user's photo.

### 10.2 Layout

```text
Try this on you
Select a photo or upload a new one
```

### 10.3 Specs

| Element | Value |
|---|---:|
| Section margin top | `24px` |
| Horizontal padding | `16px` |
| Heading size | `22px–24px` |
| Heading weight | `650–700` |
| Heading line height | `28px–30px` |
| Heading color | `text-primary` |
| Helper size | `13px–14px` |
| Helper line height | `18px–20px` |
| Helper color | `text-secondary` |
| Helper margin top | `4px` |

## 11. Saved Photos Carousel

### 11.1 Purpose

Allows users to quickly choose from previously uploaded or saved photos.

### 11.2 Layout

```text
[photo selected] [photo] [photo] [photo] [+ View more]
```

### 11.3 Specs

| Property | Value |
|---|---:|
| Container margin top | `14px–16px` |
| Horizontal padding | `16px` |
| Scroll direction | Horizontal |
| Scroll snap | Optional, recommended |
| Gap | `10px–12px` |
| Thumbnail width | `72px–80px` |
| Thumbnail aspect ratio | `3:4` |
| Thumbnail radius | `10px–12px` |
| Selected border | `2px solid accent-primary` |
| Selected check size | `20px–22px` |
| Check position | Top right, `6px` inset |
| Check background | `accent-primary` |
| Check icon color | White |
| View more tile border | Dashed `rgba(28,26,24,0.14)` |
| View more tile text size | `11px–12px` |

### 11.4 Behavior

- Row scrolls horizontally.
- A partial final item should be visible to suggest swiping.
- Tapping a thumbnail selects it.
- Selected thumbnail displays a border and checkmark.
- Selected photo preview updates immediately.
- CTA becomes active when a valid photo is selected.
- `View more` opens a saved-photo picker screen or bottom sheet.

### 11.5 States

| State | Visual Treatment |
|---|---|
| Default | Normal image thumbnail |
| Selected | Accent border + check badge |
| Pressed | `scale(0.98)` |
| Loading | Skeleton placeholder |
| Error | Muted tile with retry icon |
| Empty | Show upload card prominently |

## 12. Selected Photo Preview

### 12.1 Purpose

The selected photo preview gives users confidence before generation.

It answers:

> Is this the correct photo I am about to use?

This is the mobile translation of the desktop modal's large visual preview behavior.

### 12.2 Placement

Place immediately after the Saved Photos Carousel.

```text
Saved Photos Carousel
Selected Photo Preview
Upload New Photo
```

### 12.3 Layout

```text
Selected photo

┌────────────────────────────┐
│                            │
│     selected user image     │
│                            │
└────────────────────────────┘

Change Photo                         Remove
```

### 12.4 Specs

| Property | Value |
|---|---:|
| Container margin top | `16px–18px` |
| Horizontal padding | `16px` |
| Label size | `13px–14px` |
| Label weight | `600` |
| Label color | `text-primary` |
| Label margin bottom | `8px` |
| Card background | `bg-elevated` |
| Card padding | `8px` |
| Card radius | `16px` |
| Image width | `100%` |
| Image aspect ratio | `3:4` |
| Image max height | `320px–380px` |
| Image object-fit | `cover` |
| Image radius | `12px–14px` |
| Border | `1px solid rgba(140,106,74,0.25)` when selected |
| Optional glow | Very subtle warm accent only |
| Actions margin top | `8px–10px` |
| Action text size | `12px–13px` |
| Action weight | `500–600` |

### 12.5 Action Layout

```text
Change Photo                                      Remove
```

| Action | Style |
|---|---|
| Change Photo | `accent-primary`, medium weight |
| Remove | `text-tertiary` or muted error color if destructive emphasis is needed |

### 12.6 Behavior

When a saved photo is selected:

1. Thumbnail selected state updates.
2. Preview image updates instantly.
3. CTA becomes active.
4. Preview remains visible.

When a newly uploaded photo succeeds:

1. Add uploaded photo to the carousel.
2. Place it first or mark it as most recent.
3. Select it automatically.
4. Update preview image.
5. Show temporary success message: `Photo added`.
6. Enable CTA.

When `Change Photo` is tapped:

- Scroll or focus user back to saved photos carousel, or
- Open saved-photo picker sheet.

When `Remove` is tapped:

- Clear selected photo.
- Remove selected thumbnail state.
- Show empty preview state or collapse preview based on product decision.
- Disable CTA.

### 12.7 Empty State

If no photo is selected, use a compact empty state.

```text
Selected photo

┌────────────────────────────┐
│      No photo selected      │
│ Select a saved photo or     │
│ upload a new one            │
└────────────────────────────┘
```

Empty state specs:

| Property | Value |
|---|---:|
| Height | `160px–200px` |
| Background | `bg-elevated` |
| Border | Dashed `rgba(28,26,24,0.12)` |
| Text size | `13px–14px` |
| Text color | `text-secondary` |
| Icon | Optional user/photo icon |

## 13. Upload New Photo Card

### 13.1 Purpose

Allows user to add a new image from camera, photo library, or files.

### 13.2 Layout

```text
┌────────────────────────────┐
│ ↑ Upload New Photo         │
│   JPG, PNG up to 10MB      │
│   Use camera or library    │
└────────────────────────────┘
```

### 13.3 Specs

| Property | Value |
|---|---:|
| Margin top | `18px–20px` |
| Horizontal padding | `16px` |
| Height | `88px–104px` |
| Background | `bg-elevated` |
| Radius | `14px` |
| Border | Dashed `rgba(28,26,24,0.14)` |
| Padding | `14px–16px` |
| Icon size | `22px–24px` |
| Title size | `14px` |
| Title weight | `600` |
| Subtext size | `12px–13px` |
| Subtext color | `text-secondary` |
| Microcopy size | `11px–12px` |
| Microcopy color | `text-tertiary` |

### 13.4 Behavior

On tap:

- Open native file picker.
- Prefer native options where available:
  - Camera
  - Photo Library
  - Files

Accepted formats:

- JPG
- PNG

Maximum size:

- `10MB`

### 13.5 Upload States

| State | Label / Behavior |
|---|---|
| Default | `Upload New Photo` |
| Pressed | `scale(0.98)` |
| Uploading | `Uploading photo...` + progress indicator |
| Success | `Photo added` |
| Error | `Couldn’t upload photo. Try another image.` |
| Unsupported file | `Please upload a JPG or PNG image.` |
| Too large | `Image must be under 10MB.` |

## 14. For Best Results Card

### 14.1 Purpose

Gives users guidance to improve try-on quality.

### 14.2 Layout

```text
For best results

✓ Use a clear, front-facing photo
✓ Keep your upper body visible
✓ Ensure good lighting
✓ Avoid baggy clothing or obstructions
```

### 14.3 Specs

| Property | Value |
|---|---:|
| Margin top | `18px–20px` |
| Horizontal padding | `16px` |
| Background | `bg-secondary` |
| Radius | `14px` |
| Padding | `14px–16px` |
| Heading size | `13px–14px` |
| Heading weight | `700` |
| Tip text size | `12px–13px` |
| Tip line height | `18px` |
| Icon size | `14px–16px` |
| Icon color | `success` |
| Tip gap | `8px` |

### 14.4 Behavior

- Static guidance card.
- No required interaction.
- Optional `View all tips` if guidance becomes longer.
- Keep guidance compact.

## 15. Privacy Note

### 15.1 Purpose

Reassures the user before submitting their photo for Try-On generation.

### 15.2 Text

Recommended copy:

```text
Your photos are private and only used to generate your try-on.
```

Optional longer copy:

```text
Your photos are private and secure. We only use them to generate your try-on.
```

### 15.3 Specs

| Property | Value |
|---|---:|
| Margin top | `16px–18px` |
| Horizontal padding | `16px` |
| Bottom margin before sticky CTA | `96px–112px` |
| Text size | `11px–12px` |
| Line height | `16px–18px` |
| Color | `text-tertiary` |
| Alignment | Center or left aligned |
| Icon | Lock icon, `12px–14px` |

### 15.4 Behavior

- Static reassurance text.
- Should remain visible before the user reaches CTA.
- May also be repeated in tiny form inside sticky CTA region if needed.

## 16. Sticky Bottom CTA

### 16.1 Purpose

The CTA starts Try-On generation and must remain reachable at all times on mobile.

### 16.2 Layout

```text
┌────────────────────────────┐
│      ✦ Try This Look        │
└────────────────────────────┘
```

### 16.3 Sticky Bar Specs

| Property | Value |
|---|---:|
| Position | Fixed bottom |
| Width | `100%` |
| Background | `glass-bg` |
| Backdrop blur | `glass-blur` |
| Top border | `1px solid glass-border` |
| Padding | `12px 16px` |
| Safe area | `calc(12px + env(safe-area-inset-bottom))` |
| Z-index | Above modal body |

### 16.4 Button Specs

| Property | Value |
|---|---:|
| Height | `52px` |
| Width | `100%` |
| Radius | `12px` |
| Background | `cta-bg` |
| Text color | `cta-text` |
| Text size | `14px` |
| Text weight | `700` |
| Icon | Sparkle icon before label |

### 16.5 CTA Labels

| State | Label |
|---|---|
| No photo selected | `Select a photo to continue` |
| Ready | `✦ Try This Look` |
| Loading | `Generating Try-On...` |
| Error | `Try Again` |

### 16.6 Behavior

When no photo is selected:

- Button is disabled.
- Opacity: `40%`.
- Tapping disabled button may scroll to photo selection and show helper text.

When a photo is selected:

- Button becomes active.
- Tapping starts generation.
- Move to Step 2.

When loading:

- Disable repeated taps.
- Maintain button height and width.
- Show stable loading label.

## 17. Step 1: Select Yourself

### 17.1 Full Mobile Layout

```text
Sticky Header
← TRY ON                                      ✕

Step 1 of 4
Select Yourself
[25% progress bar]

Product Context Card
[thumbnail] Women’s Black Graphic Printed Oversized Sweatshirt
            BEWAKOOF® · ₹889

Try this on you
Select a photo or upload a new one

Saved Photos Carousel
[selected photo] [photo] [photo] [photo] [+ View more]

Selected photo
[large 3:4 selected photo preview]
Change Photo                              Remove

Upload New Photo
JPG, PNG up to 10MB
Use camera or photo library

For best results
✓ Use a clear, front-facing photo
✓ Keep your upper body visible
✓ Ensure good lighting
✓ Avoid baggy clothing or obstructions

🔒 Your photos are private and only used to generate your try-on.

Sticky CTA
[ ✦ Try This Look ]
```

### 17.2 Required Behaviors

- User must select or upload a photo before continuing.
- Selected photo must be shown as a large preview.
- CTA must reflect selected/unselected state.
- Upload success automatically selects the new photo.
- User can change or remove selected photo.

## 18. Step 2: Generating

### 18.1 Purpose

Step 2 reassures the user that generation is happening and prevents duplicate actions.

### 18.2 Layout

```text
Sticky Header
← TRY ON                                      ✕

Step 2 of 4
Generating your look
[50% progress bar]

Preview Summary
[product thumbnail] + [selected user photo]

Creating your try-on...
This usually takes a few seconds.

[soft shimmer / progress animation]

Keep this page open while we generate your result.
```

### 18.3 Specs

| Element | Value |
|---|---:|
| Main heading | `22px–24px`, `650–700` |
| Helper text | `13px–14px`, `text-secondary` |
| Animation size | `56px–72px` |
| Summary card radius | `14px` |
| Summary card background | `bg-elevated` |

### 18.4 Behavior

- Generation starts after Step 1 CTA.
- CTA changes to loading state or disappears in favor of generation state.
- Prevent duplicate generation.
- If user closes during generation, show confirmation.
- On success, move to Step 3.
- On failure, show error state with retry.

### 18.5 Error State

```text
We couldn’t generate your try-on.
Please try again with a clearer photo.

[Try Again]
[Choose Another Photo]
```

## 19. Step 3: Result

### 19.1 Purpose

Shows generated try-on result as the reward moment.

### 19.2 Layout

```text
Sticky Header
← TRY ON                                      ✕

Step 3 of 4
Result
[75% progress bar]

[large generated try-on image]

How does it look?
[Refine Pose] [Save]
```

### 19.3 Result Image Specs

| Property | Value |
|---|---:|
| Horizontal margin | `16px` |
| Aspect ratio | `3:4` |
| Radius | `16px` |
| Background | `bg-elevated` |
| Object fit | `cover` |
| Max height | `70vh` |

### 19.4 Actions

Recommended bottom actions:

| Action | Priority |
|---|---|
| Refine Pose | Primary |
| Save Image | Secondary |
| Buy on Merchant | Optional tertiary |

Avoid placing too many actions on the result screen.

### 19.5 Behavior

- Generated image loads with soft fade-in.
- User can save image.
- User can refine pose.
- User can return to photo selection if needed.
- Preserve result when navigating to Step 4.

## 20. Step 4: Refine Pose

### 20.1 Purpose

Allows the user to improve the generated result with a better pose or alternate photo.

### 20.2 Layout

```text
Step 4 of 4
Refine Pose
[100% progress bar]

Choose a better pose
[pose 1] [pose 2] [pose 3]

Or upload another photo

[Regenerate]
```

### 20.3 Behavior

- Pose selection updates selected pose state.
- Regenerate uses selected pose/photo.
- Previous result should remain accessible.
- User should be able to return to result without losing work.

## 21. Desktop Modal Layout

Desktop can use the current modal structure with refinements.

### 21.1 Desktop Structure

```text
Modal Header
TRY ON                                      X

Left Column
- Large product preview image
- Product mini card

Right Column
- Numbered stepper
- Step title
- Saved photo thumbnails
- Upload New Photo
- For Best Results guidance
- CTA

Footer Privacy Note
```

### 21.2 Desktop Specs

| Property | Value |
|---|---:|
| Modal max width | `1080px–1120px` |
| Modal radius | `16px` |
| Modal max height | `90vh` |
| Column gap | `24px` |
| Left column width | `40%–45%` |
| Right column width | `55%–60%` |
| Product preview ratio | `3:4` |
| Header height | `64px` |
| Footer height | `40px–48px` |

### 21.3 Desktop Behavior

- Center modal over dimmed PDP.
- Close icon dismisses modal.
- Stepper shows all 4 steps horizontally.
- Product preview remains fixed while right column content changes.
- CTA is inside right column, not sticky unless content scrolls.

## 22. Typography Summary

### 22.1 Mobile Typography

| Element | Size | Weight | Line Height | Color |
|---|---:|---:|---:|---|
| Header title | `14px–16px` | `700` | `20px` | `text-primary` |
| Step label | `12px` | `500` | `16px` | `text-secondary` |
| Step title | `18px–20px` | `650–700` | `24px–26px` | `text-primary` |
| Main section heading | `22px–24px` | `650–700` | `28px–30px` | `text-primary` |
| Helper text | `13px–14px` | `400` | `18px–20px` | `text-secondary` |
| Product title | `13px–14px` | `600` | `18px–20px` | `text-primary` |
| Product metadata | `12px–13px` | `400` | `16px–18px` | `text-secondary` |
| Preview label | `13px–14px` | `600` | `18px` | `text-primary` |
| Action text | `12px–13px` | `500–600` | `18px` | `accent-primary` |
| Upload title | `14px` | `600` | `18px` | `text-primary` |
| Upload subtext | `12px–13px` | `400` | `16px–18px` | `text-secondary` |
| Tip heading | `13px–14px` | `700` | `18px` | `text-primary` |
| Tip text | `12px–13px` | `400` | `18px` | `text-secondary` |
| Privacy note | `11px–12px` | `400` | `16px–18px` | `text-tertiary` |
| CTA text | `14px` | `700` | `18px` | `cta-text` |

### 22.2 Desktop Typography

| Element | Size | Weight | Line Height |
|---|---:|---:|---:|
| Modal header title | `14px–16px` | `700` | `20px` |
| Stepper label | `12px–13px` | `500` | `18px` |
| Step title | `22px–24px` | `650–700` | `30px` |
| Helper text | `13px–14px` | `400` | `20px` |
| Product card title | `12px–13px` | `500–600` | `18px` |
| CTA text | `14px` | `700` | `18px` |

## 23. Spacing Summary

### 23.1 Mobile Spacing

| Use Case | Value |
|---|---:|
| Page horizontal padding | `16px` |
| Header horizontal padding | `16px` |
| Between header and progress | `16px` |
| Product card top margin | `16px–20px` |
| Section top margin | `24px` |
| Carousel top margin | `14px–16px` |
| Preview top margin | `16px–18px` |
| Upload card top margin | `18px–20px` |
| Guidance top margin | `18px–20px` |
| Privacy top margin | `16px–18px` |
| Bottom content padding | `112px` |
| Sticky CTA padding | `12px 16px` |

### 23.2 Desktop Spacing

| Use Case | Value |
|---|---:|
| Modal padding | `24px` |
| Column gap | `24px` |
| Header padding | `24px` |
| Right column internal gap | `16px–20px` |
| Photo thumbnail gap | `10px–12px` |
| CTA top margin | `16px` |

## 24. Accessibility Requirements

### 24.1 Tap Targets

All interactive elements must have minimum tap target:

```text
44px x 44px
```

Applies to:

- Back button
- Close button
- Photo thumbnails
- View more tile
- Upload card
- Change Photo
- Remove
- CTA
- Result actions

### 24.2 Screen Reader Labels

Required labels:

| Element | Label |
|---|---|
| Back button | `Go back` |
| Close button | `Close try-on` |
| Step progress | `Step 1 of 4, Select Yourself` |
| Product card | `Trying on Women's Black Graphic Printed Oversized Sweatshirt` |
| Photo thumbnail | `Select saved photo` |
| Selected thumbnail | `Selected photo` |
| View more tile | `View more saved photos` |
| Upload card | `Upload new photo` |
| Change Photo | `Change selected photo` |
| Remove | `Remove selected photo` |
| CTA ready | `Try this look` |
| CTA disabled | `Select a photo to continue` |
| Result image | `Generated try-on result` |

### 24.3 Keyboard Behavior

Desktop and tablet must support:

- Tab navigation
- Enter/Space to activate buttons
- Escape to close modal
- Focus trap inside modal
- Return focus to PDP CTA after close

### 24.4 Focus Style

Use a visible focus state:

- Outline or border using `accent-primary`
- Minimum `2px`
- Do not remove focus indicator

## 25. Motion Guidelines

Use subtle functional motion.

| Interaction | Motion | Duration |
|---|---|---:|
| Modal open | Slide up + fade | `220ms–280ms` |
| Modal close | Slide down + fade | `180ms–220ms` |
| Button press | `scale(0.98)` | `100ms–150ms` |
| Thumbnail select | Border/check fade in | `120ms–160ms` |
| Preview image update | Crossfade | `160ms–220ms` |
| Progress update | Width transition | `180ms–220ms` |
| Upload success | Soft check animation | `180ms` |
| Result image load | Fade in | `220ms` |

Recommended easing:

```text
cubic-bezier(0.2, 0.8, 0.2, 1)
```

Avoid:

- Bouncy animations
- Long loading animations
- Distracting transitions
- Motion that shifts layout unexpectedly

## 26. Validation and Error Handling

### 26.1 No Photo Selected

If user taps CTA with no selected photo:

- Keep user on Step 1.
- Scroll/focus to photo carousel or upload card.
- Show helper text:

```text
Please select or upload a photo to continue.
```

- CTA remains disabled or temporarily shows disabled helper label.

### 26.2 Upload Error

Common errors:

| Error | Message |
|---|---|
| File too large | `Image must be under 10MB.` |
| Unsupported type | `Please upload a JPG or PNG image.` |
| Upload failed | `Couldn’t upload photo. Try another image.` |
| Poor image quality | `Try a clearer, front-facing photo for better results.` |

### 26.3 Generation Error

Message:

```text
We couldn’t generate your try-on.
Please try again with a clearer photo.
```

Actions:

```text
Try Again
Choose Another Photo
```

## 27. Final Quality Checklist

### 27.1 Mobile Layout

- Full-screen sheet, not centered popup.
- Sticky header is always visible.
- Sticky bottom CTA is always reachable.
- Product card is compact.
- Saved photos are horizontally swipeable.
- Selected photo preview is large and clear.
- Upload card is visible and easy to tap.
- Tips card is compact.
- Privacy note is visible before action.
- Content has bottom padding so CTA does not cover it.

### 27.2 Component Behavior

- Selecting a thumbnail updates the large preview.
- Uploading a new photo selects it automatically.
- Removing a photo disables CTA.
- CTA validates required photo.
- Generation prevents duplicate taps.
- Result screen preserves generated image.
- Refine flow preserves previous result.

### 27.3 Visual Quality

- Premium matte surfaces.
- Minimal shadows.
- Warm neutral palette.
- Calm editorial spacing.
- Clear hierarchy.
- No marketplace clutter.
- No desktop side-by-side layout on mobile.

### 27.4 Accessibility

- Tap targets are at least `44px`.
- Modal traps focus on desktop.
- Escape closes modal on desktop.
- Screen reader labels are present.
- Focus states are visible.
- Progress is announced accessibly.

## 28. Summary

The Try-On modal should be a focused guided flow.

On desktop, it can remain a centered two-column modal.

On mobile, it should become a full-screen app-like sheet with:

1. Sticky header
2. Simple progress indicator
3. Compact product context
4. Photo selection carousel
5. Large selected-photo preview
6. Upload card
7. Best-results guidance
8. Privacy reassurance
9. Sticky CTA

The most important mobile improvement is:

> Do not rely only on thumbnails. Always show the selected try-on photo as a larger preview before generation.

This makes the flow clearer, more trustworthy, and closer to the desktop mental model while remaining mobile-native.

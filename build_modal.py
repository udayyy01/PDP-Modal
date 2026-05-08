#!/usr/bin/env python3
"""Add modal HTML to index.html and link modal.css/modal.js."""

CHECK = '<svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>'
CLOSE = '<svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>'
SPARKLE = '<svg viewBox="0 0 24 24"><path d="M12 2l2.4 7.2L22 12l-7.6 2.8L12 22l-2.4-7.2L2 12l7.6-2.8z" stroke-linejoin="round"/></svg>'
UPLOAD = '<svg viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>'
PLUS = '<svg viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>'
ARROW_LEFT = '<svg viewBox="0 0 24 24"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>'
CHEV_RIGHT = '<svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg>'
HEART = '<svg viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>'
DOWNLOAD = '<svg viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>'
REFRESH = '<svg viewBox="0 0 24 24"><polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/></svg>'
EDIT = '<svg viewBox="0 0 24 24"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>'
LOCK = '<svg viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>'
BODY = '<svg viewBox="0 0 24 24"><circle cx="12" cy="4" r="2.5" /><line x1="12" y1="6.5" x2="12" y2="16"/><line x1="8" y1="10" x2="16" y2="10"/><line x1="12" y1="16" x2="8" y2="22"/><line x1="12" y1="16" x2="16" y2="22"/></svg>'
CLOUD_UP = '<svg viewBox="0 0 24 24"><path d="M12 16V8"/><polyline points="8 12 12 8 16 12"/><circle cx="12" cy="12" r="10"/></svg>'
POSE = '<svg viewBox="0 0 24 24"><circle cx="12" cy="4" r="2"/><path d="M16 22l-2-6h-4l-2 6"/><path d="M8 10l-3 3"/><path d="M16 10l3 3"/><line x1="12" y1="6" x2="12" y2="16"/></svg>'
CLOCK = '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>'

GREEN_CHECK = '<svg viewBox="0 0 24 24" fill="#2D9D4E" stroke="none"><circle cx="12" cy="12" r="12"/><polyline points="7 12 10.5 15.5 17 9" stroke="#fff" stroke-width="2.5" fill="none"/></svg>'

faces = [f'images/model_face_{i}.png' for i in range(1, 6)]
poses = [f'images/pose_ref_{i}.png' for i in range(1, 6)]

def selector_cards(items, attr, selected=0):
    h = ''
    for i, src in enumerate(items):
        sel = ' selected' if i == selected else ''
        h += f'''<div class="selector-card{sel}" {attr}="{i}">
<img src="{src}" alt="Option {i+1}" loading="lazy">
<div class="selector-card__check">{CHECK}</div></div>\n'''
    h += f'''<div class="selector-card selector-card--more">{PLUS}<span>Upload</span></div>'''
    return h

modal_html = f'''
<!-- TRY-ON MODAL -->
<div class="modal-overlay" id="tryon-overlay">
<div class="modal">

<!-- Header -->
<div class="modal__header desktop-only">
<span class="modal__title">Try On</span>
<button class="modal__close" id="modal-close" aria-label="Close">{CLOSE}</button>
</div>

<!-- Mobile Header (Hidden on Desktop) -->
<div class="mobile-only modal-mobile-header">
<button class="mobile-icon-btn" id="mobile-modal-back" aria-label="Back">{ARROW_LEFT}</button>
<span class="mobile-header-title">TRY ON</span>
<button class="mobile-icon-btn" id="mobile-modal-close" aria-label="Close">{CLOSE}</button>
</div>

<!-- Body -->
<div class="modal__body">

<!-- Left Panel -->
<div class="modal__left">
<div class="modal__product-image">
<img src="images/hero_product.png" alt="Product" id="modal-product-img">
</div>
<div class="modal__product-card">
<div class="modal__product-card-thumb"><img src="images/hero_product.png" alt=""></div>
<div class="modal__product-card-info">
<div class="modal__product-card-name">Women's Black Graphic<br>Printed Oversized Sweatshirt</div>
</div>
<div class="modal__product-card-price">₹889</div>
</div>
</div>

<!-- Right Panel -->
<div class="modal__right">

<!-- Stepper -->
<div class="stepper desktop-only">
<div class="stepper__step active"><div class="stepper__circle">1</div><span class="stepper__label">Select Yourself</span></div>
<div class="stepper__line"></div>
<div class="stepper__step upcoming"><div class="stepper__circle">2</div><span class="stepper__label">Generating</span></div>
<div class="stepper__line"></div>
<div class="stepper__step upcoming"><div class="stepper__circle">3</div><span class="stepper__label">Result</span></div>
<div class="stepper__line"></div>
<div class="stepper__step upcoming"><div class="stepper__circle">4</div><span class="stepper__label">Refine Pose</span></div>
</div>

<!-- Mobile Step Progress (Hidden on Desktop) -->
<div class="mobile-only mobile-step-progress" id="mobile-step-progress-1">
<div class="mobile-step-label">Step 1 of 4</div>
<div class="mobile-step-title-row">
  <div class="mobile-step-title">Select Yourself</div>
  <div class="mobile-step-percent">25%</div>
</div>
<div class="mobile-step-bar-track"><div class="mobile-step-bar-fill" style="width: 25%"></div></div>
</div>

<!-- STEP 1: Select Yourself -->
<div class="step-panel active" data-step="1">
<div><div class="step-heading">Try this on you</div>
<div class="step-subheading">Select a photo or upload a new one</div></div>
<!-- Mobile Selected Photo Card (Hidden on Desktop) -->
<div class="mobile-only mobile-photo-card" id="mobile-photo-preview-container" style="display: none;">
<div class="mobile-photo-preview-label">Selected photo</div>
<div class="mobile-photo-preview">
<img src="" alt="Selected Photo" id="mobile-selected-img">
</div>
</div>

<div class="selector-grid" id="photo-selector-grid">{selector_cards(faces, 'data-photo')}</div>

<div class="mobile-guidance-tags">
  <div class="mobile-guidance-tag">Good lighting</div>
  <div class="mobile-guidance-tag">Clear face</div>
  <div class="mobile-guidance-tag">Neutral BG</div>
</div>

<div class="sticky-bottom-cta-wrapper">
<button class="modal-cta modal-cta--pill" id="tryon-cta-btn" disabled style="opacity: 0.4;">{SPARKLE}<span>Try This Look</span></button>
</div>
</div>

<!-- STEP 2: Generating -->
<div class="step-panel" data-step="2">
<div class="generating-view">
<div class="generating-spinner">
<div class="generating-spinner__arc"></div>
{SPARKLE}
</div>
<div class="generating-title">Generating your look...</div>
<div class="generating-dynamic-text" id="generating-dynamic-text">Uploading your photo...</div>
</div>
</div>

<!-- STEP 3: Result -->
<div class="step-panel" data-step="3">
  
<div class="mobile-result-hero">
  <img src="images/hero_product.png" alt="Generated Look">
</div>

<div class="mobile-result-actions">
  <button class="mobile-icon-action">{DOWNLOAD}</button>
  <button class="mobile-icon-action">{UPLOAD}</button>
  <button class="mobile-icon-action" id="action-save-look">{HEART}</button>
</div>

<div class="sticky-bottom-cta-wrapper" style="display: flex; flex-direction: column; gap: 8px;">
  <button class="modal-cta modal-cta--outline modal-cta--pill" id="action-change-pose">{POSE}<span>Change Pose</span></button>
  <button class="modal-cta modal-cta--pill" id="action-try-another">{REFRESH}<span>Try Another Photo</span></button>
</div>
</div>

<!-- STEP 4: Refine Pose -->
<div class="step-panel" data-step="4">
<button class="back-link" id="back-to-result">{ARROW_LEFT}<span>Back</span></button>
<div><div class="step-heading">Refine your pose</div>
<div class="step-subheading">Select a pose or upload your own</div></div>
<div class="selector-grid">{selector_cards(poses, 'data-pose')}</div>
<div class="mobile-guidance-tags">
  <div class="mobile-guidance-tag">Full-body</div>
  <div class="mobile-guidance-tag">Clear pose</div>
  <div class="mobile-guidance-tag">No cropped limbs</div>
</div>
<button class="modal-cta" id="apply-pose-btn">{SPARKLE}<span>Apply Pose</span></button>
<div class="modal-cta__helper">Applying a new pose will update your try-on result</div>
</div>

</div><!-- end right -->
</div><!-- end body -->

<!-- Footer -->
<div class="modal__footer desktop-only">
{LOCK}<span>Your photos are private and secure. We only use them to generate your try-on.</span>
</div>

</div><!-- end modal -->
</div><!-- end overlay -->
'''

# Read current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add modal.css link
if 'modal.css' not in content:
    content = content.replace('</head>', '<link rel="stylesheet" href="modal.css">\n</head>')

# Add modal.js link
if 'modal.js' not in content:
    content = content.replace('</body>', '<script src="modal.js"></script>\n</body>')

# Add modal HTML before </body>
if 'tryon-overlay' not in content:
    content = content.replace('<script src="modal.js"></script>', modal_html + '\n<script src="modal.js"></script>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Modal HTML injected into index.html successfully!")

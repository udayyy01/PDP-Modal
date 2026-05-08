#!/usr/bin/env python3
"""Generate the index.html for Reflekt PDP."""

# SVG Icons
SEARCH = '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>'
HEART = '<svg viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>'
USER = '<svg viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>'
CART = '<svg viewBox="0 0 24 24"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>'
CHEV_DOWN = '<svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>'
CHEV_LEFT = '<svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg>'
CHEV_RIGHT = '<svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg>'
ARROW_RIGHT = '<svg viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>'
EXPAND = '<svg viewBox="0 0 24 24"><polyline points="15 3 21 3 21 9"/><polyline points="9 21 3 21 3 15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg>'
SPARKLE = '<svg viewBox="0 0 24 24"><path d="M12 2l2.4 7.2L22 12l-7.6 2.8L12 22l-2.4-7.2L2 12l7.6-2.8z" stroke-linejoin="round"/></svg>'
SUN = '<svg class="toggle-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>'
MOON = '<svg class="toggle-moon" style="display:none" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>'

STAR_FULL = '<svg viewBox="0 0 24 24" fill="#E8B931" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>'
STAR_HALF = '<svg viewBox="0 0 24 24"><defs><linearGradient id="half"><stop offset="50%" stop-color="#E8B931"/><stop offset="50%" stop-color="#D1D1D1"/></linearGradient></defs><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" fill="url(#half)" stroke="none"/></svg>'

# Product images
thumbs = [
    ("images/hero_product.png", "Front view"),
    ("images/product_angle_2.png", "Full body"),
    ("images/product_angle_3.png", "Side view"),
    ("images/product_angle_4.png", "Back view"),
    ("images/product_detail.png", "Detail"),
    ("images/product_flatlay.png", "Flat lay"),
]

pair_items = [
    ("images/pair_trousers.png", "Relaxed Fit\nTrousers", "₹2,990"),
    ("images/pair_cotton_shirt.png", "Oversized\nCotton Shirt", "₹2,290"),
    ("images/pair_denim_jeans.png", "Wide Leg\nDenim Jeans", "₹2,490"),
    ("images/pair_hoodie.png", "Hooded\nSweatshirt", "₹2,190"),
    ("images/pair_chinos.png", "Relaxed Fit\nChinos", "₹2,290"),
    ("images/pair_cargo.png", "Loose Fit\nCargo Pants", "₹2,490"),
]

similar_items = [
    ("images/similar_tshirt_1.png", "Relaxed Fit\nT-Shirt / 01", "₹1,990", "4.5"),
    ("images/similar_tshirt_2.png", "Relaxed Fit\nT-Shirt / 02", "₹1,990", "4.4"),
    ("images/similar_tshirt_3.png", "Relaxed Fit\nT-Shirt / 03", "₹1,990", "4.6"),
    ("images/similar_tshirt_4.png", "Relaxed Fit\nT-Shirt / 04", "₹2,050", "4.6"),
    ("images/similar_knit.png", "Textured Knit\nT-Shirt / 01", "₹2,390", "4.4"),
    ("images/similar_tshirt_1.png", "Heavyweight\nT-Shirt / 01", "₹2,250", "4.6"),
    ("images/similar_tshirt_2.png", "Striped Oversized\nT-Shirt", "₹1,890", "4.5"),
]

def card(img, name, price, rating=None, idx=0):
    lines = name.split('\n')
    name_html = '<br>'.join(lines)
    r = ''
    if rating:
        stars = STAR_FULL * 4 + STAR_HALF
        r = f'<div class="product-card__rating"><div class="product-card__rating-stars">{stars}</div><span class="product-card__rating-value">{rating}</span></div>'
    return f'''<div class="product-card" id="card-{idx}">
<div class="product-card__img-wrap"><img src="{img}" alt="{lines[0]}" loading="lazy"><button class="product-card__heart" aria-label="Wishlist">{HEART}</button></div>
<div class="product-card__name">{name_html}</div>
<div class="product-card__price">{price}</div>{r}</div>'''

# Build thumb HTML
thumb_html = ''
for i, (src, alt) in enumerate(thumbs):
    active = ' active' if i == 0 else ''
    thumb_html += f'<button class="gallery__thumb{active}" aria-label="{alt}"><img src="{src}" data-full="{src}" alt="{alt}"></button>\n'

# Build pair cards
pair_cards = '\n'.join(card(img, name, price, idx=i) for i, (img, name, price) in enumerate(pair_items))

# Build similar cards
similar_cards = '\n'.join(card(img, name, price, rating, idx=100+i) for i, (img, name, price, rating) in enumerate(similar_items))

html = f'''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Reflekt - Women's Black Graphic Printed Oversized Sweatshirt. Try it on virtually before you buy.">
<title>Women's Black Graphic Printed Oversized Sweatshirt | Reflekt</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>

<!-- NAVBAR -->
<nav class="navbar" id="navbar">
<div class="container navbar__inner">
<button class="navbar__action-btn navbar__back-btn" aria-label="Go back">{CHEV_LEFT}</button>
<a href="#" class="navbar__logo">REFLEKT</a>
<div class="navbar__actions">
<button class="navbar__search" aria-label="Search">{SEARCH}<span class="navbar__search-text">Search</span></button>
<button class="navbar__action-btn" id="theme-toggle" aria-label="Toggle theme">{SUN}{MOON}</button>
<button class="navbar__action-btn" aria-label="Wishlist">{HEART}</button>
<button class="navbar__action-btn" aria-label="Account">{USER}</button>
<button class="navbar__action-btn" aria-label="Cart">{CART}</button>
</div>
</div>
</nav>

<!-- BREADCRUMB -->
<div class="container">
<nav class="breadcrumb" aria-label="Breadcrumb">
<a href="#">Home</a><span class="breadcrumb__sep">›</span>
<a href="#">Men</a><span class="breadcrumb__sep">›</span>
<a href="#">Topwear</a><span class="breadcrumb__sep">›</span>
<a href="#">Sweatshirts</a><span class="breadcrumb__sep">›</span>
<span class="breadcrumb__current">Women's Black Graphic Printed Oversized Sweatshirt</span>
</nav>
</div>

<!-- PRODUCT SECTION -->
<section class="container" id="product-section">
<div class="product-section">

<!-- Gallery -->
<div class="gallery">
<div class="gallery__thumbs">
{thumb_html}
<button class="gallery__thumb-scroll" aria-label="Scroll thumbnails">{CHEV_DOWN}</button>
</div>
<div class="gallery__hero">
<div class="gallery__hero-scroll">
<img id="gallery-hero-img" src="images/hero_product.png" alt="Women's Black Graphic Printed Oversized Sweatshirt">
<img src="images/product_angle_2.png" alt="Full body" class="mobile-only-img">
<img src="images/product_angle_3.png" alt="Side view" class="mobile-only-img">
<img src="images/product_angle_4.png" alt="Back view" class="mobile-only-img">
<img src="images/product_detail.png" alt="Detail" class="mobile-only-img">
<img src="images/product_flatlay.png" alt="Flat lay" class="mobile-only-img">
</div>
<button class="gallery__expand" aria-label="Expand image">{EXPAND}</button>
<button class="product-card__heart gallery__mobile-heart" aria-label="Wishlist">{HEART}</button>
<div class="gallery__dots">
<div class="gallery__dot active"></div>
<div class="gallery__dot"></div>
<div class="gallery__dot"></div>
<div class="gallery__dot"></div>
<div class="gallery__dot"></div>
<div class="gallery__dot"></div>
</div>
</div>
</div>

<!-- Product Info -->
<div class="product-info">
<span class="product-info__brand">BEWAKOOF®</span>
<h1 class="product-info__title">Women's Black Graphic Printed Oversized Sweatshirt</h1>
<div class="product-info__meta"><span>Women</span><span class="product-info__meta-dot"></span><span>Black</span></div>
<div class="product-info__price">₹889</div>
<div class="product-info__price-note">Inclusive of all taxes</div>

<div class="rating">
<div class="rating__stars">
<span class="rating__star">{STAR_FULL}</span>
<span class="rating__star">{STAR_FULL}</span>
<span class="rating__star">{STAR_FULL}</span>
<span class="rating__star">{STAR_FULL}</span>
<span class="rating__star rating__star--half">{STAR_HALF}</span>
</div>
<span class="rating__value">4.6</span>
<a class="rating__count" href="#">(128 reviews)</a>
</div>

<div class="size-selector">
<div class="size-selector__header">
<span class="size-selector__label">Select Size</span>
<a class="size-selector__guide" href="#">Size Guide</a>
</div>
<div class="size-selector__pills">
<button class="size-pill" id="size-s">S</button>
<button class="size-pill active" id="size-m">M</button>
<button class="size-pill" id="size-l">L</button>
<button class="size-pill" id="size-xl">XL</button>
<button class="size-pill" id="size-xxl">XXL</button>
</div>
</div>

<button class="try-on-cta" id="try-on-cta">
<div class="try-on-cta__left">
<span class="try-on-cta__icon">{SPARKLE}</span>
<div class="try-on-cta__text">
<div class="try-on-cta__title">Try This On You</div>
<div class="try-on-cta__subtitle">See how it looks in real life</div>
</div>
</div>
<span class="try-on-cta__arrow">{ARROW_RIGHT}</span>
</button>

<div class="buy-row">
<button class="buy-btn" id="buy-btn">{CART}<span>Buy on Merchant</span></button>
<button class="wishlist-btn" id="main-wishlist" aria-label="Add to wishlist">{HEART}</button>
</div>

<div class="accordion" id="accordion">
<div class="accordion__item">
<button class="accordion__header"><span>Description</span><span class="accordion__chevron">{CHEV_DOWN}</span></button>
<div class="accordion__body"><div class="accordion__content">
This oversized sweatshirt features a bold graphic print with abstract artistic illustrations. Made from premium cotton-blend fleece for ultimate comfort and warmth. The relaxed, oversized silhouette offers a contemporary streetwear aesthetic perfect for layering.
</div></div>
</div>
<div class="accordion__item">
<button class="accordion__header"><span>Fabric &amp; Care</span><span class="accordion__chevron">{CHEV_DOWN}</span></button>
<div class="accordion__body"><div class="accordion__content">
<strong>Material:</strong> 80% Cotton, 20% Polyester<br>
<strong>Weight:</strong> 320 GSM heavyweight fleece<br>
<strong>Care:</strong> Machine wash cold, tumble dry low. Do not bleach. Iron on low heat inside out.
</div></div>
</div>
<div class="accordion__item">
<button class="accordion__header"><span>Fit Details</span><span class="accordion__chevron">{CHEV_DOWN}</span></button>
<div class="accordion__body"><div class="accordion__content">
<strong>Fit:</strong> Oversized / Relaxed<br>
<strong>Length:</strong> Regular<br>
<strong>Sleeve:</strong> Drop shoulder, full length<br>
<strong>Model:</strong> Height 5'8", wearing size M
</div></div>
</div>
</div>

</div>
</div>
</section>

<!-- PAIR IT WITH -->
<section class="container carousel-section" id="pair-section">
<div class="carousel-section__header">
<h2 class="carousel-section__title">Pair it with</h2>
<div class="carousel-section__nav">
<span class="carousel-section__viewall">View all</span>
<button class="carousel-nav-btn carousel-prev" aria-label="Previous">{CHEV_LEFT}</button>
<button class="carousel-nav-btn carousel-next" aria-label="Next">{CHEV_RIGHT}</button>
</div>
</div>
<div class="carousel-track">{pair_cards}</div>
</section>

<!-- SIMILAR PRODUCTS -->
<section class="container carousel-section" id="similar-section">
<div class="carousel-section__header">
<h2 class="carousel-section__title">Similar Products</h2>
<div class="carousel-section__nav">
<span class="carousel-section__viewall">View all</span>
<button class="carousel-nav-btn carousel-prev" aria-label="Previous">{CHEV_LEFT}</button>
<button class="carousel-nav-btn carousel-next" aria-label="Next">{CHEV_RIGHT}</button>
</div>
</div>
<div class="carousel-track">{similar_cards}</div>
</section>

<!-- FOOTER -->
<footer class="footer" id="footer">
<div class="container">
<div class="footer__grid">
<div class="footer__brand">
<div class="footer__brand-logo">REFLEKT</div>
<p class="footer__tagline">You Choose, We Reflekt.<br>Try it. Own it.</p>
<div class="footer__socials">
<a href="#" class="footer__social-icon" aria-label="Instagram"><svg viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><circle cx="12" cy="12" r="5"/><circle cx="17.5" cy="6.5" r="1.5" fill="currentColor" stroke="none"/></svg></a>
<a href="#" class="footer__social-icon" aria-label="Facebook"><svg viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>
<a href="#" class="footer__social-icon" aria-label="YouTube"><svg viewBox="0 0 24 24"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19.1c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"/><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"/></svg></a>
<a href="#" class="footer__social-icon" aria-label="Pinterest"><svg viewBox="0 0 24 24"><path d="M8 12a4 4 0 1 1 8 0c0 3-2 5-4 5s-2-1-2-1"/><path d="M9 17l1-4"/></svg></a>
</div>
</div>
<div>
<div class="footer__col-title">Shop</div>
<div class="footer__links"><a href="#">Men</a><a href="#">Women</a><a href="#">New In</a><a href="#">Collections</a><a href="#">Sale</a></div>
</div>
<div>
<div class="footer__col-title">Help</div>
<div class="footer__links"><a href="#">Track Order</a><a href="#">Returns &amp; Exchanges</a><a href="#">Shipping</a><a href="#">FAQs</a><a href="#">Size Guide</a></div>
</div>
<div>
<div class="footer__col-title">About</div>
<div class="footer__links"><a href="#">About Us</a><a href="#">Sustainability</a><a href="#">Careers</a><a href="#">Press</a><a href="#">Contact Us</a></div>
</div>
<div>
<div class="footer__col-title">Join Us</div>
<p class="footer__newsletter-text">Get 10% off on your first order</p>
<div class="footer__newsletter-input">
<input type="email" placeholder="Enter your email" aria-label="Email for newsletter">
<button aria-label="Subscribe">{ARROW_RIGHT}</button>
</div>
</div>
</div>
<div class="footer__bottom">
<span class="footer__copyright">© 2024 REFLEKT. All rights reserved.</span>
<div class="footer__legal">
<a href="#">Privacy Policy</a>
<a href="#">Terms &amp; Conditions</a>
<a href="#">Cookie Policy</a>
</div>
</div>
</div>
</footer>

<div class="sticky-bottom-bar">
<button class="buy-btn sticky-buy">{CART}<span>Buy on Merchant</span></button>
<button class="try-on-cta sticky-try-on" id="sticky-try-on-btn">
<div class="try-on-cta__left">
<span class="try-on-cta__icon">{SPARKLE}</span>
<div class="try-on-cta__text">
<div class="try-on-cta__title">Try This On</div>
<div class="try-on-cta__subtitle">See how it looks in real life</div>
</div>
</div>
</button>
</div>

<script src="script.js"></script>
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html generated successfully!")

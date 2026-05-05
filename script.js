document.addEventListener('DOMContentLoaded', () => {

  // ===== DARK MODE TOGGLE =====
  const themeToggle = document.getElementById('theme-toggle');
  const html = document.documentElement;

  // Check saved preference
  const savedTheme = localStorage.getItem('reflekt-theme');
  if (savedTheme) html.setAttribute('data-theme', savedTheme);

  themeToggle?.addEventListener('click', () => {
    const current = html.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    localStorage.setItem('reflekt-theme', next);
    updateToggleIcon(next);
  });

  function updateToggleIcon(theme) {
    const svg = themeToggle?.querySelector('.toggle-sun');
    const svgMoon = themeToggle?.querySelector('.toggle-moon');
    if (theme === 'dark') {
      svg && (svg.style.display = 'none');
      svgMoon && (svgMoon.style.display = 'block');
    } else {
      svg && (svg.style.display = 'block');
      svgMoon && (svgMoon.style.display = 'none');
    }
  }
  updateToggleIcon(html.getAttribute('data-theme') || 'light');


  // ===== GALLERY THUMBNAIL CLICK =====
  const heroImg = document.getElementById('gallery-hero-img');
  const thumbs = document.querySelectorAll('.gallery__thumb');

  thumbs.forEach(thumb => {
    thumb.addEventListener('click', () => {
      thumbs.forEach(t => t.classList.remove('active'));
      thumb.classList.add('active');
      const src = thumb.querySelector('img').getAttribute('data-full');
      if (heroImg && src) {
        heroImg.style.opacity = '0';
        setTimeout(() => {
          heroImg.src = src;
          heroImg.style.opacity = '1';
        }, 200);
      }
    });
  });


  // ===== SIZE PILL SELECTION =====
  const sizePills = document.querySelectorAll('.size-pill');
  sizePills.forEach(pill => {
    pill.addEventListener('click', () => {
      sizePills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
    });
  });


  // ===== ACCORDION =====
  const accordionHeaders = document.querySelectorAll('.accordion__header');
  accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const item = header.parentElement;
      const body = item.querySelector('.accordion__body');
      const content = body.querySelector('.accordion__content');

      if (item.classList.contains('open')) {
        body.style.maxHeight = '0';
        item.classList.remove('open');
      } else {
        // Close others
        document.querySelectorAll('.accordion__item.open').forEach(openItem => {
          openItem.querySelector('.accordion__body').style.maxHeight = '0';
          openItem.classList.remove('open');
        });
        body.style.maxHeight = content.scrollHeight + 'px';
        item.classList.add('open');
      }
    });
  });


  // ===== CAROUSEL NAVIGATION =====
  document.querySelectorAll('.carousel-section').forEach(section => {
    const track = section.querySelector('.carousel-track');
    const prevBtn = section.querySelector('.carousel-prev');
    const nextBtn = section.querySelector('.carousel-next');
    const scrollAmount = 240;

    prevBtn?.addEventListener('click', () => {
      track.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
    });
    nextBtn?.addEventListener('click', () => {
      track.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    });
  });


  // ===== WISHLIST HEART TOGGLE =====
  document.querySelectorAll('.product-card__heart, .wishlist-btn').forEach(heart => {
    heart.addEventListener('click', (e) => {
      e.stopPropagation();
      heart.classList.toggle('active');
    });
  });


  // ===== THUMB SCROLL DOWN =====
  const thumbScroll = document.querySelector('.gallery__thumb-scroll');
  const thumbContainer = document.querySelector('.gallery__thumbs');
  thumbScroll?.addEventListener('click', () => {
    thumbContainer.scrollBy({ top: 90, behavior: 'smooth' });
  });


  // ===== HERO IMAGE TRANSITION =====
  if (heroImg) {
    heroImg.style.transition = 'opacity 0.2s ease';
  }

});

/**
 * Try-On Modal — State Machine & Interaction Logic
 */
document.addEventListener('DOMContentLoaded', () => {

  const overlay = document.getElementById('tryon-overlay');
  const modal = overlay?.querySelector('.modal');
  if (!overlay || !modal) return;

  // Elements
  const openBtn = document.getElementById('try-on-cta');
  const closeBtn = document.getElementById('modal-close');
  const stepPanels = modal.querySelectorAll('.step-panel');
  const stepperSteps = modal.querySelectorAll('.stepper__step');
  const stepperLines = modal.querySelectorAll('.stepper__line');

  // State
  let currentStep = 1;
  let selectedPhoto = 0; // index of selected photo (0 = first preset)
  let selectedPose = 0;

  // ===== OPEN / CLOSE =====
  const stickyOpenBtn = document.getElementById('sticky-try-on-btn');
  openBtn?.addEventListener('click', () => openModal());
  stickyOpenBtn?.addEventListener('click', () => openModal());
  closeBtn?.addEventListener('click', () => closeModal());
  
  // Mobile Header Controls
  document.getElementById('mobile-modal-close')?.addEventListener('click', () => closeModal());
  document.getElementById('mobile-modal-back')?.addEventListener('click', () => closeModal());

  overlay?.addEventListener('click', (e) => {
    if (e.target === overlay) closeModal();
  });

  // ESC key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && overlay.classList.contains('open')) closeModal();
  });

  function openModal() {
    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
    goToStep(1);
  }

  function closeModal() {
    overlay.classList.remove('open');
    document.body.style.overflow = '';
    // Reset after animation
    setTimeout(() => {
      goToStep(1);
      resetGenerating();
    }, 350);
  }

  // ===== STEP NAVIGATION =====
  function goToStep(step) {
    currentStep = step;
    // Update panels
    stepPanels.forEach(p => p.classList.remove('active'));
    const target = modal.querySelector(`[data-step="${step}"]`);
    if (target) target.classList.add('active');

    // Update stepper
    stepperSteps.forEach((s, i) => {
      const stepNum = i + 1;
      s.classList.remove('active', 'completed', 'upcoming');
      if (stepNum < step) s.classList.add('completed');
      else if (stepNum === step) s.classList.add('active');
      else s.classList.add('upcoming');
    });

    // Update stepper lines
    stepperLines.forEach((line, i) => {
      const lineAfterStep = i + 1;
      if (lineAfterStep < step) line.classList.add('completed');
      else line.classList.remove('completed');
    });

    // Update stepper circle content
    stepperSteps.forEach((s, i) => {
      const circle = s.querySelector('.stepper__circle');
      const stepNum = i + 1;
      if (s.classList.contains('completed')) {
        circle.innerHTML = '<svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>';
      } else {
        circle.textContent = stepNum;
      }
    });

    // Update mobile step progress
    const mobileLabel = modal.querySelector('.mobile-step-label');
    const mobileTitle = modal.querySelector('.mobile-step-title');
    const mobilePercent = modal.querySelector('.mobile-step-percent');
    const mobileFill = modal.querySelector('.mobile-step-bar-fill');
    
    if (mobileLabel && mobileTitle && mobilePercent && mobileFill) {
      const titles = ["Select Yourself", "Generating", "Result", "Refine Pose"];
      const percents = ["25%", "50%", "75%", "100%"];
      
      mobileLabel.textContent = `Step ${step} of 4`;
      mobileTitle.textContent = titles[step - 1] || titles[0];
      mobilePercent.textContent = percents[step - 1] || percents[0];
      mobileFill.style.width = percents[step - 1] || percents[0];
    }
  }

  // ===== PHOTO SELECTION (Step 1) =====
  const photoCards = modal.querySelectorAll('.selector-card[data-photo]');
  const mobilePreviewContainer = document.getElementById('mobile-photo-preview-container');
  const mobileSelectedImg = document.getElementById('mobile-selected-img');
  
  function updateMobilePreview(card) {
    if (mobileSelectedImg && mobilePreviewContainer) {
      const img = card.querySelector('img');
      if (img) {
        mobileSelectedImg.src = img.src;
        // On mobile we show it, on desktop the CSS hides it
        mobilePreviewContainer.style.display = 'block'; 
      }
    }
  }

  photoCards.forEach((card, i) => {
    card.addEventListener('click', () => {
      photoCards.forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');
      selectedPhoto = i;
      
      updateMobilePreview(card);

      // Enable CTA
      const cta = modal.querySelector('#tryon-cta-btn');
      if (cta) {
        cta.removeAttribute('disabled');
        cta.style.opacity = '1';
      }
    });
  });

  // ===== POSE SELECTION (Step 4) =====
  const poseCards = modal.querySelectorAll('.selector-card[data-pose]');
  poseCards.forEach((card, i) => {
    card.addEventListener('click', () => {
      poseCards.forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');
      selectedPose = i;
    });
  });

  // ===== TRY THIS LOOK CTA =====
  const tryLookBtn = modal.querySelector('#tryon-cta-btn');
  tryLookBtn?.addEventListener('click', () => {
    goToStep(2);
    runGenerating();
  });

  // ===== APPLY POSE CTA =====
  const applyPoseBtn = modal.querySelector('#apply-pose-btn');
  applyPoseBtn?.addEventListener('click', () => {
    goToStep(2);
    runGenerating();
  });

  // ===== GENERATING SIMULATION =====
  function runGenerating() {
    const dynamicText = modal.querySelector('#generating-dynamic-text');
    if (!dynamicText) return;

    // Reset
    dynamicText.textContent = "Uploading your photo...";

    // Step 2: Analyzing
    setTimeout(() => {
      dynamicText.textContent = "Analyzing outfit & pose...";
    }, 1500);

    // Step 3: Rendering
    setTimeout(() => {
      dynamicText.textContent = "Rendering your look...";
    }, 3500);

    // Step 4: Almost there
    setTimeout(() => {
      dynamicText.textContent = "Almost there...";
    }, 5000);

    // Transition to result
    setTimeout(() => {
      goToStep(3);
    }, 6500);
  }

  // ===== STEP 3 ACTIONS =====
  // Try Another Photo → go back to Step 1
  modal.querySelector('#action-try-another')?.addEventListener('click', () => goToStep(1));

  // Change photo → go back to Step 1
  modal.querySelector('#action-change-photo')?.addEventListener('click', () => goToStep(1));

  // Change Pose → go to Step 4
  modal.querySelector('#action-change-pose')?.addEventListener('click', () => goToStep(4));

  // Save Look (just toggle heart)
  modal.querySelector('#action-save-look')?.addEventListener('click', function() {
    this.classList.toggle('saved');
  });

  // Close button in result
  modal.querySelector('#result-close-btn')?.addEventListener('click', () => closeModal());

  // ===== STEP 4 BACK =====
  modal.querySelector('#back-to-result')?.addEventListener('click', () => goToStep(3));

  // ===== UPLOAD BLOCKS (simulated click) =====
  modal.querySelectorAll('.upload-block').forEach(block => {
    block.addEventListener('click', () => {
      // Create temp file input
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = 'image/jpeg,image/png';
      input.click();
      // We don't actually process the file — just UI demo
    });
  });

  // Initialize first photo as selected
  if (photoCards[0]) {
    photoCards[0].classList.add('selected');
    updateMobilePreview(photoCards[0]);
    const cta = modal.querySelector('#tryon-cta-btn');
    if (cta) {
      cta.removeAttribute('disabled');
      cta.style.opacity = '1';
    }
  }
  if (poseCards[0]) {
    poseCards[0].classList.add('selected');
  }

});

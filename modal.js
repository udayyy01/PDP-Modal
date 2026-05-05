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
  openBtn?.addEventListener('click', () => openModal());
  closeBtn?.addEventListener('click', () => closeModal());
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
  }

  // ===== PHOTO SELECTION (Step 1) =====
  const photoCards = modal.querySelectorAll('.selector-card[data-photo]');
  photoCards.forEach((card, i) => {
    card.addEventListener('click', () => {
      photoCards.forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');
      selectedPhoto = i;
      // Enable CTA
      const cta = modal.querySelector('#tryon-cta-btn');
      if (cta) cta.removeAttribute('disabled');
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
  const progressItems = modal.querySelectorAll('.progress-item');

  function resetGenerating() {
    progressItems.forEach(item => {
      const status = item.querySelector('.progress-item__status');
      status.className = 'progress-item__status';
      status.innerHTML = '';
      item.classList.add('muted');
    });
  }

  function runGenerating() {
    resetGenerating();

    const checkSvg = '<svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>';

    // Step 1: Uploading (instant complete)
    setTimeout(() => {
      setProgressDone(0, checkSvg);
    }, 600);

    // Step 2: Analyzing
    setTimeout(() => {
      setProgressLoading(1);
    }, 800);

    setTimeout(() => {
      setProgressDone(1, checkSvg);
    }, 2200);

    // Step 3: Rendering
    setTimeout(() => {
      setProgressLoading(2);
    }, 2400);

    setTimeout(() => {
      setProgressDone(2, checkSvg);
    }, 4200);

    // Step 4: Almost there
    setTimeout(() => {
      setProgressLoading(3);
    }, 4400);

    setTimeout(() => {
      setProgressDone(3, checkSvg);
    }, 5400);

    // Transition to result
    setTimeout(() => {
      goToStep(3);
    }, 5800);
  }

  function setProgressDone(index, checkSvg) {
    const item = progressItems[index];
    if (!item) return;
    item.classList.remove('muted');
    const status = item.querySelector('.progress-item__status');
    status.className = 'progress-item__status progress-item__status--done';
    status.innerHTML = checkSvg;
  }

  function setProgressLoading(index) {
    const item = progressItems[index];
    if (!item) return;
    item.classList.remove('muted');
    const status = item.querySelector('.progress-item__status');
    status.className = 'progress-item__status progress-item__status--loading';
    status.innerHTML = '';
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
  }
  if (poseCards[0]) {
    poseCards[0].classList.add('selected');
  }

});

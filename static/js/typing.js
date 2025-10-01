document.addEventListener('DOMContentLoaded', () => {
  const welcomeEl = document.querySelector('.typing.welcome');
  const descEl = document.querySelector('.typing.description');

  if (!welcomeEl || !descEl) return;

  const typeTextWithCursor = (el, text, speed = 50) => {
    return new Promise((resolve) => {
      el.textContent = '';
      let i = 0;
      const cursor = '|';
      let showingCursor = true;

      const interval = setInterval(() => {
        if (i <= text.length) {
          el.textContent = text.substring(0, i) + cursor;
          i++;
        } else {
          clearInterval(interval);
          el.textContent = text; 
          resolve();
        }
      }, speed);
    });
  };

  const startTyping = async () => {
    await typeTextWithCursor(welcomeEl, welcomeEl.dataset.text, 50);
    await typeTextWithCursor(descEl, descEl.dataset.text, 30);
  };

  startTyping();
});

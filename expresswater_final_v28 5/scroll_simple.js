(function() {
  const elements = Array.from(document.querySelectorAll('*'));
  const target = elements.find(el => el.textContent.trim() === 'MT-V-E300A Vertical' || (el.innerText && el.innerText.includes('MT-V-E300A Vertical')));
  if (target) {
    target.scrollIntoView({ block: 'center' });
    return "Found and scrolled to " + target.innerText;
  }
  return "Not found";
})()
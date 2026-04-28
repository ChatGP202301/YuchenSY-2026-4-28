(async () => {
  const elements = Array.from(document.querySelectorAll('*'));
  const targetText = 'MT-V-E300A Vertical';
  const target = elements.find(el => el.textContent.includes(targetText) && el.tagName !== 'SCRIPT' && el.tagName !== 'STYLE');
  
  if (target) {
    // Find the container/card for this product
    let card = target;
    while (card && !card.innerText.includes('viewDetails')) {
      card = card.parentElement;
    }
    if (!card) card = target.closest('div');

    card.scrollIntoView({ behavior: 'instant', block: 'center' });
    
    // Find the specific viewDetails link within this context
    const viewBtn = Array.from(card.querySelectorAll('*')).find(el => el.textContent.includes('viewDetails'));
    
    if (viewBtn) {
      return { 
        found: true, 
        text: target.innerText,
        btnText: viewBtn.innerText,
        rect: viewBtn.getBoundingClientRect()
      };
    }
    return { found: true, text: target.innerText, btnFound: false };
  }
  return { found: false };
})()
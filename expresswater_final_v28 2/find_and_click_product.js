(async () => {
  const elements = Array.from(document.querySelectorAll('*'));
  const target = elements.find(el => el.textContent.includes('MT-V-E300A Vertical') && el.tagName !== 'SCRIPT' && el.tagName !== 'STYLE');
  
  if (target) {
    const card = target.closest('.product-card') || target.closest('div[class*="card"]') || target.parentElement;
    card.scrollIntoView({ behavior: 'instant', block: 'center' });
    
    // Find the viewDetails link/button within this card
    const viewBtn = card.querySelector('button, a, .view-details, [onclick]') || 
                    Array.from(card.querySelectorAll('*')).find(el => el.textContent.includes('viewDetails'));
    
    return { 
      found: true, 
      rect: card.getBoundingClientRect(),
      btnFound: !!viewBtn,
      btnTag: viewBtn ? viewBtn.tagName : null,
      btnText: viewBtn ? viewBtn.innerText : null
    };
  }
  return { found: false };
})()
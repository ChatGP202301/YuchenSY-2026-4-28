(async () => {
  const elements = Array.from(document.querySelectorAll('*'));
  const target = elements.find(el => el.textContent.includes('MT-V-E300A Vertical') && el.tagName !== 'SCRIPT' && el.tagName !== 'STYLE');
  
  if (target) {
    const card = target.closest('.product-card') || target.closest('div[class*="card"]') || target.parentElement;
    card.scrollIntoView({ behavior: 'instant', block: 'center' });
    
    // Find the viewDetails link/button within this card
    const viewBtn = card.querySelector('button, a, .view-details, [onclick]') || 
                    Array.from(card.querySelectorAll('*')).find(el => el.textContent.includes('viewDetails'));
    
    if (viewBtn) {
      // Return details first to confirm scroll position
      return { 
        found: true, 
        cardText: card.innerText,
        btnTag: viewBtn.tagName,
        btnText: viewBtn.innerText
      };
    }
  }
  return { found: false };
})()
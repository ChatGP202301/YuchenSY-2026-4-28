(function() {
  const cards = Array.from(document.querySelectorAll('.product-card, div[class*="card"], div[class*="item"]'));
  const targetCard = cards.find(card => card.innerText.includes('MT-V-E300A Vertical'));
  if (targetCard) {
    targetCard.scrollIntoView({ block: 'center', behavior: 'instant' });
    const viewBtn = targetCard.querySelector('.view-details, button, a') || 
                    Array.from(targetCard.querySelectorAll('*')).find(el => el.innerText.includes('viewDetails'));
    
    // Return the bounds so we can click if needed, but first return status
    return {
      found: true,
      text: targetCard.innerText,
      btnFound: !!viewBtn,
      rect: targetCard.getBoundingClientRect()
    };
  }
  return { found: false };
})()
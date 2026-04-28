(function() {
  const cards = Array.from(document.querySelectorAll('.product-card, div[class*="card"], div[class*="item"]'));
  const targetCard = cards.find(card => card.innerText.includes('MT-V-E300A Vertical'));
  if (targetCard) {
    const viewBtn = targetCard.querySelector('.view-details, button, a') || 
                    Array.from(targetCard.querySelectorAll('*')).find(el => el.innerText.includes('viewDetails'));
    
    if (viewBtn) {
      viewBtn.click();
      return "Clicked viewDetails for MT-V-E300A Vertical";
    }
    return "viewDetails button not found";
  }
  return "Product card not found";
})()
(async () => {
  const products = Array.from(document.querySelectorAll('.product-card, [data-id], .product-item'));
  // Let's try to find it by text if class is unknown
  const targetProduct = Array.from(document.querySelectorAll('*')).find(el => el.textContent.includes('MT-V-E300A Vertical') && el.closest('.product-card, .product-item, div'));
  
  if (targetProduct) {
    targetProduct.scrollIntoView({ behavior: 'instant', block: 'center' });
    return { success: true, text: targetProduct.innerText };
  }
  return { success: false, error: 'Product not found' };
})()
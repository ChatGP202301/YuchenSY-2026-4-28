(async () => {
  const rgbToHex = (rgb) => {
    if (!rgb || rgb === 'rgba(0, 0, 0, 0)' || rgb === 'transparent') return 'transparent';
    const match = rgb.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/) || rgb.match(/^rgba\((\d+),\s*(\d+),\s*(\d+),\s*(\d+(\.\d+)?)\)$/);
    if (!match) return rgb;
    const r = parseInt(match[1]);
    const g = parseInt(match[2]);
    const b = parseInt(match[3]);
    return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1).toUpperCase();
  };

  const bodyBg = rgbToHex(window.getComputedStyle(document.body).backgroundColor);

  // Look for the hero section - usually the first section or a div with large heading
  const h1 = document.querySelector('h1');
  const heroColor = h1 ? rgbToHex(window.getComputedStyle(h1.closest('section, div, header')).backgroundColor) : 'not found';

  // Look for "MAIN PRODUCTS"
  const productsH2 = Array.from(document.querySelectorAll('h2, h3, h4')).find(el => el.textContent.includes('MAIN PRODUCTS'));
  const productsColor = productsH2 ? rgbToHex(window.getComputedStyle(productsH2.closest('section, div')).backgroundColor) : 'not found';

  return { __result: { body: bodyBg, hero: heroColor, products: productsColor } };
})()
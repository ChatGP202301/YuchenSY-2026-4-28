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

  const getBgColor = (el) => {
    if (!el) return null;
    return window.getComputedStyle(el).backgroundColor;
  };

  const results = {};

  // Body
  results.body = rgbToHex(getBgColor(document.body));

  // Hero section - usually contains the H1 or first major heading
  const h1 = document.querySelector('h1');
  if (h1) {
    let hero = h1.parentElement;
    // Walk up a bit to find the section/div container
    while (hero && hero.tagName !== 'SECTION' && hero.tagName !== 'DIV' && hero !== document.body) {
      hero = hero.parentElement;
    }
    results.hero = rgbToHex(getBgColor(hero));
  }

  // Products section - contains "MAIN PRODUCTS"
  const productsHeader = Array.from(document.querySelectorAll('h2, h3, h4')).find(el => el.textContent.includes('MAIN PRODUCTS'));
  if (productsHeader) {
    let productsSection = productsHeader.parentElement;
    while (productsSection && productsSection.tagName !== 'SECTION' && productsSection.tagName !== 'DIV' && productsSection !== document.body) {
      productsSection = productsSection.parentElement;
    }
    results.products = rgbToHex(getBgColor(productsSection));
  }

  return { __result: results };
})()
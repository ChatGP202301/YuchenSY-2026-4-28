(async () => {
  const data = Array.from(document.querySelectorAll('img')).map(img => ({
    src: img.src,
    alt: img.alt,
    id: img.id,
    className: img.className
  }));
  // Also check background images
  const bgs = Array.from(document.querySelectorAll('*'))
    .filter(el => window.getComputedStyle(el).backgroundImage.includes('assets.zyrosite.com'))
    .map(el => ({
      src: window.getComputedStyle(el).backgroundImage.slice(5, -2).replace(/"/g, ''),
      text: el.innerText.substring(0, 50)
    }));
  return { images: data, backgrounds: bgs };
})()
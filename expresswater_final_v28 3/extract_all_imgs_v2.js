(() => {
  const images = Array.from(document.querySelectorAll('img')).map(img => ({
    src: img.src,
    alt: img.alt
  }));
  const backgrounds = Array.from(document.querySelectorAll('*'))
    .map(el => {
      const bg = window.getComputedStyle(el).backgroundImage;
      if (bg && bg.includes('assets.zyrosite.com')) {
        return { src: bg.slice(5, -2).replace(/"/g, ''), text: el.innerText.substring(0, 50) };
      }
      return null;
    })
    .filter(x => x !== null);
  return { images, backgrounds };
})()
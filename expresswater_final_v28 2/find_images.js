(async () => {
  const imgs = Array.from(document.querySelectorAll('img')).map(img => ({
    src: img.src,
    alt: img.alt,
    closestText: img.closest('div')?.innerText.substring(0, 100) || ''
  }));
  const backgrounds = Array.from(document.querySelectorAll('*'))
    .filter(el => {
      const bg = window.getComputedStyle(el).backgroundImage;
      return bg && bg !== 'none' && bg.includes('zyro');
    })
    .map(el => ({
      src: window.getComputedStyle(el).backgroundImage.slice(5, -2),
      text: el.innerText.substring(0, 100)
    }));
  return { imgs, backgrounds };
})()
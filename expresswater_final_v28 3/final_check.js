(() => {
  const bodyStyle = window.getComputedStyle(document.body);
  const rgb = bodyStyle.backgroundColor.match(/\d+/g);
  let hex = "";
  if (rgb) {
    hex = "#" + rgb.slice(0, 3).map(x => parseInt(x).toString(16).padStart(2, '0')).join('').toUpperCase();
  }

  const paint = performance.getEntriesByType('paint');
  const fcp = paint.find(p => p.name === 'first-contentful-paint');
  
  const hero = document.querySelector('section, div[class*="hero"], header + div');
  const heroBg = hero ? window.getComputedStyle(hero).backgroundImage : "";

  const images = Array.from(document.querySelectorAll('img')).map(i => ({
    src: i.src,
    complete: i.complete && i.naturalHeight > 0
  }));

  return {
    ssl: window.location.protocol === 'https:',
    backgroundColor: bodyStyle.backgroundColor,
    backgroundColorHex: hex,
    fcp: fcp ? fcp.startTime : "N/A",
    loadTime: performance.timing.loadEventEnd - performance.timing.navigationStart,
    heroBg: heroBg,
    heroBgZyro: heroBg.includes('assets.zyrosite.com'),
    imagesCount: images.length,
    imagesLoaded: images.filter(i => i.complete).length,
    sgsPresent: images.some(i => i.src.toLowerCase().includes('sgs') || i.src.toLowerCase().includes('uploads/2022/08')),
    workshopPresent: images.some(i => i.src.toLowerCase().includes('workshop') || i.src.toLowerCase().includes('pp-%e6%bb%a4%e8%8a%af')),
    exhibitionPresent: images.some(i => i.src.toLowerCase().includes('exhibition') || i.src.toLowerCase().includes('img_5611'))
  };
})()
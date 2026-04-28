(async () => {
  const result = {};
  
  // 1. SSL Check
  result.ssl = window.location.protocol === 'https:';
  
  // 2. Performance Metrics
  const paintEntries = performance.getEntriesByType('paint');
  const fcpEntry = paintEntries.find(entry => entry.name === 'first-contentful-paint');
  result.fcp = fcpEntry ? fcpEntry.startTime : 'N/A';
  result.loadTime = performance.timing.loadEventEnd - performance.timing.navigationStart;

  // 3. Design: Background Color
  const bodyStyle = window.getComputedStyle(document.body);
  result.backgroundColor = bodyStyle.backgroundColor;
  const rgb = bodyStyle.backgroundColor.match(/\d+/g);
  if (rgb) {
    result.backgroundColorHex = "#" + rgb.slice(0, 3).map(x => parseInt(x).toString(16).padStart(2, '0')).join('').toUpperCase();
  }

  // 4. Header check
  const header = document.querySelector('header') || document.querySelector('.header') || document.querySelector('nav');
  result.headerPresent = !!header;

  // 5. Hero Background
  // Often hero is the first section
  const firstSection = document.querySelector('section');
  const heroStyle = firstSection ? window.getComputedStyle(firstSection) : window.getComputedStyle(document.body);
  result.heroBackgroundImage = heroStyle.backgroundImage;
  result.heroBgFromZyro = heroStyle.backgroundImage.includes('assets.zyrosite.com');

  // 6. Specific Images
  const images = Array.from(document.querySelectorAll('img'));
  result.imageStats = {
    total: images.length,
    loading: images.filter(img => img.complete && img.naturalHeight !== 0).length
  };

  return result;
})()
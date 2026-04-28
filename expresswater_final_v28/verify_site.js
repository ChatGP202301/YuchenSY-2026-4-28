(async () => {
  const result = {};
  
  // 1. SSL Check
  result.ssl = window.location.protocol === 'https:';
  
  // 2. Performance Metrics
  const [fcpEntry] = performance.getEntriesByName('first-contentful-paint');
  result.fcp = fcpEntry ? fcpEntry.startTime : 'N/A';
  result.loadTime = performance.timing.loadEventEnd - performance.timing.navigationStart;

  // 3. Design: Background Color
  const bodyStyle = window.getComputedStyle(document.body);
  result.backgroundColor = bodyStyle.backgroundColor;
  // Convert rgb/rgba to hex for forest green comparison
  const rgb = bodyStyle.backgroundColor.match(/\d+/g);
  if (rgb) {
    const hex = "#" + rgb.map(x => parseInt(x).toString(16).padStart(2, '0')).join('').toUpperCase();
    result.backgroundColorHex = hex;
  }

  // 4. Header check
  const header = document.querySelector('header');
  result.headerPresent = !!header;

  // 5. Hero Background
  const heroSection = document.querySelector('section') || document.body; // Adjust selector as needed
  const heroStyle = window.getComputedStyle(heroSection);
  result.heroBackgroundImage = heroStyle.backgroundImage;
  result.heroBgFromZyro = heroStyle.backgroundImage.includes('assets.zyrosite.com');

  // 6. Specific Images (SGS, Workshop, Exhibition)
  const images = Array.from(document.querySelectorAll('img'));
  result.images = images.map(img => ({
    src: img.src,
    alt: img.alt,
    loading: img.complete && img.naturalHeight !== 0
  }));

  result.sgsImages = result.images.filter(img => img.src.toLowerCase().includes('sgs') || img.alt.toLowerCase().includes('sgs'));
  result.workshopImages = result.images.filter(img => img.src.toLowerCase().includes('workshop') || img.alt.toLowerCase().includes('workshop'));
  result.exhibitionImages = result.images.filter(img => img.src.toLowerCase().includes('exhibition') || img.alt.toLowerCase().includes('exhibition'));

  return result;
})()
(() => {
  const nav = performance.getEntriesByType('navigation')[0];
  const resources = performance.getEntriesByType('resource');
  
  const largeAssets = resources
    .filter(r => r.transferSize > 100000)
    .map(r => ({
      url: r.name,
      size: (r.transferSize / 1024).toFixed(2) + ' KB',
      duration: r.duration.toFixed(2) + ' ms'
    }))
    .sort((a, b) => parseFloat(b.size) - parseFloat(a.size));

  return {
    navigation: {
      loadTime: (nav.loadEventEnd - nav.startTime).toFixed(2) + ' ms',
      domReady: (nav.domContentLoadedEventEnd - nav.startTime).toFixed(2) + ' ms',
      domContentLoaded: nav.domContentLoadedEventEnd,
      loadEventEnd: nav.loadEventEnd
    },
    largeAssets,
    dictionaryFile: resources.find(r => r.name.includes('dictionary') || r.transferSize > 800000) ? 'Found' : 'Not found'
  };
})()
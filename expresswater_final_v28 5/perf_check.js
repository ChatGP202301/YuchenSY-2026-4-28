(async () => {
  try {
    const nav = performance.getEntriesByType('navigation')[0];
    const resources = performance.getEntriesByType('resource');
    
    const largeAssets = resources
      .filter(r => r.transferSize > 100000) // > 100KB
      .map(r => ({
        url: r.name,
        size: (r.transferSize / 1024).toFixed(2) + ' KB',
        duration: r.duration.toFixed(2) + ' ms'
      }))
      .sort((a, b) => parseFloat(b.size) - parseFloat(a.size));

    const loadTime = nav.loadEventEnd - nav.startTime;
    const domReady = nav.domContentLoadedEventEnd - nav.startTime;

    // Check for the dictionary-related lag (speculative)
    // We can't easily "measure" lag without interaction, but we can look for large JSON/JS files
    const dictionaryFile = resources.find(r => r.name.includes('dictionary') || r.transferSize > 800000);

    return {
      navigation: {
        loadTime: loadTime.toFixed(2) + ' ms',
        domReady: domReady.toFixed(2) + ' ms',
        domContentLoaded: nav.domContentLoadedEventEnd,
        loadEventEnd: nav.loadEventEnd,
        details: nav
      },
      largeAssets,
      dictionaryFile: dictionaryFile ? {
        url: dictionaryFile.name,
        size: (dictionaryFile.transferSize / 1024).toFixed(2) + ' KB',
        duration: dictionaryFile.duration.toFixed(2) + ' ms'
      } : 'Not found'
    };
  } catch (e) {
    return { error: e.message };
  }
})()
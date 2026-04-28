(async () => {
  const performance = window.performance;
  const navEntry = performance.getEntriesByType('navigation')[0];
  const paintEntries = performance.getEntriesByType('paint');
  const fcpEntry = paintEntries.find(entry => entry.name === 'first-contentful-paint');

  const resourceEntries = performance.getEntriesByType('resource');
  const totalTransferredBytes = resourceEntries.reduce((sum, entry) => sum + (entry.transferSize || 0), 0) + (navEntry.transferSize || 0);

  const slowAssets = resourceEntries
    .filter(entry => entry.duration > 500) // assets taking more than 500ms
    .map(entry => ({
      name: entry.name,
      duration: entry.duration,
      size: entry.transferSize,
      type: entry.initiatorType
    }))
    .sort((a, b) => b.duration - a.duration);

  return {
    fcp: fcpEntry ? fcpEntry.startTime : null,
    loadTime: navEntry.loadEventEnd - navEntry.startTime,
    totalBytes: totalTransferredBytes,
    ssl: window.location.protocol === 'https:',
    slowAssets: slowAssets.slice(0, 10) // top 10 slow assets
  };
})()
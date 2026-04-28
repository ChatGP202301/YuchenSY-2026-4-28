(async () => {
  try {
    const urls = [
      'https://www.expresswater.cn/',
      'https://www.expresswater.cn/water-dispenser',
      'https://www.expresswater.cn/inline-filter-series',
      'https://www.expresswater.cn/flat-cap-filter-series',
      'https://www.expresswater.cn/carbonblockfilters'
    ];
    const results = {};
    for (const url of urls) {
      try {
        const response = await fetch(url);
        const html = await response.text();
        const imgMatches = html.match(/src="([^"]+)"/g) || [];
        const bgMatches = html.match(/url\(['"]?([^'"]+)['"]?\)/g) || [];
        results[url] = {
          images: imgMatches.map(m => m.match(/src="([^"]+)"/)[1]),
          backgrounds: bgMatches.map(m => m.match(/url\(['"]?([^'"]+)['"]?\)/)[1])
        };
      } catch (e) {
        results[url] = { error: e.message };
      }
    }
    return results;
  } catch (e) {
    return { error: e.message };
  }
})()

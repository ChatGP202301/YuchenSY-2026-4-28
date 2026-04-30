(() => {
  const name = (document.querySelector('h1')?.textContent || '').trim();
  const description = Array.from(document.querySelectorAll('article p, .entry-content p, .description p')).map(p => p.innerText.trim()).join('\n');
  const images = Array.from(document.querySelectorAll('img')).map(img => img.src).filter(src => src.includes('/wp-content/uploads/'));
  const specs = {};
  document.querySelectorAll('table tr').forEach(tr => {
    const tds = tr.querySelectorAll('td');
    if (tds.length >= 2) specs[tds[0].innerText.trim()] = tds[1].innerText.trim();
  });
  const features = Array.from(document.querySelectorAll('ul li')).map(li => li.innerText.trim()).filter(t => t.length > 0 && t.length < 200);
  return { name, description, images: [...new Set(images)], specs, features };
})()
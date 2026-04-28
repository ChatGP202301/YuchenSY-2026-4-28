(function() {
  const products = [];
  
  // Try to find sections that look like product entries
  // On homepage, we have headings and paragraphs
  
  // Section 1: Main Products (Colors)
  // headings "Golden Color", "White Color", "Dark Green Color"
  // These seem to be under "MAIN PRODUCTS"
  const mainProducts = [];
  const h4s = Array.from(document.querySelectorAll('h4'));
  h4s.forEach(h4 => {
    const text = h4.innerText.trim();
    if (['Golden Color', 'White Color', 'Dark Green Color', 'MT-V-600', 'MT-EV-600', 'MT-V-E300A'].includes(text)) {
      // Find the closest image and description
      // This is a bit tricky without seeing the DOM structure, 
      // but usually the image is nearby.
      let img = null;
      let desc = "";
      
      // Look for img in the same parent or sibling
      let parent = h4.parentElement;
      while (parent && !img) {
        img = parent.querySelector('img');
        if (!img) parent = parent.parentElement;
      }
      
      products.push({
        name: text,
        description: "", // Descriptions for these specific ones might be missing or shared
        image: img ? img.src : ""
      });
    }
  });

  // Section 2: CARBON BLOCK FILTER
  const cbf = document.querySelector('h3:contains("CARBON BLOCK FILTER"), h3:contains("CARBON BLOCK FILTER")'.replace(':contains', '')); 
  // Custom selector logic or iterate
  Array.from(document.querySelectorAll('h3')).forEach(h3 => {
    if (h3.innerText.includes('CARBON BLOCK FILTER')) {
      const desc = h3.nextElementSibling ? h3.nextElementSibling.innerText.trim() : "";
      const img = h3.parentElement.querySelector('img');
      products.push({
        name: "CARBON BLOCK FILTER",
        description: desc,
        image: img ? img.src : ""
      });
    }
    if (h3.innerText.includes('GAC Filter Flat Cap')) {
      const desc = h3.nextElementSibling ? h3.nextElementSibling.innerText.trim() : "";
      const img = h3.parentElement.querySelector('img');
      products.push({
        name: "GAC Filter Flat Cap",
        description: desc,
        image: img ? img.src : ""
      });
    }
  });

  // Generic extraction for other pages
  // We'll use this function on all pages
  const genericItems = document.querySelectorAll('.product-item, .product-card, .item, .col-md-4, .product-inner');
  genericItems.forEach(item => {
    const titleEl = item.querySelector('h1, h2, h3, h4, .title, .product-title, .name');
    const descEl = item.querySelector('p, .description, .desc, .product-desc');
    const imgEl = item.querySelector('img');
    
    if (titleEl && imgEl) {
      products.push({
        name: titleEl.innerText.trim(),
        description: descEl ? descEl.innerText.trim() : "",
        image: imgEl.src
      });
    }
  });

  return products;
})();
(function() {
  const result = [];
  
  // Helper to find descriptions (all following paragraphs until next header)
  function getDesc(el) {
    let desc = "";
    let next = el.nextElementSibling;
    while (next && !['H1','H2','H3','H4','H5'].includes(next.tagName)) {
      if (next.tagName === 'P' || next.tagName === 'DIV') {
          desc += next.innerText.trim() + " ";
      }
      next = next.nextElementSibling;
    }
    return desc.trim();
  }

  // Sections on homepage
  const headings = document.querySelectorAll('h2, h3, h4');
  headings.forEach(h => {
    const name = h.innerText.trim();
    // Filter out boilerplate
    if (['express water', 'MAIN PRODUCTS', 'Vertical Water Dispenser', 'WHY CHOOSE US', 'SUBSCRIBE', 'Copyright © 2023 Express', 'Alibaba Verified Supplier'].some(s => name.toLowerCase().includes(s.toLowerCase()))) return;
    if (name.length < 3 || name.length > 100) return;
    
    // Skip navigation/footer links
    if (h.closest('header') || h.closest('footer')) return;

    // Find image: check parent, or previous sibling, or inside current header parent
    let img = h.parentElement.querySelector('img');
    if (!img) {
      const container = h.closest('.col-md-4, .col-sm-6, .item, .section, .container');
      if (container) img = container.querySelector('img');
    }
    
    // If we have an image or description, count as product
    const desc = getDesc(h);
    if (img || desc) {
      result.push({
        name,
        description: desc,
        image: img ? img.src : ""
      });
    }
  });

  return result;
})();
(async () => {
  const data = [];
  const titles = Array.from(document.querySelectorAll('h2, h3, h4'));
  const skipList = ['express water', 'MAIN PRODUCTS', 'Vertical Water Dispenser', 'WHY CHOOSE US', 'SUBSCRIBE', 'Copyright © 2023 Express', 'Alibaba Verified Supplier', 'NSF Certified Express Water logo', 'Home', 'Product', 'OEM/ODM', 'About us', 'Contact', 'Learn more', 'Our Products', 'Check more', 'check more', 'SUBSCRIBE', 'Email address', 'MORE ABOUT US', 'Wall Mounted Water Dispenser', 'Water Filter', 'Activated Carbon Block Filter', 'PP Filter', 'T33', 'GAC Filter', 'UDF Filter', 'China Manufacturer, Factory, Supplier, Exporter', 'Alibaba Verified Supplier'];

  titles.forEach(titleEl => {
    const name = titleEl.innerText.trim();
    if (!name || skipList.some(s => name.toLowerCase() === s.toLowerCase())) return;
    if (name.length < 3 || name.length > 100) return;

    // Search for image in the same parent or preceding element
    let img = titleEl.parentElement.querySelector('img');
    if (!img) {
      // Search for img in a sibling container
      let container = titleEl.closest('.col-md-4, .col-sm-6, .item, .section, .container');
      if (container) img = container.querySelector('img');
    }
    
    // Search for description
    let desc = "";
    let next = titleEl.nextElementSibling;
    while (next && !['H1','H2','H3','H4'].includes(next.tagName)) {
      if (next.tagName === 'P' || next.tagName === 'DIV') {
          desc += next.innerText.trim() + " ";
      }
      next = next.nextElementSibling;
    }
    
    if (img || desc) {
      data.push({
        name,
        description: desc.trim(),
        image: img ? img.src : ""
      });
    }
  });
  
  return { __result: data };
})();
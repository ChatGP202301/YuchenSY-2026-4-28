(async () => {
  const data = {};

  // Product Name
  data.productName = document.querySelector('h1')?.innerText?.trim();

  // Main Image URL
  // Alibaba usually has a gallery. Let's look for the main image.
  const galleryImage = document.querySelector('.main-image-thumb-container img, .detail-main-image img, .gallery-image img, .main-layout img');
  data.mainImageUrl = galleryImage ? galleryImage.src : null;

  // If the above fails, look for the first large image
  if (!data.mainImageUrl) {
    const allImages = Array.from(document.querySelectorAll('img'));
    const largeImage = allImages.find(img => img.width > 300 && img.height > 300);
    data.mainImageUrl = largeImage ? largeImage.src : null;
  }

  // Key features
  const featuresList = document.querySelectorAll('.product-description-list li, .about-product-content li, .description-content li');
  data.keyFeatures = Array.from(featuresList).map(li => li.innerText.trim()).filter(t => t.length > 0);

  // Attributes / Specifications
  const attributeItems = document.querySelectorAll('.attribute-item, .key-attributes-list .attribute-item, .specification-item');
  const specs = {};
  attributeItems.forEach(item => {
    const key = item.querySelector('.attribute-name')?.innerText?.trim();
    const value = item.querySelector('.attribute-value')?.innerText?.trim();
    if (key && value) specs[key] = value;
  });
  data.specifications = specs;

  // If attributes are just text in a container (as seen in snapshot)
  if (Object.keys(specs).length === 0) {
    const attrContainer = document.querySelector('.key-attributes, .product-attributes');
    if (attrContainer) {
       data.specificationsRaw = attrContainer.innerText.trim();
    }
  }

  // Price and MOQ
  const priceContainer = document.querySelector('.price-item, .product-price, .price-list');
  data.priceInfo = priceContainer ? priceContainer.innerText.trim() : null;
  
  const moqElement = document.querySelector('.moq-item, .product-moq');
  data.moq = moqElement ? moqElement.innerText.trim() : null;

  return data;
})()
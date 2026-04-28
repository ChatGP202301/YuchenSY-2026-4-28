(async () => {
  const result = {};
  
  // Name
  result.name = document.querySelector('h1')?.innerText?.trim();
  
  // Image - looking for the main product image
  // Alibaba often uses a specific class for the main image
  const mainImg = document.querySelector('.main-image-thumb-container img, .detail-main-image img, .gallery-image img, .product-main-image img, .main-layout img, [class*="main-image"] img');
  result.image = mainImg ? mainImg.src : null;
  
  // If still null, try finding the first large image in the gallery
  if (!result.image) {
    const galleryImgs = Array.from(document.querySelectorAll('img')).filter(img => img.src.includes('product-detail') || img.src.includes('O1CN'));
    result.image = galleryImgs.length > 0 ? galleryImgs[0].src : null;
  }

  // Key Features
  const features = Array.from(document.querySelectorAll('.product-description-list li, .about-product-content li'));
  result.features = features.map(f => f.innerText.trim()).filter(t => t);

  // Specifications
  const attrText = document.querySelector('.key-attributes, .product-attributes')?.innerText;
  result.specsRaw = attrText;

  // Price/MOQ
  const priceMOQ = document.querySelector('.price-item, .price-list, .promotion-price-container')?.innerText;
  result.priceMOQRaw = priceMOQ;

  return result;
})()
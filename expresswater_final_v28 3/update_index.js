(async () => {
  const content = await fetch('index.html').then(r => r.text());
  
  // Add to products array
  const productsMatch = content.match(/products: \[([\s\S]*?)\]/);
  if (productsMatch) {
    const productsList = productsMatch[1];
    const newProducts = productsList.trim() + ',\n                    { nameKey: \'p45Name\', descKey: \'p45Desc\', tagKey: \'p45Tag\', image: "https://sc02.alicdn.com/kf/A30e494f90fa64e9da05ccd5f6c9687438.png" },\n                    { nameKey: \'p46Name\', descKey: \'p46Desc\', tagKey: \'p46Tag\', image: "https://sc02.alicdn.com/kf/Af352f0b28a2b45f898b1740b5602a230z.png" }';
    var newContent = content.replace(productsList, newProducts);
    
    // Add to English dictionary
    const enMatch = newContent.match(/en: \{([\s\S]*?)\}/);
    if (enMatch) {
        const enDict = enMatch[1];
        const newEn = enDict.replace('p44Tag: "Premium Carbon"', 'p44Tag: "Premium Carbon",\n                        p45Name: "Big Blue PCP Composite Filter (PP+GAC+PP)", p45Desc: "High-capacity composite filter combining dual PP layers with granular activated carbon for comprehensive filtration.", p45Tag: "Big Blue / 10\\"",\n                        p46Name: "Big Blue CTO Carbon Block Filter", p46Desc: "Industrial-grade high-density carbon block for superior chlorine and organic compound reduction in Big Blue housings.", p46Tag: "Big Blue / 10\\""');
        newContent = newContent.replace(enDict, newEn);
    }
    
    return newContent;
  }
  return null;
})()
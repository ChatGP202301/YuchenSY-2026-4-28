(async () => {
  const el = document.querySelector('a[href*="wa.me"]'); // Broad selector first
  if (!el) return { error: "WhatsApp button not found" };

  const rect = el.getBoundingClientRect();
  const styles = window.getComputedStyle(el);
  const bgColor = styles.backgroundColor;
  
  // Check position (bottom-right)
  const isBottomRight = (rect.bottom > window.innerHeight * 0.8) && (rect.right > window.innerWidth * 0.8);
  
  // Convert rgb to hex if needed
  const rgbToHex = (rgb) => {
    const match = rgb.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
    if (!match) return rgb;
    return "#" + ("0" + parseInt(match[1]).toString(16)).slice(-2).toUpperCase() +
                 ("0" + parseInt(match[2]).toString(16)).slice(-2).toUpperCase() +
                 ("0" + parseInt(match[3]).toString(16)).slice(-2).toUpperCase();
  };

  const hexColor = rgbToHex(bgColor);

  return {
    rect: {
      top: rect.top,
      left: rect.left,
      bottom: rect.bottom,
      right: rect.right,
      width: rect.width,
      height: rect.height
    },
    isBottomRight,
    bgColor: hexColor,
    href: el.href,
    title: el.title,
    innerText: el.innerText,
    viewport: {
      width: window.innerWidth,
      height: window.innerHeight
    }
  };
})()
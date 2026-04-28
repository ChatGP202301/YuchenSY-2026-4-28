(async () => {
  const el = document.querySelector('a.wa-float');
  const tooltip = document.querySelector('.wa-tooltip');
  
  if (!el) return { error: "WhatsApp button (a.wa-float) not found" };

  const rect = el.getBoundingClientRect();
  const styles = window.getComputedStyle(el);
  const bgColor = styles.backgroundColor;
  
  const isBottomRight = (rect.bottom > window.innerHeight * 0.8) && (rect.right > window.innerWidth * 0.8);
  
  const rgbToHex = (rgb) => {
    const match = rgb.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
    if (!match) return rgb;
    return "#" + ("0" + parseInt(match[1]).toString(16)).slice(-2).toUpperCase() +
                 ("0" + parseInt(match[2]).toString(16)).slice(-2).toUpperCase() +
                 ("0" + parseInt(match[3]).toString(16)).slice(-2).toUpperCase();
  };

  const hexColor = rgbToHex(bgColor);
  
  // For the tooltip, it might only be visible on hover. 
  // I'll check its text and style.
  const tooltipText = tooltip ? tooltip.innerText : "Not found";
  const tooltipStyle = tooltip ? window.getComputedStyle(tooltip) : null;
  const tooltipVisibleBeforeHover = tooltipStyle ? (tooltipStyle.opacity !== '0' && tooltipStyle.visibility !== 'hidden' && tooltipStyle.display !== 'none') : false;

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
    tooltipText,
    tooltipVisibleBeforeHover,
    viewport: {
      width: window.innerWidth,
      height: window.innerHeight
    }
  };
})()
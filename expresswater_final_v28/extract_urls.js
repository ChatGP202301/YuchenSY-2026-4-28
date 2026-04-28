(async () => {
  const results = {};
  
  // MT-900G Golden
  // The snapshot shows heading "Golden Color" is e11. The image is above it.
  // I'll look for an image near the text "MT-900G".
  const mt900gHeading = Array.from(document.querySelectorAll('h1, h2, h3, h4, h5, h6, p')).find(el => el.textContent.includes('MT-900G'));
  if (mt900gHeading) {
    let container = mt900gHeading.parentElement;
    // Walk up or look for siblings
    let img = container.querySelector('img') || container.previousElementSibling?.querySelector('img') || container.parentElement.querySelector('img');
    if (img) results.mt900g = img.src;
  }

  // MT-V-E300A Vertical
  const mtve300aHeading = Array.from(document.querySelectorAll('h1, h2, h3, h4, h5, h6, p')).find(el => el.textContent.includes('MT-V-E300A'));
  if (mtve300aHeading) {
    let container = mtve300aHeading.parentElement;
    let img = container.querySelector('img') || container.previousElementSibling?.querySelector('img') || container.parentElement.querySelector('img');
    if (img) results.mtve300a = img.src;
  }

  return results;
})()
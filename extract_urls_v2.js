(async () => {
  const getImageUrl = (text) => {
    const headings = Array.from(document.querySelectorAll('*')).filter(el => el.textContent.includes(text) && (el.tagName.startsWith('H') || el.tagName === 'P'));
    for (const h of headings) {
      // Look for the closest image in the ancestor chain or siblings
      let current = h;
      while (current && current !== document.body) {
        const img = current.querySelector('img');
        if (img) return img.src;
        // Check siblings
        let prev = current.previousElementSibling;
        while (prev) {
          const prevImg = prev.querySelector('img') || (prev.tagName === 'IMG' ? prev : null);
          if (prevImg) return prevImg.src;
          prev = prev.previousElementSibling;
        }
        current = current.parentElement;
      }
    }
    return null;
  };

  return {
    mt900g: getImageUrl('MT-900G'),
    mtve300a: getImageUrl('MT-V-E300A')
  };
})()
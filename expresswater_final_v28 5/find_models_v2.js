
(() => {
    const models = [
        "MT-S800",
        "MT-600DG",
        "MT-B600",
        "MT-D-20",
        "MT-DW-20",
        "MT-V-600",
        "MT-DV-E600"
    ];
    
    const results = {};
    const allImgs = Array.from(document.querySelectorAll('img')).map(img => ({
        src: img.src,
        rect: img.getBoundingClientRect(),
        alt: img.alt
    }));
    
    models.forEach(model => {
        const textElements = Array.from(document.querySelectorAll('*')).filter(el => 
            el.children.length === 0 && (el.textContent || '').includes(model)
        );
        
        if (textElements.length > 0) {
            const el = textElements[0];
            const elRect = el.getBoundingClientRect();
            
            // Find the closest image by vertical distance
            let closestImg = null;
            let minDistance = Infinity;
            
            allImgs.forEach(img => {
                // Vertical distance from bottom of image to top of text OR top of image to bottom of text
                const dist = Math.abs(img.rect.top - elRect.top);
                if (dist < minDistance) {
                    minDistance = dist;
                    closestImg = img.src;
                }
            });
            
            results[model] = closestImg;
        } else {
            results[model] = "Text not found";
        }
    });
    
    return results;
})();

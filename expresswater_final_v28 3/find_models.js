
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
    
    models.forEach(model => {
        // Find element containing the model name
        const elements = Array.from(document.querySelectorAll('*'));
        const modelElement = elements.find(el => el.children.length === 0 && el.innerText.includes(model));
        
        if (modelElement) {
            // Find the closest image
            let parent = modelElement;
            let foundImg = null;
            // Go up to 10 parents to find a sibling or ancestor with an image
            for (let i = 0; i < 10; i++) {
                if (!parent) break;
                const img = parent.querySelector('img');
                if (img) {
                    foundImg = img.src;
                    break;
                }
                // Also check siblings
                const siblingImg = Array.from(parent.parentElement?.children || []).find(s => s.querySelector('img'));
                if (siblingImg) {
                    foundImg = siblingImg.querySelector('img').src;
                    break;
                }
                parent = parent.parentElement;
            }
            results[model] = foundImg;
        } else {
            results[model] = "Not found";
        }
    });
    
    return results;
})();

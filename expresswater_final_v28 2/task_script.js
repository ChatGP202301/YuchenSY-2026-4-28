(async () => {
    try {
        const response = await fetch(window.location.href);
        const t = await response.text();
        
        // Step 2 logic
        const start = t.indexOf('languages: {');
        const end = t.indexOf('t(key) {');
        const languagesPart = t.substring(start, end).substring(0, 1000);
        
        // Step 3: Check for ar -> it transition comma
        // Find 'ar' and 'it' in the languagesPart
        const arMatch = languagesPart.match(/['"]?ar['"]?\s*:/);
        const itMatch = languagesPart.match(/['"]?it['"]?\s*:/);
        
        let commaStatus = "Not found";
        if (arMatch && itMatch) {
            const arEnd = arMatch.index + arMatch[0].length;
            const itStart = itMatch.index;
            const textBetween = languagesPart.substring(arEnd, itStart);
            
            // Check if there is a comma after the value of 'ar' and before 'it'
            // Usually it looks like: ar: '...', it: '...'
            // We look for a comma that isn't inside quotes (though the prompt is simpler)
            commaStatus = textBetween.includes(',') ? "Comma present" : "Comma missing";
        }

        // Step 4 logic
        let evalResult = "";
        try {
            const siteDataStart = t.indexOf('function siteData()');
            const siteDataEnd = t.lastIndexOf('</script>');
            if (siteDataStart !== -1 && siteDataEnd !== -1) {
                const evalCode = t.substring(siteDataStart, siteDataEnd);
                eval(evalCode);
                evalResult = "LIVE EVAL OK";
            } else {
                evalResult = "LIVE EVAL FAIL: Could not find siteData function markers";
            }
        } catch(e) {
            evalResult = "LIVE EVAL FAIL: " + e.message + " at line " + e.stack;
        }

        return {
            languagesSnippet: languagesPart,
            commaStatus: commaStatus,
            evalResult: evalResult
        };
    } catch (err) {
        return { error: err.message };
    }
})()
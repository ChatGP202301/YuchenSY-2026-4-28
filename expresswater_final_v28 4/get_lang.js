(async () => {
    try {
        const response = await fetch(window.location.href);
        const t = await response.text();
        const start = t.indexOf('languages: {');
        const end = t.indexOf('t(key) {');
        const snippet = t.substring(start, end).substring(0, 1000);
        return { __result: snippet };
    } catch (e) {
        return { __result: "ERROR: " + e.message };
    }
})()
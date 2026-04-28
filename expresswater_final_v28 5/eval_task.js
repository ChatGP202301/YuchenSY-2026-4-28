(async () => {
    try {
        const r = await fetch(window.location.href);
        const t = await r.text();
        const start = t.indexOf('function siteData()');
        const end = t.lastIndexOf('</script>');
        const code = t.substring(start, end);
        eval(code);
        return { __result: "LIVE EVAL OK" };
    } catch(e) {
        return { __result: "LIVE EVAL FAIL: " + e.message };
    }
})()
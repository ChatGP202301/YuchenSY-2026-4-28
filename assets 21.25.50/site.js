// Express Water - shared site JS
function toggleLangMenu() {
  const m = document.getElementById('langMenu');
  if (m) m.classList.toggle('open');
}
document.addEventListener('click', function(e) {
  const sw = document.querySelector('.lang-switcher');
  const m = document.getElementById('langMenu');
  if (m && sw && !sw.contains(e.target)) m.classList.remove('open');
});

// FAQ accordion
document.addEventListener('click', function(e) {
  const q = e.target.closest('.faq-q');
  if (q) q.parentElement.classList.toggle('open');
});

// Product category filter (on products.html)
function filterCat(cat, btn) {
  document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');
  document.querySelectorAll('.product-card').forEach(c => {
    c.style.display = (cat === 'all' || c.dataset.cat === cat) ? '' : 'none';
  });
}

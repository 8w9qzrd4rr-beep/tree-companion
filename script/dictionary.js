// ---------- SAMPLE DATA ----------
// Replace this with a real fetch() call to your backend/API.
const SPECIES = [
  {
    id: 1,
    common: 'Green Ash',
    latin: 'Fraxinus pennsylvanica',
    desc: 'A fast-growing shade tree common across the prairies. Tolerant of urban conditions but vulnerable to the emerald ash borer.',
    tags: ['Full sun', 'Medium water', 'Fast growth'],
  },
  {
    id: 2,
    common: 'Bur Oak',
    latin: 'Quercus macrocarpa',
    desc: 'A long-lived, hardy oak with deeply furrowed bark. Extremely drought tolerant once established and a great choice for parks.',
    tags: ['Full sun', 'Low water', 'Slow growth'],
  },
  {
    id: 3,
    common: 'Colorado Spruce',
    latin: 'Picea pungens',
    desc: 'An evergreen conifer with distinctive blue-grey needles. Popular as a windbreak and ornamental specimen tree.',
    tags: ['Full sun', 'Medium water', 'Evergreen'],
  },
  {
    id: 4,
    common: 'Silver Maple',
    latin: 'Acer saccharinum',
    desc: 'A large, fast-growing maple with deeply lobed leaves that flash silver in the wind. Prefers moist soil near rivers.',
    tags: ['Full sun', 'High water', 'Fast growth'],
  },
  {
    id: 5,
    common: 'Trembling Aspen',
    latin: 'Populus tremuloides',
    desc: 'Known for leaves that flutter in the slightest breeze. Spreads by root suckers and often grows in large clonal groves.',
    tags: ['Full sun', 'Medium water', 'Fast growth'],
  },
];

const listEl = document.getElementById('species-list');
const noResultsEl = document.getElementById('noResults');
const searchInput = document.getElementById('searchInput');

function render(items) {
  listEl.innerHTML = '';
  noResultsEl.hidden = items.length !== 0;

  for (const s of items) {
    const card = document.createElement('div');
    card.className = 'species-card';
    card.innerHTML = `
      <div class="species-row">
        <div class="icon-circle"><i class="fa fa-tree" aria-hidden="true"></i></div>
        <div class="species-info">
          <h4>${s.common}</h4>
          <p>${s.latin}</p>
        </div>
        <i class="fa fa-chevron-down chevron" aria-hidden="true"></i>
      </div>
      <div class="species-detail">
        <div class="species-detail-inner">
          ${s.desc}
          <div class="species-tags">
            ${s.tags.map(t => `<span class="species-tag">${t}</span>`).join('')}
          </div>
        </div>
      </div>
    `;

    card.querySelector('.species-row').addEventListener('click', () => {
      const wasOpen = card.classList.contains('open');
      document.querySelectorAll('.species-card.open').forEach(c => c.classList.remove('open'));
      if (!wasOpen) card.classList.add('open');
    });

    listEl.appendChild(card);
  }
}

searchInput.addEventListener('input', () => {
  const q = searchInput.value.trim().toLowerCase();
  const filtered = SPECIES.filter(s =>
    s.common.toLowerCase().includes(q) || s.latin.toLowerCase().includes(q)
  );
  render(filtered);
});

render(SPECIES);

// ---------- SAMPLE DATA ----------
// Replace this with a real fetch() call to your backend/API.
const ACTIVITIES = [
  { id: 1, type: 'plant', title: 'Planted a Green Ash', place: 'Wascana Park', date: '2026-08-01', thumb: null },
  { id: 2, type: 'water', title: 'Watered a Silver Maple', place: 'Albert St. Bridge', date: '2026-08-01', thumb: null },
  { id: 3, type: 'report', title: 'Reported storm damage', place: '14th Avenue', date: '2026-07-28', thumb: null },
  { id: 4, type: 'adopt', title: 'Adopted a Bur Oak', place: 'Victoria Park', date: '2026-07-28', thumb: null },
  { id: 5, type: 'plant', title: 'Planted a Colorado Spruce', place: 'Cathedral Village', date: '2026-07-15', thumb: null },
  { id: 6, type: 'water', title: 'Watered a Green Ash', place: 'Wascana Park', date: '2026-07-15', thumb: null },
];

const ICONS = {
  plant: 'fa-tree',
  water: 'fa-tint',
  report: 'fa-exclamation-triangle',
  adopt: 'fa-heart',
};

const timelineEl = document.getElementById('timeline');
const emptyStateEl = document.getElementById('emptyState');
const chips = document.querySelectorAll('.chip');

function formatDate(iso) {
  const d = new Date(iso + 'T00:00:00');
  return d.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' });
}

function render(filter) {
  const items = filter === 'all' ? ACTIVITIES : ACTIVITIES.filter(a => a.type === filter);

  timelineEl.innerHTML = '';
  emptyStateEl.hidden = items.length !== 0;

  // group by date, preserving order
  const groups = new Map();
  for (const item of items) {
    if (!groups.has(item.date)) groups.set(item.date, []);
    groups.get(item.date).push(item);
  }

  for (const [date, group] of groups) {
    const groupEl = document.createElement('div');
    groupEl.className = 'timeline-group';

    const dateEl = document.createElement('p');
    dateEl.className = 'timeline-date';
    dateEl.textContent = formatDate(date);
    groupEl.appendChild(dateEl);

    for (const item of group) {
      const card = document.createElement('div');
      card.className = `activity-card ${item.type}`;
      card.innerHTML = `
        <div class="icon-circle"><i class="fa ${ICONS[item.type]}" aria-hidden="true"></i></div>
        <div class="activity-info">
          <h4>${item.title}</h4>
          <p>${item.place}</p>
        </div>
        ${item.thumb ? `<img class="activity-thumb" src="${item.thumb}" alt="">` : ''}
      `;
      groupEl.appendChild(card);
    }

    timelineEl.appendChild(groupEl);
  }
}

chips.forEach(chip => {
  chip.addEventListener('click', () => {
    chips.forEach(c => c.classList.remove('active'));
    chip.classList.add('active');
    render(chip.dataset.filter);
  });
});

render('all');

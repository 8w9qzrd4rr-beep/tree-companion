export async function fetchTrees() {
    const response = await fetch('/api/v1/trees');
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
}

export async function addTree(formData) {
  return fetch('/api/v1/add/trees', { method: 'POST', body: formData });
}
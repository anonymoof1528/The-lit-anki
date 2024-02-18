fetch('data/list.txt')
  .then(response => response.text())
  .then(data => document.getElementById('content').innerText = data)
  .catch(error => console.error('Error fetching content:', error));


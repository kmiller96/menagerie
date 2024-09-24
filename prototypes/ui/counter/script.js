  // Elements
  const content = document.getElementById('content');
  const upButton = document.getElementById('up-button');
  const downButton = document.getElementById('down-button');

  // Variables
  let value = 0;

  // Functions
  function updateContent() {
    content.innerText = value;
  }

  // Handlers
  upButton.onclick = () => {
    value += 1;
    updateContent();
  }

  downButton.onclick = () => {
    value -= 1;
    updateContent();
  }

  // Initial call
  updateContent();
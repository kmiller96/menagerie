// -------- //
// Handlers //
// -------- //

function handleNewTodoItem() {
  const input = getInputNode();

  addTodoItem(input.value);

  renderListItems();
  clearInput();
}

// --------------- //
// Event Listeners //
// --------------- //

input.onsubmit = (e) => {
  e.preventDefault();
  handleNewTodoItem();
}

input.onkeydown = (e) => {
  if (e.code == "Enter") {
    handleNewTodoItem();
  } 
}

// clearListItems(); // TODO: Remove
renderListItems();
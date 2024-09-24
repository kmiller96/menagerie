/** Retrieves the list node in the DOM */
function getListNode() {
  return document.getElementById("list");
}

/** Retrieves the input node in the DOM */
function getInputNode() {
  return document.getElementById("input");
}

/** Clears the input field */
function clearInput() {
  getInputNode().value = "";
}

/** Appends a new todo item to the list */
function addTodoItem(content) {
  const items = getListItems() || [];
  items.push(content);
  saveListItems(items);
}

/** Removes a todo item from the list */
function removeTodoItem(index) {
  const items = getListItems() || [];
  items.splice(index, 1);
  saveListItems(items);
}

/** Creates the HTML for a single TODO item */
function renderItem (index, content) {
  // -- Generate layout nodes -- //
  const listItemNode = document.createElement("li");
  const containerNode = document.createElement("div");

  listItemNode.id = `item-${index}`;

  // -- Create remove button -- //
  const removeButton = document.createElement("button");
  removeButton.textContent = "X";
  removeButton.onclick = () => {
    // NOTE: There is a bug if items in the list have identical content.
    const index = getListItems().indexOf(content);
    removeTodoItem(index);
    renderListItems();
  }

  // -- Create text -- //
  const text = document.createElement("span");
  text.textContent = content;

  // -- Arrange elements -- //
  containerNode.appendChild(removeButton) 
  containerNode.appendChild(text);

  listItemNode.appendChild(containerNode);

  // -- Return -- //
  return listItemNode;
}

/** Converts the list of items into a rendered list */
function renderListItems() {
  const node = getListNode();
  node.innerHTML = "";  // Clear the list

  const items = getListItems() || [];

  for (const i in items) {
    const value = items[i];
    const listItem = renderItem(i, value);
    node.appendChild(listItem);
  }
}

// -------------------- //
// Save/Load List Items //
// -------------------- //

/** Retrieves the list items from local storage */
function getListItems() {
  return JSON.parse(localStorage.getItem("items"));
}

/** Saves the list items to local storage */
function saveListItems(items) {
  localStorage.setItem("items", JSON.stringify(items));
}

/** Clears the list items from local storage */
function clearListItems() {
  localStorage.removeItem("items");
}
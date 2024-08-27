const listElement = document.getElementById("list");

for (let el of listElement.children) {
  if (el.nodeName.toLowerCase() !== "li") {
    continue;
  }

  const checkboxElement = el.querySelector("input[type=checkbox]");
  checkboxElement.addEventListener("change", function () {
    if (checkboxElement.checked) {
      el.classList.add("checked");
    } else {
      el.classList.remove("checked");
    }
  });
}

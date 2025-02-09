const divContainer = document.getElementById("container-todos");
const activeTodos = document.getElementById("active_todos");
const checkbox = document.getElementById("cbx-12");
const TodosChildren = document.getElementById("container-main-todos");

activeTodos.addEventListener("click", () => {
  let i;
  let g;
  for (i = 0; i < todosList.length; i++) {
    for (g = 0; g < checkbox.length; g++) {
      if (checkbox[g].checked) {
        divContainer[i].style.display = "none";
        console.log(
          `check items ${checkbox[i].checked ? "checked" : "not checked"}`
        );
      } else {
        divContainer[i].style.display = "block";
      }
    }
  }
});

const submitForm = document.getElementById("submit");
// submitForm.addEventListener("submit", () => {});

const btnToggleMode = document.getElementById("toggle-light-dark-mode");
const lightSvg = document.getElementById("light-mode");
const darkSvg = document.getElementById("dark-mode");
const todosList = document.querySelectorAll(".container-main-todos");
const containerTodos = document.getElementById("container-todos");
const imgDesktop = document.getElementById("img-desktop");
const imgMobile = document.getElementById("img-mobile");

lightSvg.style.display = "block";
darkSvg.style.display = "none";

imgDesktop.src = "./images/bg-desktop-light.jpg";

btnToggleMode.addEventListener("click", () => {
  submit = false;

  document.body.classList.toggle("dark-mode");
  imgDesktop.src = "static/images/bg-desktop-dark.jpg";
  imgMobile.src = "static/images/bg-mobile-dark.jpg";
  todosList.forEach((div) => {
    div.classList.toggle("todoList");
  });
  const mode = document.body.classList.contains("dark-mode") ? "dark" : "light";
  localStorage.setItem("mode", mode);
  window.location.reload();
});

const addTodo = document.getElementById("add-todo");
const addTodoBtn = document.getElementById("add-todoBtn");
const addTodoBtn_ = document.getElementById("add-todoBtn-");
const smScreen = document.getElementById("sm-screen");
const formContainer = document.getElementById("container-form");
const containerFooter = document.getElementById("todos-footer");

// Check local storage for saved mode
const savedMode = localStorage.getItem("mode");
if (savedMode === "dark") {
  document.body.classList.add("dark-mode");

  smScreen.classList.add("todoListFooter");

  todosList.forEach((div) => {
    div.classList.add("todoList");
  });

  containerFooter.classList.add("todoListFooter");
  addTodo.classList.add("todoList");
  addTodoBtn.classList.add("todoList");
  addTodoBtn_.classList.add("todoList");

  containerTodos.classList.add("todoList");

  lightSvg.style.display = "none";
  darkSvg.style.display = "block";

  imgDesktop.src = "./static/images/bg-desktop-dark.jpg";
  imgMobile.src = "./static/images/bg-mobile-dark.jpg";
}

if (savedMode === "light") {
  imgDesktop.src = "./static/images/bg-desktop-light.jpg";
  imgMobile.src = "./static/images/bg-mobile-light.jpg";
  lightSvg.style.display = "block";
  darkSvg.style.display = "none";
}

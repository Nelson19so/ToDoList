const filterCompletedItems = document.querySelectorAll("#filterCompleted");
const filterAll = document.querySelectorAll("#filterAll");
const filterActive = document.querySelectorAll("#filterActive");

const todoItems = document.querySelectorAll(".container-main-todos");
const completeCheck = document.querySelectorAll(".completeCheck");

filterCompletedItems.forEach((completed) => {
  completed.addEventListener("click", () => {
    completeCheck.forEach((check) => {
      const todoItem = check.closest(".container-main-todos");
      if (check.checked) {
        todoItem.style.display = "block";
      } else {
        todoItem.style.display = "none";
      }
    });
  });
});

filterActive.forEach((active) => {
  active.addEventListener("click", () => {
    completeCheck.forEach((check) => {
      const todoItem = check.closest(".container-main-todos");
      if (!check.checked) {
        todoItem.style.display = "block";
      } else {
        todoItem.style.display = "none";
      }
    });
  });
});

filterAll.forEach((allItems) => {
  allItems.addEventListener("click", () => {
    completeCheck.forEach((check) => {
      const todoItem = check.closest(".container-main-todos");
      if (check.checked || !check.checked) {
        todoItem.style.display = "block";
      }
    });
  });
});

const btnToggleMode = document.getElementById("toggle-light-dark-mode");
const lightSvg = document.getElementById("light-mode");
const darkSvg = document.getElementById("dark-mode");
const todosList = document.querySelectorAll(".container-main-todos");
const containerTodos = document.getElementById("container-todos");
const imgDesktop = document.getElementById("img-desktop");
const imgMobile = document.getElementById("img-mobile");

lightSvg.style.display = "block";
darkSvg.style.display = "none";

imgDesktop.src = "./static/images/bg-desktop-light.jpg";

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
const updateTodo = document.getElementById("update-todoBtn");

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
  updateTodo.classList.add("todoList");
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

// if todos in input todos, shows save else shows update todo

const updateTodos = document.getElementById("update-todoBtn");
const saveTodos = document.getElementById("add-todoBtn");
const todoInput = document.getElementById("add-todo");

saveTodos.style.display = "none";

todoInput.addEventListener("input", () => {
  if (todoInput.value === "") {
    saveTodos.style.display = "none";
    updateTodos.style.display = "block";
  } else {
    saveTodos.style.display = "block";
    updateTodos.style.display = "none";
  }
});

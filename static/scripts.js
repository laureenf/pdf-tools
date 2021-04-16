function enableLightMode() {
    var themeToggle = document.getElementById('themeToggle');
    var head = document.head;
    var link = document.createElement("link")
    link.type = "text/css";
    link.rel = "stylesheet";
    link.href = "static/css/styles-light.css";
    link.id = "lightTheme";

    head.appendChild(link);
    console.log("Lightt");
    themeToggle.classList.add("btn-dark");
    themeToggle.innerText = 'Dark Mode';

    document.getElementsByClassName("navbar-toggler")[0].classList.replace("navbar-dark", "navbar-light");
    sessionStorage.setItem("mode", "light");
}

function enableDarkMode() {
    var themeStylesheet = document.getElementById('lightTheme');
    var themeToggle = document.getElementById('themeToggle');
    var head = document.head;
    if (themeStylesheet != null) {
        head.removeChild(themeStylesheet);
        console.log("Darkk");
        themeToggle.classList.remove("btn-dark");
        themeToggle.innerText = 'Light Mode';
        document.getElementsByClassName("navbar-toggler")[0].classList.replace("navbar-light", "navbar-dark");
    }
    sessionStorage.setItem("mode", "dark");
}

function toggleMode() {
    if(sessionStorage.getItem("mode") == "dark"){
        // if it's dark -> go light
        enableLightMode();
    } else if (sessionStorage.getItem("mode") == "light"){
        // if it's light -> go dark
        enableDarkMode();
    }
}
document.addEventListener('DOMContentLoaded', () => {
    console.log("loaded");
    console.log(sessionStorage.getItem("mode"))
    if (sessionStorage.getItem("mode") == "light") {
        console.log("stay in light mode");
        enableLightMode();
    } else if (sessionStorage.getItem("mode") == "dark") {
        console.log("stay in dark mode");
        enableDarkMode();
    } else {
        sessionStorage.setItem("mode", "dark");
    }
})

function changePasswordVisibility() {
    const password = document.getElementById('password');
    const togglePassword = document.getElementById('togglePassword');

    if (password.getAttribute('type') === 'password') {
        //change to text
        password.setAttribute('type', 'text');
        togglePassword.classList.add('fa-eye-slash');
    } else {
        //change to password
        password.setAttribute('type', 'password');
        togglePassword.classList.remove('fa-eye-slash');
    }
}

// function toggleDarkMode() {
//     //check if active is included in the class list
//     const darkMode = document.getElementById('darkMode')
//     if (darkMode.classList.contains('active')) {
//         //remove active class
//         darkMode.classList.remove('active')

//         //change to light mode
        
//         document.getElementsByTagName('body')[0].style.backgroundColor = '#f1e8d3';

//         const navbar = document.getElementsByTagName('nav')[0];
//         navbar.style.backgroundColor = '#d9534f';
//         navbar.classList.remove('navbar-dark');
//         navbar.classList.add('navbar-light'); //check if neededd

//         const cards = document.getElementsByClassName('card');
//         var i;
//         for (i = 0; i < cards.length; i++) {
//             cards[i].classList.add('card-light');
//         }

//         darkMode.classList.add('btn-outline-dark')

//         const mainContents = document.getElementsByClassName('main-content');
//         for (i = 0; i < mainContents.length; i++) {
//             mainContents[i].classList.add('main-content-light');
//         }

//         const headings = document.getElementsByTagName('h2');
//         for (i = 0; i < headings.length; i++) {
//             headings[i].style.borderBottomColor = 'black';
//         }

//         const modal = document.getElementById('modalContent')
//         modal.style.backgroundColor = 'white';
//         modal.style.color = 'black';

//         document.getElementById('modalCloseBtn').classList.remove('text-light');

        
//     } else {
//         //add active class
//         darkMode.classList.add('active')
        
//         //change to dark mode
//     }
// }
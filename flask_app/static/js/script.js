// const labels = document.querySelectorAll("label");

// labels.forEach(label => {
//   // console.log(label.innerText);
//   label.innerHTML = label.innerText
//     .split('')
//     .map((letter, index) => {
//     return `<span style="transition-delay: ${index*30}ms">${letter}</span>`;})
//     .join('');
//   console.log(label.innerHTML);
// });



'use strict';

//navbar toggle

const overlay = document.querySelector("[data-overlay]");
const navOpenBtn = document.querySelector("[data-nav-open-btn]");
const navbar = document.querySelector("[data-navbar]");
const navCloseBtn = document.querySelector("[data-nav-close-btn]");
const navLinks = document.querySelectorAll("[data-nav-link]");

const navElemArr = [navOpenBtn, navCloseBtn, overlay];

const navToggleEvent = function (elem) {
  for (let i = 0; i < elem.length; i++) {
    elem[i].addEventListener("click", function () {
      navbar.classList.toggle("active");
      overlay.classList.toggle("active");
    });
  }
};

navToggleEvent(navElemArr);
navToggleEvent(navLinks);

// heasder sticky & go top

const header = document.querySelector("[data-header]");
const goTopBtn = document.querySelector("[data-go-top]");
window.addEventListener("scroll", function () {
  if (window.scrollY >= 50) {
    header.classList.add("active");
    goTopBtn.classList.add("active")
  } else {
    header.classList.remove("active");
    goTopBtn.classList.remove("active");
  }
});

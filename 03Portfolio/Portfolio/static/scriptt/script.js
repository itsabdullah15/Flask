import {Swiper} from 'https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.mjs'
console.log("Script.js is running...");
var swiper = new Swiper(".mySwiper", {
  cssMode: true,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  pagination: {
    el: ".swiper-pagination",
  },
  mousewheel: true,
  keyboard: true,
});
swiper()
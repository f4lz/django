

let burgerBtn = document.querySelector('.header__burger');
let menu = document.querySelector('.header__nav');
let list = document.querySelector('.nav__list');
burgerBtn.addEventListener('click', function(){
	burgerBtn.classList.toggle('active');
	menu.classList.toggle('active');
    list.classList.toggle('active');
})




$(document).ready(function() {
    $('.header__burger').click(function(event) {
        $('header__burger', '.header__nav', '.nav__list'). toggleClass ('active');
    });
});
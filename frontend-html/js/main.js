// Cursor

let cursor = document.querySelector('.cursor')
let cursor2 = document.querySelector('.cursor2')

document.addEventListener("mousemove", function (e) {
    cursor.style.cssText = cursor2.style.cssText = "left: " + e.clientX + "px; top: " + e.clientY + "px;"
})
document.addEventListener("mouseout", function (e) {
    cursor.style.cssText = cursor2.style.cssText = "display: none;"
})
// Dropdown

let dropdown_link = document.getElementById('dropdownMenuLink1')
let dropdown_menu = document.querySelector('.nav-dropdown-menu')


// Burger Menu
// Can be used with JavaScript
// -----------------------------
const icnMenu = document.querySelector('.menu-icon');
const navItems = document.querySelector('.nav-items');
const body = document.querySelector('body')

icnMenu.addEventListener('click', () => {
    icnMenu.classList.toggle('active');
    navItems.classList.toggle('active-menu');
    body.classList.toggle('not-scroll-body')
	
});

$(document).ready(function() {
    $("#dropdownMenuLink2").click(function(){
        $("#dropdownMenu2").slideToggle();
    });
});  


// Scroll Down
window.onscroll = function() {onTheScroll()};

function onTheScroll() {
  if (document.documentElement.scrollTop > 300) {
        $('.header').addClass('onscrollHeader')
        $('#logo2').addClass('d-block')
        $('#logo1').addClass('d-none')

  } else {
        $('.header').removeClass('onscrollHeader')
        $('#logo1').removeClass('d-none')
        $('#logo2').removeClass('d-block')

  }
}



// Slide

function openSearch() {
    document.getElementById("myOverlay").style.display = "block";
    document.querySelector(".menu-icon").style.display = "none";

}

// Close the full screen search box
function closeSearch() {
    document.getElementById("myOverlay").style.display = "none";
    document.querySelector(".menu-icon").style.display = "block";
}


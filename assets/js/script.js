// document.addEventListener('DOMContentLoaded', function() {
//     var stickyNav = document.getElementById('stickyNav');
//     var content = document.querySelector('.content');

//     window.addEventListener('scroll', function() {
//         if (window.scrollY > content.offsetTop) {
//             stickyNav.classList.add('active');
//         } else {
//             stickyNav.classList.remove('active');
//         }
//     });
// });

window.onscroll = function() {
    var navbar = document.getElementById("navbar");
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        navbar.style.top = "0";
    } else {
        navbar.style.top = "-60px";
    }
};


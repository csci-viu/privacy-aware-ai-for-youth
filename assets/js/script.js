document.addEventListener('DOMContentLoaded', function() {
    var stickyNav = document.getElementById('stickyNav');
    var content = document.querySelector('.content');

    window.addEventListener('scroll', function() {
        if (window.scrollY > content.offsetTop) {
            stickyNav.classList.add('active');
        } else {
            stickyNav.classList.remove('active');
        }
    });
});

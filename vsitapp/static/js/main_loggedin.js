$(document).ready(function() {
    function appear(){
        $('.main-head').fadeIn(2000);
    }
    setTimeout(appear, 0.1);

})

/* Global scope function */
var openNav = function openNav() {
    $("#myNav").css("height", "100%");
}
var closeNav = function closeNav() {
    $("#myNav").css("height", "0%");
}


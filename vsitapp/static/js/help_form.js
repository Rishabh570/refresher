$(document).ready(function() {
    function enter() {
        $('.box').fadeIn(500);
        $('.box2').fadeIn(1500);
    }
    function appear() {
        $('.box3').fadeToggle(1200)
        $('.box3').css(("background-color", "aquablue"), ("box-shadow", "3px 5px solid #111111"));
    }
    setTimeout(enter, 1000);
    setTimeout(appear, 1200);
})
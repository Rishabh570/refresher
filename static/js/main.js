$(document).ready(function() {

    function firstIn() {
        $('#one').fadeIn(2000);
    }
    function firstOut() {
        $('#one').fadeOut(2000);
    }

    function secIn() {
        $('#two').fadeIn(2000);
    }
    function secOut() {
        $('#two').fadeOut(2000);
    }

    function thirdIn() {
        $('#three').fadeIn(2000);
    }
    function thirdOut() {
        $('#three').fadeOut(2000);
    }

    function fourIn() {
        $('#four').fadeIn(1000);
    }
    function fourOut() {
        $('#four').fadeOut(1000);
    }

    function fifthIn() {
        $('#five').fadeIn(2000);
    }
    function fifthOut() {
        $('#five').fadeOut(2000);
    }

    function refresherIn() {
        $('.main-head').fadeIn(2500);
    }

    setTimeout(firstIn, 2000);
    setTimeout(firstOut, 4000)
    setTimeout(secIn, 6000);
    setTimeout(secOut, 8000)
    setTimeout(thirdIn, 10000)
    setTimeout(thirdOut, 13000)
    setTimeout(fourIn, 15000)
    setTimeout(fourOut, 16000)
    setTimeout(fifthIn, 17000)
    setTimeout(fifthOut, 19000)
    setTimeout(refresherIn, 21000)
    
})
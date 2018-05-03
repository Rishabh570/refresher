$(document).ready(() => {

    $('.delete').mouseenter(function () {
        $(this).css('cursor', 'pointer')
        $(this).children().fadeIn()
    })
    $('.delete').mouseleave(function () {
        $(this).children().fadeOut()
    })


    // Upvote handler
    $('.upvotes').click(function(e) {
        e.preventDefault();
        var refer = $(this)
        var filter = $(this).attr("id")

        $.get('/upvote/', mydata={ 'filter': filter }, function (votes) {
            refer.parent().next().html(votes);
        })
        .fail(function () {
            $('.fail').fadeIn(1000, 'swing')
        })
    })

    // Downvote handler
    $('.downvotes').click(function(e) {
        e.preventDefault();
        var refer_down = $(this)
        var filter = $(this).attr("id")

        $.get('/downvote/', mydata={ 'filter': filter }, function (votes) {
            refer_down.parent().prev().html(votes);
        })
        .fail(function () {
            $('.fail').css('display', 'block')
        })
        
    })

    $('.delete').click(function(e) {
        e.preventDefault();
        var refer = $(this)
        var post_id = $(this).attr('id')
        $.get('/delete/', mydata = {'post_id': post_id}, function(callback) {
            refer.parent().css('display', 'none')
            console.log(callback)
        })
        .fail(function (callback) {
            refer.parent().html(callback)
        })
    })

})

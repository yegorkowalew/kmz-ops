$(document).ready(function () {
    $("#sidebar").mCustomScrollbar({
        theme: "minimal"
    });

    $('#dismiss, .overlay').on('click', function () {
        $('#sidebar').removeClass('active');
        $('.overlay').removeClass('active');
    });

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').addClass('active');
        $('.overlay').addClass('active');
        $('.collapse.in').toggleClass('in');
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
    });

    $(".peity-donut").peity("donut");

    $('#flt-ready').click(function() {
    $(this).toggleClass("btn-success btn-outline-success");
    $('.ready').toggleClass("show");
    return false;
    });

    $('#flt-overdue').click(function() {
    $(this).toggleClass("btn-danger btn-outline-danger");
    $('.overdue').toggleClass("show");
    return false;
    });

    $('#flt-tendays').click(function() {
    $(this).toggleClass("btn-warning btn-outline-warning");
    $('.tendays').toggleClass("show");
    return false;
    });

    $('#flt-inwork').click(function() {
    $(this).toggleClass("btn-primary btn-outline-primary");
    $('.inwork').toggleClass("show");
    return false;
    });

    $('#flt-np').click(function() {
    $(this).toggleClass("btn-info btn-outline-info");
    $('.np').toggleClass("show");
    return false;
    });

    $.each($('.l-order'), function(i) {
        if(i % 2 == 0){
            // console.log(i);
            $(this).addClass("l-order-two");
        };
    });

    $(function() {
        var mask = "cls-";
    
        $("div[class*=" + mask + "]").hover(function() {
            var classes = $(this).attr("class").split(" ")
            for (var i = 0; i < classes.length; i++) {
                if (classes[i].indexOf(mask) !== -1) {
                    $("."+classes[i]).toggleClass( "hover" )
                    return;
                }
            }
        });
    });

});
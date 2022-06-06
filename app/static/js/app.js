$(document).on('submit', '#contact-form', function(e) {
    console.log('hello');
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/contact',
        data: {
            name: $("#name").val(),
            subject: $("#subject").val(),
            email: $("#email").val(),
            message: $("#message").val(),
            receiver_name: $("#receiver_name").val(),
            receiver_email: $("#receiver_email").val()
        },
        success: function() {
            $('input[type="text"],textarea').val('');
            $("#submit").remove()
            $("#success-notification").text = "Message successfully sent"
        }
    })
});

$(document).ready(function() {

    // Check for click events on the navbar burger icon
    $(".navbar-burger").click(function() {

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");

    });
});
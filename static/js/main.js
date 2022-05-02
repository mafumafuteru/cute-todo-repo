function taskDone() {
    $("body").addClass("done-body-color");
    $(".mainLogoText").addClass("green-text");
    $(".nav-button").addClass("green-text");
    $("#signup-button").addClass("green-button");
    $(".submit-button-style-1").addClass("green-button");
    $(".submit-button-style-2").addClass("green-text");
    $("#task-text").addClass("green-text");
    $("#task-icon").attr("src", '/static/assets/images/icons8-carrot-60.png');
    $("#task-title-text").html("Good job!" + '<br />' + "Let's do something more fun!");
}

function taskSwitch() {
    $("body").removeClass("done-body-color");
    $(".mainLogoText").removeClass("green-text");
    $(".nav-button").removeClass("green-text");
    $("#signup-button").removeClass("green-button");
    $(".submit-button-style-1").removeClass("green-button");
    $(".submit-button-style-2").removeClass("green-text");
    $("#task-text").removeClass("green-text");
    $("#task-icon").attr("src", '/static/assets/images/icons8-bunny-64.png');
    $("#task-title-text").html("I see..." + '<br />' + "How about doing this next?");
} 
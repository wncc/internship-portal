//Navbar Sign-in dropdown JS
$(document).ready(function(){
    //Handles menu drop down
    $('.dropdown-menu').find('form').click(function (e) {
        e.stopPropagation();
    });
});
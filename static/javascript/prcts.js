var typed = new Typed(".auto-type", {
    strings: ["Active Reconnaissance", "Powered by Shodan"],
    typeSpeed: 50,
    backSpeed: 50,
    loop: true
})
/* function searchToggle(obj, evt){
    var container = $(obj).closest('.search-wrapper');
        if(!container.hasClass('active')){
            container.addClass('active');
            evt.preventDefault();
        }
        else if(container.hasClass('active') && $(obj).closest('.input-holder').length == 0){
            container.removeClass('active');
            // clear input
            container.find('.search-input').val('');
        }
}
*/
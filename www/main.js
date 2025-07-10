$(document).ready(function () {
    
    // Initialize the textillate plugin on elements with the class 'text'
    // Set the animation to loop and sync, with bounceIn and bounceOut effects

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'bounceIn',
        },
        out: {
            effect: 'bounceOut',
        }
    });

    
});    


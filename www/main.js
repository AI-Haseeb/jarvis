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

    // Siri Configuration
    var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style: "ios9",
    amplitude: 1,
    speed: 0.30,
    autostart: true,
  }); 

    //Siri Messaage Animation
     $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'fadeInUp',
            sync: true,
        },
        out: {
            effect: 'fadeOutUp',
            sync: true,
        }
    });

    // Mic Button click event
    $("#MicBtn").click(function (e) {
        eel.playAssisstantSound("start_sound.mp3");
        $("#oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands();
        eel.speak("Listening...");

    });
    
});    


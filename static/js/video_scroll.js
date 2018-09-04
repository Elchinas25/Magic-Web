var height = 300;
var btn = document.getElementById("myBtn"); 
var video = document.getElementById("myVideo");

function myFunction() {
  
      if (video.paused) {
          video.play();
          btn.innerHTML = "Pause";
      } else {
          video.pause();
          btn.innerHTML = "Play";
      }

      toggleVideoButton();
}


$(document).scroll(function(){

if ($(this).scrollTop() > height) {
  video.pause();

} else {
    if (btn.innerHTML == "Pause") {
      video.play();
    }  
  

}

});
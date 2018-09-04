    var height = 1000;

  $(document).scroll(function() {
  
  if ($(this).scrollTop() > height) {
    
    $(".navbar").css("background-color","#{{styles.nav_bg_color}}");

  } else {
    $(".navbar").css("background-color","transparent");
  }

});
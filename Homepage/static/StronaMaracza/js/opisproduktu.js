$(".btn").on("click",function(){
  $('.menu').toggleClass("show");
});
$(".menu").on("click",function(){
  $('.menu').toggleClass("show");
});


$(document).ready(function(){
  $( "a.scroll" ).click(function( event ) {
      window.history.back()
  });
});
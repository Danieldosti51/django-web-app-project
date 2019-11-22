$(document).ready(function() {

  $( ".card" ).hover(
  function() {
    $(this).removeClass('shadow-sm');
    $(this).addClass('shadow-lg').css('cursor', 'pointer');
  }, function() {
    $(this).removeClass('shadow-lg');
    $(this).addClass('shadow-sm');
  }
);

});
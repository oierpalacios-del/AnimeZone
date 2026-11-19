$(document).ready(function() {
  //jQuery code...
  $("div.content > a").click(function () {
    var contenido = $(this).attr("name");
    contenido = "#" + contenido + "body";
    $(contenido).slideUp();
  });
  $("div.content > a").dblclick(function () {
    var contenido = $(this).attr("name");
    contenido = "#" + contenido + "body";
    $(contenido).slideDown();
  });
  $("div.top > a").click(function () { 
    $("div.content > a").trigger("click");
  });
  $("div.top > a").dblclick(function () { 
    $("div.content > a").trigger("dblclick");
  });
  $("a.menu").click(function () { 
    var contenido = $(this).attr("name");
    contenido = "div.content > a." + contenido;  
    $(contenido).trigger("click");
  });
  $("a.menu").dblclick(function () { 
    var contenido = $(this).attr("name");
    contenido = "div.content > a." + contenido;  
    $(contenido).trigger("dblclick");
  });
});


$(document).ready(function() {
  
    // Desplegar y replegar sinopsis y estudios con un click
    $("div.content > a").click(function (e) {
        e.preventDefault();

        var contenido = $(this).attr("name");
        contenido = "#" + contenido + "body";

        $(contenido).slideToggle();
    });

    // 2. Barra superior: cierra TODO con un click
    $("div.top > a").click(function () {
        $("div.content > a").trigger("click");
    });

});

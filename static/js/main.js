var respuestas = [];
var id_user = null;

$(document).ready(function () {

    id_user = $("#id_user").text();

    $(".respuesta").click(function(e){

        e.preventDefault();
        var id = $(this).parent().attr("id");
        $("#" + id + " .respuesta").hide();
        $("#" + id +" .contestada").show();

        var obj = { "id": id.split("_")[1], "respuesta": $(this).attr("data-opcion")}
        respuestas.push(obj);

    });

    $("#enviar").click(function(){
        console.log(id_user);
        console.log(respuestas);
        $.ajax({
            url: '/guadar/',
            type: 'POST',
            data: {
                'id_user': id_user,
                'respuestas': respuestas
            },
            headers:{
                'X-CSRFToken': $('meta[name="token"]').attr("content")
            },
            success: function (data) {
                console.log(data);
            }

        });
    });

});
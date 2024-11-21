$(document).ready(function() {
    $('#search-box').keyup(function() {
        var query = $(this).val();
        if (query.length > 1) {
            $.ajax({
                url: '{% url "buscar_ciudades" %}',
                data: {
                    'q': query
                },
                dataType: 'json',
                success: function(data) {
                    var resultados = $('#resultados');
                    resultados.empty();
                    if (data.resultados.length > 0) {
                        data.resultados.forEach(function(ciudad) {
                            resultados.append(
                                '<div>' + 
                                    '<strong>' + ciudad.nombre + '</strong>, ' + 
                                    ciudad.estado + ', ' + 
                                    ciudad.pais + 
                                '</div>'
                            );
                        });
                    } else {
                        resultados.append('<div>No se encontraron resultados</div>');
                    }
                }
            });
        } else {
            $('#resultados').empty();
        }
    });
});

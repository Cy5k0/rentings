document.addEventListener('DOMContentLoaded', function () {
    const input = document.getElementById('buscar-ciudad');
    const resultadosDiv = document.getElementById('resultados');

    input.addEventListener('keyup', function () {
        const query = input.value;

        if (query.length > 2) {  // Inicia la búsqueda después de 2 caracteres
            fetch(`/buscar_ciudad/?q=${query}`)
                .then(response => response.json())
                .then(data => {
                    resultadosDiv.innerHTML = '';  // Limpiar resultados previos

                    if (data.length > 0) {
                        const lista = document.createElement('ul');
                        data.forEach(item => {
                            const li = document.createElement('li');
                            li.textContent = `${item.ciudad}, ${item.estado_provincia}, ${item.pais}`;
                            lista.appendChild(li);
                        });
                        resultadosDiv.appendChild(lista);
                    } else {
                        resultadosDiv.innerHTML = '<p>No se encontraron resultados</p>';
                    }
                });
        } else {
            resultadosDiv.innerHTML = '';  // Limpiar si la consulta es demasiado corta
        }
    });
});

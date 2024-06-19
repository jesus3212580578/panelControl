$(document).ready(function() {
    $('.task-status').on('change', function() {
        // Lógica para manejar el cambio de estado
    });

    $('.edit-task').on('click', function() {
        const currentTask = $(this).closest('.list-group-item');
        const title = currentTask.find('h5').text();
        const desc = currentTask.find('p').text();
        const assign = currentTask.find('small').text().replace('Asignado a: ', '');
        
        $('#edit-task-title').val(title);
        $('#edit-task-desc').val(desc);
        $('#edit-task-assign').val(assign);
    });


});

function eliminarTask(){
    const currentTask = $(this).closest('.list-group-item');
    
    Swal.fire({
        title: '¿Estás seguro?',
        text: "¡No podrás revertir esto!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Sí, eliminarlo'
    }).then((result) => {
        if (result.isConfirmed) {
            currentTask.remove();
            Swal.fire(
                '¡Eliminado!',
                'Tu tarea ha sido eliminada.',
                'success'
            ); 
        }
    });
}
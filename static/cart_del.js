$(document).ready(function() {
    $('form.remove-from-cart').on('submit', function(e) {
        e.preventDefault();
        var $form = $(this);
        var url = $form.attr('action');
        $.ajax({
            type: 'POST',
            url: url,
            data: $form.serialize(),
            success: function(response) {
                if (response.deleted) {
                    Swal.fire({
                        icon: 'success',
                        title: 'Успех',
                        text: 'Проект удален из корзины',
                        confirmButtonColor: '#3085d6',
                        confirmButtonText: 'OK'
                    }).then(() => {
                        // Обновите страницу или удалите элемент из DOM
                        location.reload(); // Это обновит страницу
                    });
                } else {
                    Swal.fire({
                        icon: 'error',
                        title: 'Ошибка',
                        text: 'Проект не найден в корзине',
                        confirmButtonColor: '#d33',
                        confirmButtonText: 'OK'
                    });
                }
            },
            error: function(response) {
                Swal.fire({
                    icon: 'error',
                    title: 'Ошибка',
                    text: 'Произошла ошибка. Попробуйте снова.',
                    confirmButtonColor: '#d33',
                    confirmButtonText: 'OK'
                });
            }
        });
    });
});
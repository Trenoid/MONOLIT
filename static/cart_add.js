$(document).ready(function() {
    $('form.add-to-cart').on('submit', function(e) {
        e.preventDefault();
        var $form = $(this);
        var url = $form.attr('action');
        $.ajax({
            type: 'POST',
            url: url,
            data: $form.serialize(),
            success: function(response) {
                if (response.added) {
                    Swal.fire({
                        icon: 'success',
                        title: 'Успех',
                        text: 'Проект добавлен в корзину',
                        confirmButtonColor: '#3085d6',
                        confirmButtonText: 'OK'
                    });
                } else {
                    Swal.fire({
                        icon: 'info',
                        title: 'Информация',
                        text: 'Проект уже в корзине',
                        confirmButtonColor: '#3085d6',
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
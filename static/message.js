const messageSucceful = `
            <div class="message">
                <div class="message__wrapper">
                    <img width="48" height="48" src="static/source/icons/message-succeful.svg" alt="" class="message__image" />
                    <h2 class="message__title">Спасибо за обращение!</h2>
                    <p class="message__descr">Мы свяжемся с вами в ближайшее время!</p>
                    <button class="message__button" data-action="message-close">Закрыть</button>
                </div>
            </div>`;
        const messageError = `
            <div class="message">
                <div class="message__wrapper">
                    <img width="48" height="48" src="static/source/icons/message-error.svg" alt="" class="message__image" />
                    <h2 class="message__title">Что-то пошло не так...</h2>
                    <p class="message__descr">Попробуйте снова или свяжитесь с нами!</p>
                    <button class="message__button" data-action="message-close">Закрыть</button>
                </div>
            </div>`;

        $(document).ready(function() {
            const form = $('#contactForm');
            const divWrapper = $(".wrapper");
            const overlay = $(".overlay");

            form.on("submit", function(event) {
                event.preventDefault();
                const formData = form.serialize();

                $.ajax({
                    type: "POST",
                    url: form.attr('action'),
                    data: formData,
                    success: function(response) {
                        if (response.status === 'success') {
                            divWrapper.append(messageSucceful);
                        } else {
                            divWrapper.append(messageError);
                        }
                        overlay.show();
                    },
                    error: function() {
                        divWrapper.append(messageError);
                        overlay.show();
                    }
                });
            });

            $('body').on('click', '[data-action="message-close"], .overlay', function() {
                divWrapper.children('.message').remove();
                overlay.hide();
            });
        });
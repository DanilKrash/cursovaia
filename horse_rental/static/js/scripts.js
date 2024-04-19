$(document).ready(function() {
            $('#id_trainer').change(function (e) {
                let trainer_id = $(this).val();
                $.get({
                    url: `/trainer/${trainer_id}/`,
                    data: {csrfmiddlewaretoken: '{{ csrf_token }}'},
                    success: function (info) {
                        $('.description_trainer').html('')
                        $('.description_trainer').append(`<img src="${info.image}" style="width: 300px; border-radius: 10px 10px 0 0;">`)
                        $('.description_trainer').append(`<p style="padding: 20px 0 10px 0">Фамилия: ${info.sername}</p>`)
                        if ('info.lastname' in info) {
                            $('.description_trainer').append(`<p style="padding: 0 0 10px 0">Отчество: ${info.lastname}</p>`)}
                        else {

                        }
                        $('.description_trainer').append(`<p style="">Работает с: ${info.date}</p>`)
                    }
                })
            })
});


$(document).ready(function() {
            $('#id_horse').change(function (e) {
                let horses_id = $(this).val();
                $.get({
                    url: `/horse/${horses_id}/`,
                    data: {csrfmiddlewaretoken: '{{ csrf_token }}'},
                    success: function (info) {
                        $('.description_horse').html('')
                        $('.description_horse').append(`<img src="${info.horse_img}" style="width: 300px; border-radius: 10px 10px 0 0;">`)
                        $('.description_horse').append(`<p style="padding: 20px 0 10px 0">Порода: ${info.breed}</p>`)
                        $('.description_horse').append(`<p style="padding: 20px 0 10px 0">День рождения: ${info.birthday}</p>`)
                        $('.description_horse').append(`<p style="padding-bottom: 20px">Статус: ${info.status}</p>`)
                    }
                })
            })
 });

$(document).ready(function () {
    $('#jquery').click(function () {
        var data = {
            'student_name': $('#student_name').val(),
            'student_e_mail': $('#student_e_mail').val(),
        };
        $.ajax({
            type: 'POST',
            url: '/api/retorno',
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(data),
            success: function (callback) {
                $('#response').html(callback.nome_e_mail)
            },
            error: function () {
                $(this).html("error!");
            }
        });
    });
});
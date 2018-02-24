$(document).ready(function () {

    $('#create-new-todo').submit(function (e) {
        e.preventDefault();

        var data = $('#create-new-todo').serialize();
        var gId = $('#dropdown-goals').attr('data');
        data = data + "&gId=" + gId;
        $.ajax({
            type: "POST",
            url: '/createTodo',
            data: data,
        }).done(function (resp) {
            window.location.href = 'listTodo';
        });

    });


    $('.btn-t-delete').click(function () {

        var parent = $(this).closest('.todo');
        var id = parent.attr('data');

        $.ajax({
            type: "POST",
            url: '/deleteTodo',
            data: {id: id}
        }).done(function (data) {
            parent.hide('slow', function () {
                parent.remove();
            });
        })
    });


    $('.btn-t-complete').click(function () {
        var parent = $(this).closest('.todo');
        var id = parent.attr('data');

        $.ajax({
            type: "POST",
            url: '/completeTodo',
            data: {id: id}
        }).done(function (data) {
            parent.find('.todo-container').addClass('complete');
        })
    });

    $('.goal-panel').click(function () {
        var parent = $(this).closest('.goal');

        $(this).find('svg').toggleClass('fa-arrow-down fa-arrow-up');

        parent.find('.goal-todo-list').slideToggle();
    });


    $('.dropdown').click(function () {
        $("#dropdown-goals").toggleClass("show");
    });

    $('#dropdown-goals').on('click', 'div', function () {
        var id = $(this).attr('data');
        var caption = $(this).find("span").text();
        $('#dropdown-goals').attr('data', id);

        if (id === "0") {
            caption = "";
        }
        $('.input-dropwown').find('input').val(caption);
    })

});



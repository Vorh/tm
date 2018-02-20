$(document).ready(function () {

    $('#create-new-todo').submit(function (e) {
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: '/createTodo',
            data: $('#create-new-todo').serialize(),
        });

    });


    $('.btn-t-delete').click(function () {

        var parent = $(this).closest('div[class^="todo"]');
        var id = parent.attr('data');

        $.ajax({
            type: "POST",
            url: '/deleteTodo',
            data: {id: id}
        }).done(function (data) {
            parent.remove();
        })
    });


    $('.btn-t-complete').click(function () {
        var parent = $(this).closest('div[class^="todo"]');
        var id = parent.attr('data');

        $.ajax({
            type: "POST",
            url: '/completeTodo',
            data: {id: id}
        }).done(function (data) {
            parent.addClass('complete');
        })
    });
});



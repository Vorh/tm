$(document).ready(function () {

    $('#create-new-todo').submit(function (e) {
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: '/createTodo',
            data: $('#create-new-todo').serialize(),
        }).done(function (resp) {
            window.location.href = 'listTodo';
        });

    });


    $('.btn-t-delete').click(function () {

        var parent = $(this).closest('div[class="todo"]');
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
});



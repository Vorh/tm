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

        parent.find('.goal-todo').slideToggle('slow', function () {
            // btn.toggleClass('', $(this).is(':visible'));

        });
    });

});



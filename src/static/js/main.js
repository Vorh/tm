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
        var id = $(this).closest('div[class^="todo"]').attr('data');
        $.ajax({
            type: "POST",
            url: '/deleteTodo',
            data: {id: id}
        })
    });


    $('.btn-t-complete').click(function () {
        var id = $(this).closest('div[class^="todo"]').attr('data');
        $.ajax({
            type: "POST",
            url: '/completeTodo',
            data: {id: id}
        })
    });
});


function deleteTodo(id) {
    xhr.open("GET", api + "delete.php" + '?id=' + id, true);
    xhr.send(null);

}

function completeTodo(id) {
    xhr.open("GET", api + "complete.php" + '?id=' + id, true);
    xhr.send(null);
}


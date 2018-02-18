
$(document).ready(function () {

    $('#create-new-todo').submit(function (e) {
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: '/createTodo',
            data: $('#create-new-todo').serialize(),
        });

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


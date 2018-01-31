<div class="create-todo">
    <h1 class="caption">CREATE NEW TODO</h1><br>
    <form id="create-new-todo" method="POST" action="">
        <label>Name</label><br>
        <input class="name border-red" type="text" name="caption"><br>
        <label>Notes</label><br>
        <textarea class="notes border-red" name="content" form="create-new-todo"></textarea><br>
        <input type="submit" onclick="window.location.href='index.php/list" class="btn-create-todo" value="Create todo">
    </form>
</div>

<?php
include_once '../dao/dataBase.php';
include_once '../dao/todoDao.php';
include_once '../utils.php';

?>


<div class="create-todo">
    <h1 class="caption">CREATE NEW TODO</h1><br>
    <form id="create-new-todo" >
        <label>Name</label><br>
        <input  class="name border-red" type="text" name="caption"><br>
        <label>Notes</label><br>
        <textarea class="notes border-red" name="content" form="create-new-todo"></textarea><br>
        <input type="submit" id="sb-create-new-todo" class="btn-create-todo" value="Create todo">
    </form>
</div>
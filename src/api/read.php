<?php

header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");

include_once '../dao/dataBase.php';
include_once '../model/todo.php';
include_once '../dao/todoDao.php';


$dataBase = new DataBase();
$db = $dataBase->getConnection();

$dao = new TodoDao($db);

$id = $_GET['id'];

$list = $dao->getListTodo($id);


$count = $list->rowCount();


if ($count > 0) {

    $todos=array();
    $todos["todo"]=array();

    while ($row = $list->fetch(PDO::FETCH_ASSOC)){
        extract($row);

        $product_item=array(
            "content" => $content,
            "date" => $date,
            "deleted" => $deleted,
            "complete" => $complete,
            "id" => $id
        );
        array_push($todos["todo"], $product_item);
    }

    echo json_encode($todos);

} else {
    echo json_encode(
        array("message" => "No products found.")
    );
}





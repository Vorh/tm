
<?php

session_start();

header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json; charset=UTF-8');
header("Access-Control-Allow-Methods: POST");
header("Access-Control-Max-Age: 3600");
header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");

include_once '../dao/dataBase.php';
include_once '../dao/todoDao.php';
include_once '../model/todo.php';
include_once '../utils.php';



$dataBase = new DataBase();
$db = $dataBase->getConnection();

$dao = new TodoDao($db);

$todo = new Todo();
$todo->content = validateInput($_POST['content']);
$todo->caption= validateInput($_POST['caption']);
$todo->userId = $_SESSION['id'];

$dao->createTodo($todo);

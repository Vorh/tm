<?php

header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json; charset=UTF-8');

include_once '../dataBase.php';
include_once '../todoDao.php';
include_once '../todo.php';



$dataBase = new DataBase();
$db = $dataBase->getConnection();

$dao = new TodoDao($db);

$dao->completeTodo($_GET['id']);

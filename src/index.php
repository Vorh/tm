<?php
session_start();


include_once 'dao/todoDao.php';
include_once 'model/todo.php';


if (!isset($_SESSION['username']) || empty($_SESSION['username'])) {
    header('location: login.php');
    exit;
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Todo</title>
    <?php include 'resources.php' ?>
</head>
<body>
<div id="container">
    <?php include 'partMain/sidebar.php' ?>
    <div id="content">
        <?php

        if (isset($_GET['create'])) {
            include 'partMain/createTodo.php';
        } else {
            include 'partMain/listTodo.php';
        }

        ?>
    </div>
</div>
</body>
</html>
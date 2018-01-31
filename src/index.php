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
    <link rel="stylesheet" href="static/css/style.css">
    <script src="https://use.fontawesome.com/releases/v5.0.4/js/all.js"></script>
    <script src="static/js/main.js"></script>

</head>
<body>
<div id="container">
    <?php include 'sidebar.php'?>
    <div id="content">
        <?php

        if (isset($_GET['create'])) {
            include 'createTodo.php';
        } else {
            include 'listTodo.php';
        }

        ?>
    </div>
</div>
</body>
</html>
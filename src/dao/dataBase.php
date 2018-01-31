<?php


class DataBase {

    private $host = "localhost";
    private $name = "tm";
    private $user = "root";
    private $password = "root";

    public $conn;


    public function getConnection(){

        $this->conn =null;

        try{
            $this->conn = new PDO(
                "mysql:host=".$this->host.
                ";dbname=".$this->name,
                $this->user,
                $this->password);
            $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            $this->conn->exec("set names utf8");
        }catch (PDOException $e){
            echo 'Connection error: '.$e->getMessage();
        }

        return $this->conn;
    }
}

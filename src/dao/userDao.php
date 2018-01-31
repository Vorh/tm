<?php



class UserDao{


    private $con;

    public function _construct($con){
        $this->con=$con;
    }



    public function checkLogin($username , $password){

        $sql = "select * from users where username = :username and password = :pass";



        $stmp=$this->con->prepare($sql);


        $stmp->bindParam(":username",$username);
        $stmp->bindParam(":pass",$password);


       return $stmp->execute()->rowCount()===0;
    }
}



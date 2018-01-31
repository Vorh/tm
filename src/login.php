


<?php


include_once 'dao/dataBase.php';
include_once 'dao/userDao.php';
include_once 'utils.php';


$dataBase = new DataBase();
$pdo = $dataBase->getConnection();



$username = $password = "";
$username_err = $password_err = "";


if ($_SERVER["REQUEST_METHOD"]=="POST"){

    if (empty(trim($_POST['username']))){
        $username_err = "Please enter username";
    }else{
        $username = validateInput($_POST['username']);
    }


    if (empty(trim($_POST['password']))){
        $password_err = 'Please enter your password';
    }else{
        $password = ($_POST['password']);
    }



    if (empty($username_err) && empty($password_err)){

        $sql = "select id,username , password from users where username = :username";


        if ($stmt = $pdo->prepare($sql)){


            $stmt->bindParam(':username',$param_username,PDO::PARAM_STR);


            $param_username = validateInput($_POST['username']);


            if ($stmt->execute()){

                if ($stmt->rowCount() ==1){

                    if($row = $stmt->fetch()){

                        $hashed_password = $row['password'];
                        $id = $row['id'];


                        if (password_verify($password,$hashed_password)){

                            session_start();

                            $_SESSION['username']= $username;
                            $_SESSION['id']= $id;
                            header('location:index.php');
                        }else{
                            $password_err = 'The password you entered was not valid.';

                        }
                    }
                }else{
                    $username_err = 'No account found with that username';
                }
            }else{
                echo "Oops! Something went wrong. Please try again later.";
            }
        }

        unset($stmt);
    }

    unset($pdo);
}
    ?>



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.css">
    <style type="text/css">
        body{ font: 14px sans-serif; }
        .wrapper{ width: 350px; padding: 20px; }
    </style>
</head>
<body>
<div class="wrapper">
    <h2>Login</h2>
    <p>Please fill in your credentials to login.</p>
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <div class="form-group <?php echo (!empty($username_err)) ? 'has-error' : ''; ?>">
            <label>Username:<sup>*</sup></label>
            <input type="text" name="username"class="form-control" value="<?php echo $username; ?>">
            <span class="help-block"><?php echo $username_err; ?></span>
        </div>
        <div class="form-group <?php echo (!empty($password_err)) ? 'has-error' : ''; ?>">
            <label>Password:<sup>*</sup></label>
            <input type="password" name="password" class="form-control">
            <span class="help-block"><?php echo $password_err; ?></span>
        </div>
        <div class="form-group">
            <input type="submit" class="btn btn-primary" value="Submit">
        </div>
        <p>Don't have an account? <a href="register.php">Sign up now</a>.</p>
    </form>
</div>
</body>
</html>

<?php



class TodoDao {


    private $db;

    public function __construct($db){
        $this->db = $db;
    }


    function  getListTodo($id){

        $sql = "select * from todo where user_id = :id";

        $stmp =$this->db->prepare($sql);

        $stmp->bindParam(':id',$id);

        $stmp->execute();

        return $stmp;
    }

    function deleteTodo($id){
        $sql = "delete from todo where id = :id";

        $stmt = $this->db->prepare($sql);

        $stmt->bindParam(":id",$id);

        $stmt->execute();
    }

    function completeTodo($id){
        $sql = "update todo set complete = true where id = :id";

        $stmt = $this->db->prepare($sql);

        $stmt->bindParam(":id",$id);

        $stmt->execute();
    }

    function createTodo($todo){
        $sql = "insert into todo (user_id,content,caption ) VALUES 
                (:user_id,:cont,:cap)";

        $stmp = $this->db->prepare($sql);

        $stmp->bindParam(':user_id',$todo->userId);
        $stmp->bindParam(':cont',$todo->content);
        $stmp->bindParam(':cap',$todo->caption);

        $stmp->execute();
    }
}

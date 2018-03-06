CREATE TABLE reward (

  id          INTEGER AUTO_INCREMENT,
  caption     VARCHAR(255),
  reward      VARCHAR(255),
  create_date TIMESTAMP,
  user_id     INT,

  PRIMARY KEY (id)
)
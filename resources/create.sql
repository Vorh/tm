CREATE TABLE reward (

  id          INTEGER AUTO_INCREMENT,
  caption     VARCHAR(255),
  reward      VARCHAR(255),
  create_date TIMESTAMP,
  user_id     INT,

  PRIMARY KEY (id)
);


CREATE TABLE goal (
  id          INT AUTO_INCREMENT PRIMARY KEY,
  caption     VARCHAR(255)                        NULL,
  create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  user_id     INT                                 NULL,
  reward      INT                                 NULL,
  FOREIGN KEY (reward) REFERENCES reward (id)
)
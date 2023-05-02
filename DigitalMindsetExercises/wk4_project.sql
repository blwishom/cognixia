
-- PROJECT 1
CREATE DATABASE Digital_Mindset_Project_Wk4;

use Digital_Mindset_Project_Wk4;

CREATE TABLE house (
house_id int PRIMARY KEY AUTO_INCREMENT,
address varchar(100) NOT NULL,
bedrooms int NOT NULL,
bathrooms float NOT NULL,
square_feet int
);

INSERT INTO house VALUES(1, '333 Query Ln Sequal, Ca 98765', 4, 2.5, 1500);
INSERT INTO house VALUES(2, '4402 Digital Cir Mindset, Ca 56789', 5, 3.5, 1800);

SELECT *
FROM house
WHERE house_id = 1;

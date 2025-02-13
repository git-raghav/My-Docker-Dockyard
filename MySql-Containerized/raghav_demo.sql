CREATE DATABASE IF NOT EXISTS RaghavDB;
USE RaghavDB;

CREATE TABLE students(
    StudentID INT NOT NULL AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    Surname VARCHAR(100) NOT NULL,
    PRIMARY KEY (StudentID)
);

INSERT INTO students (FirstName, Surname)
VALUES ("Raghav", "Agarwal"), ("Tarak", "Katoch");

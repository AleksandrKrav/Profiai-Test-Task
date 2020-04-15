CREATE TABLE IF NOT EXISTS person
(
    id      INT AUTO_INCREMENT PRIMARY KEY,
    name    VARCHAR(128) NOT NULL,
    surname VARCHAR(128) NOT NULL,
    age     SMALLINT(5) UNSIGNED,
    salary  INT UNSIGNED
);

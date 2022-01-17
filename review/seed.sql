CREATE database Discriminator_dev_v1;
USE Discriminator_dev_v1;
CREATE USER 'Disc'@'localhost' IDENTIFIED BY 'V9reamWwANyYc8j';
GRANT ALL PRIVILEGES ON Discriminator_dev_v1 . * TO 'Disc'@'localhost';
FLUSH PRIVILEGES;
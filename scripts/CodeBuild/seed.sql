-- codebuildでインストールしたDBに投入するクエリ
CREATE database Discriminator_test_v1;
USE Discriminator_test_v1;
CREATE USER 'Disc_test'@'localhost' IDENTIFIED BY 'V!9r<eamWwANyY}c8j';
GRANT ALL PRIVILEGES ON Discriminator_test_v1 . * TO 'Disc_test'@'localhost';
FLUSH PRIVILEGES;
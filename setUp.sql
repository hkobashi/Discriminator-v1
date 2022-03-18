-- データベース作成
CREATE database discriminator_local_v1;
USE discriminator_local_v1;

-- ユーザー作成
CREATE USER 'disc_local_v1'@'localhost' IDENTIFIED BY '7ThxqYs67yn';

-- 作成したDBユーザーに権限を付与
GRANT ALL PRIVILEGES ON * . * TO 'disc_local_v1'@'localhost';
FLUSH PRIVILEGES;
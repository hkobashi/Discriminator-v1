-- データベース作成
CREATE database discriminator_dev_v1;
USE discriminator_dev_v1;

-- ユーザー作成
CREATE USER 'disc_staging'@'%' IDENTIFIED BY '7Thx<qYs]67ynCfUF';

-- 作成したDBユーザーに権限を付与
GRANT ALL PRIVILEGES ON discriminator_dev_v1 . * TO 'disc_staging'@'%';
FLUSH PRIVILEGES;
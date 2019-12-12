# SQL QUERIES

create_admin_table="CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)"
create_employee_table="CREATE TABLE IF NOT EXISTS `employee` (ename_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, ENAME TEXT, CNP TEXT, SALARY TEXT)"
select_admin="SELECT * FROM `admin` WHERE `username` = 'savnet' AND `password` = 'pep19'"
add_admin="INSERT INTO `admin` (username, password) VALUES('savnet', 'pep19')"

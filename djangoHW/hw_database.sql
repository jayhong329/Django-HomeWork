-- creat database
create database django_hw;
use django_hw;

-- drop table djangohw;
-- drop database django_hw;

create table djangohw(
todo_id int not null primary key auto_increment,
completed boolean default 0,
todo varchar(20) not null,
last_update timestamp default current_timestamp on update current_timestamp
);

insert into djangohw(completed, todo)
values
('1', '學習 Python'),
('0', '學習 Django'),
('0', '學習 AJax');

select * from djangohw;

-- show warnings;
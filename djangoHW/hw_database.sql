-- creat database
create database django_hw;
use django_hw;

-- drop table djangohw

create table djangohw(
todolist int not null primary key auto_increment,
checkbox boolean not null,
learnsome varchar(20) not null);

select * from djangohw;

insert into djangohw(checkbox, learnsome)
values
('1', '學習 Python'),
('0', '學習 Django'),
('0', '學習 AJax');

select * from djangohw;

show warnings;
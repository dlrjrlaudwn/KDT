use sqlclass_db;

drop table if exists person;
create table person
	(person_id smallint unsigned,
	 fname varchar(20),
	 lname varchar(20),
	 eye_color enum('br','bl','gr'),
	 birth_date date,
	 street varchar(30),
	 city varchar(20),
	 state varchar(20),
	 country varchar(20),
	 postal_code varchar(20),
	 primary key(person_id)
	 );
	 
desc person;


drop table if exists favorite_food;
create table favorite_food
	(person_id smallint unsigned,
	food varchar(20),
	primary key(person_id,food),
	foreign key(person_id) references person(person_id)
	);
	
desc favorite_food;

set foreign_key_checks=0;
alter table person modify person_id smallint unsigned auto_increment;
set foreign_key_checks=1;

insert into person 
	(person_id,fname,lname,eye_color,birth_date)
	values(null,'william','turner','br','1972-05-27');
	
select * from person;

select person_id,fname,lname,birth_Date from person;

select person_id,fname,lname,birth_date from person where lname ='turner';

insert into favorite_food (person_id,food) values (1,'pizza');
insert into favorite_food (person_id,food) values (1,'cookies');
insert into favorite_food (person_id,food) values (1,'nachos');

select * from favorite_food;

delete from favorite_food where person_id=1;

insert into favorite_food (person_id,food)
values (1,'pizza'),(1,'cookies'),(1,'nachos');

select food from favorite_food where person_id =1 order by food;
select food from favorite_food where person_id =1 order by food desc;

insert into person 
(person_id,fname,lname,eye_color,birth_date,street,city,state,country,postal_code)
values(null,'susan','smith','bl','1975-11-02','23 maple st.','arlington','va','usa','20220');

select person_id,fname,lname,birth_date from person;

update person 
set street ='1225 tremon st.',
	city='boston',
	state ='ma',
	country ='usa',
	postal_code ='02138'
where person_id =1;
select *from person;

delete from person where person_id=2;
select *from person;
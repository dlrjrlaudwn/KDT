select 1 as num, 'abc' as str;
select 9 as num, 'xyz' as str;

select 1 as num, 'abc' as str
union
select 9 as num, 'xyz' as str;

use sakila;

desc customer;

desc actor;

select 'cust' as type1, c.first_name,c.last_name from customer c
union all
select 'actr' as type1, a.first_name, a.last_name from actor a;

select count(first_name) from customer;

select count(first_name) from actor;

select 'actr1' as type, a.first_name, a.last_name from actor a
union all
select 'actr2' as type, a.first_name, a.last_name from actor a;

select 'cust' as type1, c.first_name, c.last_name from customer c
where c.first_name like 'j%' and c.last_name like 'd%'
union all 
select 'act' as type1, a.first_name, a.last_name from actor a
where a.first_name like 'j%' and a.last_name like 'd%';

select c.first_name, c.last_name from customer c
where c.first_name like 'j%' and c.last_name like 'd%'
union
select a.first_name, a.last_name from actor a
where a.first_name like 'j%' and a.last_name like 'd%';

select c.first_name, c.last_name from customer c
where c.first_name like 'd%' and c.last_name like 't%';

select a.first_name, a.last_name from actor a
where a.first_name like 'd%' and a.last_name like 't%';

select c.first_name, c.last_name from customer c
where c.first_name like 'd%' and c.last_name like 't%'
intersect 
select a.first_name, a.last_name from actor a
where a.first_name like 'd%' and a.last_name like 't%';

select c.first_name, c.last_name from customer c
where c.first_name like 'j%' and c.last_name like 'd%'
intersect 
select a.first_name, a.last_name from actor a
where a.first_name like 'j%' and a.last_name like 'd%';

select c.first_name, c.last_name from customer as c
inner join actor as a
on(c.first_name=a.first_name) and (c.last_name=a.last_name);

select c.first_name, c.last_name from customer as c
inner join actor as a
on(c.first_name=a.first_name) and (c.last_name=a.last_name)
where a.first_name like 'j%' and a.last_name like 'd%';

select a.first_name,a.last_name from actor a
where a.first_name like 'j%' and a.last_name like 'd%';

select c.first_name, c.last_name from customer c
where c.first_name like 'j%' and c.last_name like 'd%';

select a.first_name,a.last_name from actor a
where a.first_name like 'j%' and a.last_name like 'd%'
except
select c.first_name, c.last_name from customer c
where c.first_name like 'j%' and c.last_name like 'd%';

select a.first_name, a.last_name from actor a
where a.first_name like 'j%' and a.last_name like 'd%'
union all
select a.first_name, a.last_name from actor a
where a.first_name like 'm%' and a.last_name like 't%'
union 
select c.first_name, c.last_name from customer c
where c.first_name like 'j%' and c.last_name like 'd%';

select first_name, last_name from actor
where last_name like 'l%'
union
select first_name, last_name from customer
where last_name like 'l%'
order by last_name;
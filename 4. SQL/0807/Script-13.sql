

#지역별 평균 임금

use sql_project;


drop table if exists region_wage;

create table region_wage
(region varchar(20),
working_day int,
working_time int,
working_real_time int,
working_over_time int,
wage int,
reg_wage int,
over_wage int,
special_wage int,
primary key(region));

desc region_wage;

select * from region_wage;




#각 공연별 평균 티켓 가격

use sql_project;

drop table if exists total_avg;

create table total_avg
(region varchar(20),
musical_avg float(10),
pop_music_avg float(10),
show_avg float(10),
primary key(region)
);

desc total_avg;

select * from total_avg;


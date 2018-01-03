drop table if exists entries;
create table entries (
  id        integer primary key autoincrement,
  title     varchar(150) not null,
  'text'    varchar(1500)  not null
);
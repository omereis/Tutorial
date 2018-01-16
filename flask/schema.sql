drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title varchar(35) not null,
  entry_text varchar(350) not null
);

create table entries (id integer primary key autoincrement, title varchar(35) not null, 'text' varchar(350) not null);
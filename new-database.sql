 create table place
(
    IdPlace integer NOT NULL
        primary key autoincrement,
    Name text(30),
    Address text(30),
    City text(30)
);

create table tournament
(
    IdTournament integer  not null
        primary key autoincrement,
    IdPlace integer references place,
    IdGame integer references game,
    Date text(30) NOT NULL,
    Duration integer
);

create table game
(
    idGame integer NOT NULL
        primary key autoincrement,
    Name text(30) NOT NULL
);

create table coach
(
    IdCoach integer NOT NULL primary key autoincrement,
    IdGame integer references game,
    LicenseDate text(30),
    IdEmployeeData integer references employee_Data
);
create table player
(
    IdPlayer integer NOT NULL primary key autoincrement,
    IdGame integer references game,
    Ranking integer,
    IdEmployeeData integer references employee_Data
);
create table staff
(
    IdStaff integer NOT NULL primary key autoincrement,
    IdEmployeeData integer references employee_Data
);

create table employee_Data
(
    IdEmployee integer NOT NULL
        primary key autoincrement,
    LastName text(30),
    FirstName text(30),
    Gender text(30),
    Age integer,
    Wage integer
); 
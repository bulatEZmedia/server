import sqlite3 as sq

with sq.connect("saper.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS Student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name  TEXT NOT NULL,
    Surname TEXT NOT NULL,
    Dads_name TEXT NOT NULL,
    id_group INTEGER NOT NULL)
     """);

    cur.execute("""CREATE TABLE IF NOT EXISTS Subject(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name  TEXT  NOT NULL UNIQUE,
    Teacher TEXT NOT NULL)
    """);

    cur.execute("""CREATE TABLE IF NOT EXISTS Score(
    Studentid INTEGER NOT NULL,
    Subjectid INTEGER NOT NULL,
    Data INTEGER NOT NULL,
    Score INTEGER NOT NULL,
    PRIMARY KEY(Studentid, Subjectid),
    constraint fk_Studentid FOREIGN KEY(Studentid) REFERENCES Student(id),	
    constraint fk_Subjectid FOREIGN KEY(Subjectid) REFERENCES Subject(id))	
    """)

    cur.execute("""INSERT INTO `Student` (`name`, `surname`, `dads_name`, `id_group`) VALUES ("Татлыбаев", "Булат", "Ильшатович", 10), ("Татлыбаев", "Булат", "Ильшатови", 10), ( "Татлыбаев", "Булат", "Ильатович", 10)""")

    cur.execute("""
    INSERT INTO Subject VALUES (1, "Java", "Сахапов Арслан Айратович"), (2, "Android", "Сахапов Арслан Айратович"),(3, "SQL", "Сахапов Арслан Айратович")
    """)
    cur.execute("""
        INSERT INTO Score VALUES (1, 5, 15, 5), (5, 4, 16, 2), (4, 7, 14, 3)
        """)

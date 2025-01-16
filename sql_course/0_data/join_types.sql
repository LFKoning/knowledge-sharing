/* Script for generating data for exercises with JOIN types. */

DROP TABLE IF EXISTS KoppelA;
DROP TABLE IF EXISTS KoppelB;

CREATE TABLE KoppelA (
    Id INTEGER,
    Tekst TEXT
);


INSERT INTO KoppelA (Id, Tekst) 
VALUES
    (1, 'ID 1 in A'),
    (2, 'ID 2 in A'),
    (4, 'ID 4 in A'),
    (4, 'ID 4 duplicaat in A'),
    (5, 'ID 5 in A'),
    (6, 'ID 6 in A'),
    (6, 'ID 6 duplicaat in A')
;

CREATE TABLE KoppelB (
    Id INTEGER,
    Tekst TEXT
);

INSERT INTO KoppelB (Id, Tekst) 
VALUES
    (1, 'ID 1 in B'),
    (3, 'ID 3 in B'),
    (4, 'ID 4 in B'),
    (5, 'ID 5 in B'),
    (5, 'ID 5 duplicaat in B'),
    (6, 'ID 6 in B'),
    (6, 'ID 6 duplicaat in B')
;
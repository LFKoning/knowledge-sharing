/* Script for generating data for exercises with JOIN types. */

DROP TABLE IF EXISTS KoppelA;
DROP TABLE IF EXISTS KoppelB;


-- Create the tables.
CREATE TABLE KoppelA (
    Id INTEGER,
    Beschrijving TEXT
);

CREATE TABLE KoppelB (
    Id INTEGER,
    Beschrijving TEXT
);


-- Insert the records.
INSERT INTO KoppelA (Id, Beschrijving)
VALUES
    (1, 'ID 1 in beide tabellen'),
    (2, 'ID 2 alleen in KoppelA'),
    (4, 'ID 4 in KoppelA')
;

INSERT INTO KoppelB (Id, Beschrijving)
VALUES
    (1, 'ID 1 in beide tabellen'),
    (3, 'ID 3 alleen in KoppelB'),
    (4, 'ID 4 - 1 in KoppelB'),
    (4, 'ID 4 - 2 in KoppelB')
;
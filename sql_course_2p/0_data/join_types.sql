/* Generate data for JOIN type exercises. */

-- Drop tables if they exist.
DROP TABLE IF EXISTS TabelA;
DROP TABLE IF EXISTS TabelB;


-- Create the tables.
CREATE TABLE TabelA (
    Id INTEGER,
    Beschrijving TEXT
);

CREATE TABLE TabelB (
    Id INTEGER,
    Beschrijving TEXT
);


-- Insert the records.
INSERT INTO TabelA (Id, Beschrijving)
VALUES
    (1, 'ID 1 in TabelA'),
    (2, 'ID 2 uniek in TabelA'),
    (4, 'ID 4 in TabelA')
;

INSERT INTO TabelB (Id, Beschrijving)
VALUES
    (1, 'ID 1 in TabelB'),
    (3, 'ID 3 uniek in TabelB'),
    (4, 'ID 4 dubbel in TabelB'),
    (4, 'ID 4 dubbel in TabelB')
;
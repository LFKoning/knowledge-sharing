/* Generate data for JOIN type exercises. */

-- Drop tables if they exist.
DROP TABLE IF EXISTS TabelA;
DROP TABLE IF EXISTS TabelB;


-- Create the tables.
CREATE TABLE TabelA (
    IdA INTEGER,
    DescA TEXT
);

CREATE TABLE TabelB (
    IdB INTEGER,
    DescB TEXT
);


-- Insert the records.
INSERT INTO TabelA (IdA, DescA)
VALUES
    (1, 'Tabel A: ID 1'),
    (2, 'Tabel A: ID 2 (uniek)'),
    (4, 'Tabel A: ID 4')
;

INSERT INTO TabelB (IdB, DescB)
VALUES
    (1, 'Tabel B: ID 1'),
    (3, 'Tabel B: ID 3 (uniek)'),
    (4, 'Tabel B: ID 4 (dubbel)'),
    (4, 'Tabel B: ID 4 (dubbel)')
;
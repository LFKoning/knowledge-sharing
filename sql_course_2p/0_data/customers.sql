/* Generate dummy customer data */

-- Drop table if it exists.
DROP TABLE IF EXISTS Klanten;

-- Create the table.
CREATE TABLE Klanten (
    Id INTEGER PRIMARY KEY,
    Naam TEXT NOT NULL,
    Achternaam TEXT NOT NULL,
    Leeftijd INTEGER NULL
);

-- Insert some dummy data.
INSERT INTO Klanten
  (Naam, Achternaam, Leeftijd)
VALUES
  ('Henk', 'Knol', 54),
  ('Ingrid', 'Jansen', 1979),
  ('mark', 'VOS', 23),
  ('mike ', 'de Ruiter', NULL)
;
/* Generate dummy customer data */

-- Clean up old versions.
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
  ('mike ', 'de Ruiter', NULL),
;
-- 1. Voer twee nieuwe klanten in.
INSERT INTO Klanten
  (Naam, Achternaam, Leeftijd)
VALUES
  ('Wouter', 'Bos', 67),
  ('Maria ', 'Groen', NULL)
;


-- 2. Wijzig jaartal in leeftijd.
UPDATE Klanten
SET
  Leeftijd = STRFTIME('%Y', CURRENT_DATE) - Leeftijd
WHERE Leeftijd > 1000
;


-- 3. Schoon Naam en Achternaam op.
UPDATE Klanten
SET
  Naam = LOWER(TRIM(Naam)),
  Achternaam = LOWER(TRIM(Achternaam))
;


-- 4. Verwijder klanten zonder leeftijd.
DELETE FROM Klanten
WHERE Leeftijd IS NULL;
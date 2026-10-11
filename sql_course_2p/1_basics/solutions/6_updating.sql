-- Open 0_data/customer.db.

-- 1. Voer twee nieuwe klanten in.
INSERT INTO Klanten
  (Naam, Achternaam, Leeftijd)
VALUES
  ('Wouter', 'Bos', 67),
  ('Maria ', 'Groen', NULL)
;

-- 1. Controleer of de nieuwe klanten zijn toegevoegd.
SELECT * FROM Klanten;


-- 2. Wijzig jaartal in leeftijd.
UPDATE Klanten
SET
  Leeftijd = STRFTIME('%Y', CURRENT_DATE) - Leeftijd
WHERE Leeftijd > 1000
;

-- 2. Controleer of leeftijden kloppen.
SELECT * FROM Klanten;


-- 3. Schoon Naam en Achternaam op.
UPDATE Klanten
SET
  Naam = LOWER(TRIM(Naam)),
  Achternaam = LOWER(TRIM(Achternaam))
;

-- 3. Controleer of namen opgeschoond zijn.
SELECT * FROM Klanten;


-- 4. Check eerst de selectie...
SELECT * FROM Klanten
WHERE Leeftijd IS NULL;

-- 4. Verwijder klanten zonder leeftijd.
DELETE FROM Klanten
WHERE Leeftijd IS NULL;

-- 4. Controleer of klanten verwijderd zijn.
SELECT * FROM Klanten;
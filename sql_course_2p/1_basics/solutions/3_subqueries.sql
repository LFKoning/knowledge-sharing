-- 1. Bouw eerst de gevraagde query op.
SELECT
  *,
  DATE(DatumTijd) AS Datum,
  TIME(DatumTijd) AS Tijd,
  Aantal * Prijs AS Omzet
FROM Transacties


-- 2. Gebruik de query als CTE.
WITH AnalyseTabel AS (
  SELECT
    *,
    DATE(DatumTijd) AS Datum,
    TIME(DatumTijd) AS Tijd,
    Aantal * Prijs AS Omzet
  FROM Transacties
)
SELECT *
FROM AnalyseTabel
WHERE Datum = '2024-01-01'
ORDER BY Omzet DESC
;
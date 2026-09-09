-- 1. Berekeken omzet voor elke transactie regel.
SELECT
  *,
  Prijs * Aantal AS Omzet
FROM Transacties
;


-- 2. Maak uniek ID voor elke regel.
SELECT
  *,
  CONCAT(TransactieId, '-', RegelNummer) AS LineId
FROM Transacties
ORDER BY TransactieId, RegelNummer
;


-- 3. Haal datum uit de DatumTijd kolom.
SELECT
  *,
  DATE(DatumTijd) AS Datum
FROM Transacties
;


-- 4. Haal dag van de week uit de DatumTijd kolom.
SELECT
  *,
  STRFTIME('%u', DatumTijd) AS WeekDag
FROM Transacties
;

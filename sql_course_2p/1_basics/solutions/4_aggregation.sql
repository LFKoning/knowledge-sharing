-- Open 0_data/sales_data.db.


-- 1. Aantal en omzet per dag.
SELECT
  DATE(DatumTijd) AS Datum,
  SUM(Aantal) AS DagTotaal,
  SUM(Aantal * Prijs) AS DagOmzet
FROM Transacties
GROUP BY DATE(DatumTijd)
;


-- 2. Verschil met vorige dag.
WITH DagTabel AS (
  SELECT
    DATE(DatumTijd) AS Datum,
    SUM(Aantal) AS DagTotaal,
    SUM(Aantal * Prijs) AS DagOmzet
  FROM Transacties
  GROUP BY DATE(DatumTijd)
)
SELECT
  Datum,
  DagTotaal,
  DagTotaal - LAG(DagTotaal, 1) OVER (ORDER BY Datum)  AS VerschilTotaal,
  DagOmzet,
  DagOmzet - LAG(DagOmzet, 1) OVER (ORDER BY Datum) AS VerschilOmzet
FROM DagTabel
;


-- 3. Voortschrijdend gemiddelde over 3 dagen.
WITH DagTabel AS (
  SELECT
    DATE(DatumTijd) AS Datum,
    SUM(Aantal * Prijs) AS DagOmzet
  FROM Transacties
  GROUP BY DATE(DatumTijd)
)
SELECT
  *,
  AVG(DagOmzet) OVER(
    ORDER BY Datum
	  ROWS BETWEEN 3 PRECEDING AND CURRENT ROW
  ) AS Gemiddeld3Dagen
FROM DagTabel
;
-- 1. Aantal en omzet per dag.
SELECT
  DATE(DatumTijd) AS Datum,
  SUM(Aantal) AS DagTotaal,
  SUM(Aantal * Prijs) AS DagOmzet
FROM Transacties
GROUP BY DATE(DatumTijd);


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
  *,
  DagTotaal - LAG(DagTotaal, 1) OVER (ORDER BY Datum)  AS VerschilTotaal,
  DagOmzet - LAG(DagOmzet, 1) OVER (ORDER BY Datum) AS VerschilOmzet
FROM DagTabel;



-- 3. Voortschrijdend gemiddelde toevoegen.
WITH DagTabel AS (
  SELECT
    DATE(DatumTijd) AS Datum,
    SUM(Aantal) AS DagTotaal,
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
FROM DagTabel;
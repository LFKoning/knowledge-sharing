WITH
InclusiefBTW AS (
	-- Bereken omzet inclusief BTW.
	SELECT
		BestelDatum,
		Aantal,
		CASE
			WHEN BTWTarief = 'laag' THEN
				Aantal * PrijsExclusief * 1.09
			ELSE
				Aantal * PrijsExclusief * 1.21
		END AS OmzetInclusief
	FROM Transacties
),
DagTotalen AS (
	-- Aggregeer op BestelDatum.
	SELECT
		BestelDatum,
		SUM(Aantal) AS DagAantal,
		SUM(OmzetInclusief) AS DagOmzet
	FROM InclusiefBTW
	GROUP BY BestelDatum
)
SELECT
	-- Dagelijkse ruwe waardes.
	BestelDatum,
	DagAantal,
	DagOmzet,
	
	-- Verschil met vorige dag.
	DagAantal - LAG(DagAantal, 1) OVER(ORDER BY BestelDatum) AS AantalVerschil,
	DagOmzet - LAG(DagOmzet, 1) OVER(ORDER BY BestelDatum) AS OmzetVerschil,
	
	-- Voortschrijdend gemiddelde over 7 dagen.
	AVG(DagOmzet) OVER(ORDER BY BestelDatum ROWS BETWEEN 7 PRECEDING AND CURRENT ROW) AS OmzetGemiddelde
	
FROM DagTotalen;
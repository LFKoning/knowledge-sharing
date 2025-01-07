WITH InclusiefBTW AS (
	SELECT
		Aantal,
		Aantal * PrijsExclusief AS Totaal,
		CASE
			WHEN BTWTarief = 'laag' THEN
				Aantal * PrijsExclusief * 1.09
			ELSE
				Aantal * PrijsExclusief * 1.21
		END AS TotaalInclusief
	FROM Transacties
)
SELECT
	AVG(Aantal),
	AVG(Totaal) AS TotaalGemiddeld,
	AVG(TotaalInclusief) AS TotaalInclusiefGemiddeld
FROM InclusiefBTW;
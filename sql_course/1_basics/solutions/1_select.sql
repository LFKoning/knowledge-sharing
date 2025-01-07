SELECT *
FROM Transacties
WHERE BestelDatum = '2020-02-02'
;


SElECT *
FROM Transacties
WHERE
	KlantId = 6
	AND BTWTarief = 'laag'
;


SELECT *
FROM Transacties
ORDER BY PrijsExclusief DESC
LIMIT 3
;
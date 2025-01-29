-- 1. View geaggregeerd per transactie.
-- Noot: KlantId en DatumTijd heb je later nodig.
CREATE VIEW vwTransacties AS
SELECT
	TransactieId,
	KlantId,
	DatumTijd,
	SUM(Aantal) AS Aantal,
	SUM(Aantal * Prijs) AS Omzet
FROM Transacties
GROUP BY
	TransactieId,
	KlantId,
	DatumTijd
;


-- 2. View geaggregeerd per klant en maand.
CREATE VIEW vwKlantMaandelijks AS
SELECT
	kln.KlantId,
	kln.Naam,
	STRFTIME('%Y-%m', trn.DatumTijd) AS Maand,
	SUM(trn.Omzet) AS Omzet
FROM vwTransacties trn
LEFT JOIN Klanten as kln
	ON trn.KlantId = kln.KlantId
GROUP BY
	trn.KlantId,
	STRFTIME('%Y-%m', trn.DatumTijd)
;


-- 3. View geaggregeerd op klant.
CREATE VIEW vwKlantOmzet AS
SELECT
	trn.KlantId,
	kln.Naam,
	SUM(trn.Omzet) AS OmzetTotaal
FROM vwTransacties trn
LEFT JOIN Klanten as kln
	ON trn.KlantId = kln.KlantId
GROUP BY trn.KlantId
ORDER BY OmzetTotaal DESC
;
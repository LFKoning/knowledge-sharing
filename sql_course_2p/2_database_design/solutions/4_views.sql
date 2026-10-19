-- 1. View omzet per klant.
CREATE VIEW vwKlantOmzet AS
SELECT
	trn.KlantId,
	kln.Naam,
	SUM(trn.Aantal * trn.Prijs) AS OmzetTotaal
FROM Transacties AS trn
LEFT JOIN Klanten AS kln USING(KlantId)
GROUP BY trn.KlantId
ORDER BY OmzetTotaal DESC
;

-- 2. View aantal en omzet per transactie.
-- Noot: KlantId en DatumTijd voor vraag 3.
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


-- 3. View transacties en omzet per klant en maand.
CREATE VIEW vwKlantMaandelijks AS
SELECT
	kln.KlantId,
	kln.Naam,
	STRFTIME('%Y-%m', trn.DatumTijd) AS JaarMaand,
	COUNT(*) AS AantalTransacties,
	SUM(trn.Omzet) AS Omzet
FROM vwTransacties AS trn
LEFT JOIN Klanten AS kln USING(KlantId)
GROUP BY
	trn.KlantId,
	JaarMaand
;



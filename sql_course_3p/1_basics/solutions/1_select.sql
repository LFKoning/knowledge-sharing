-- 1. Selectie met WHERE.
SELECT *
FROM Transacties
WHERE DatumTijd >= '2024-01-01'
  AND DatumTijd < '2024-01-02'
;

-- 1. Selectie met BETWEEN.
SELECT *
FROM Transacties
WHERE DatumTijd BETWEEN '2024-01-01' AND '2024-01-02'
;

-- 1. Selectie met LIKE.
SELECT *
FROM Transacties
WHERE DatumTijd LIKE '2024-01-01%'
;


-- 2. Top 3 transacties qua aantal.
SELECT *
FROM Transacties
ORDER BY Aantal DESC
LIMIT 10
;


-- 3. Alle transacties van de beste klant.
SELECT *
FROM Transacties
WHERE KlantId = 'CST-77700'
ORDER BY DatumTijd, RegelNummer
;

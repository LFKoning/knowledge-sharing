-- 1. Query op willekeurig product ID.
SELECT * FROM Transacties
WHERE ProductId = 'PRD-00408'
;


-- 2. Query plan zeg SCAN de hele tabel...
EXPLAIN QUERY PLAN
SELECT * FROM Transacties
WHERE ProductId = 'PRD-00408'
;


-- 3. Maak een index op ProductId.
CREATE INDEX IDX_ProductId ON Transacties(ProductId);


-- 4. Query plan gebruikt nu de index!
EXPLAIN QUERY PLAN
SELECT * FROM Transacties
WHERE ProductId = 'PRD-00408'
;


-- 5. Werkt niet met LIKE...
EXPLAIN QUERY PLAN
SELECT * FROM Transacties
WHERE ProductId LIKE 'PRD-004%'
;


-- 5. Ook niet met een transformatie...
EXPLAIN QUERY PLAN
SELECT * FROM Transacties
WHERE LOWER(ProductId) = 'prd-00408'
;
-- 1. Query op willekeurig product ID.
-- Noteer de tijd in ms.
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


-- 4. Merk op dat de query sneller is!
SELECT * FROM Transacties
WHERE ProductId = 'PRD-00408'
;


-- 5. Werkt ook met LIKE.
EXPLAIN QUERY PLAN
SELECT * FROM Transacties
WHERE ProductId = '%408%'
;


-- 5. Maar niet met een transformatie...
EXPLAIN QUERY PLAN
SELECT * FROM Transacties
WHERE LOWER(ProductId) = 'prd-00408'
;
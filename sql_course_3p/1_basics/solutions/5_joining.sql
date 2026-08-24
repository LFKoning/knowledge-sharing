-- 1. LEFT JOIN KoppelA en KoppelB.
-- KoppelA bepaalt welke rijen in het resultaat komen.
SELECT *
FROM KoppelA
LEFT JOIN KoppelB USING (Id);


-- 2. RIGHT JOIN KoppelB en KoppelA.
-- Merk op: zelfde rijen als LEFT JOIN hierboven.
SELECT *
FROM KoppelB
RIGHT JOIN KoppelA USING (Id);


-- 3. INNER JOIN KoppelA en KoppelB.
-- Alleen gedeelde IDs in het resultaat.
SELECT *
FROM KoppelA
INNER JOIN KoppelB USING (Id);

-- 4. Standaard JOIN KoppelA en KoppelB.
-- Komt overeen met de INNER JOIN hierboven.
SELECT *
FROM KoppelA
JOIN KoppelB USING (Id);
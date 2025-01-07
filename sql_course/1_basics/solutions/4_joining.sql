-- 1. RIGHT JOIN KoppelA en KoppelB.
-- KoppelB bepaalt welke rijen meekomen.
SELECT *
FROM KoppelA
RIGHT JOIN KoppelB USING (Id);


-- 2. LEFT JOIN KoppelB en KoppelA.
-- Zelfde set rijen als RIGHT JOIN hierboven.
SELECT *
FROM KoppelB
LEFT JOIN KoppelA USING (Id);


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
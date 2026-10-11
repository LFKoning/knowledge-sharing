-- Open 0_data/join_types.db.


-- 1. LEFT JOIN TabelA en TabelB.
-- TabelA bepaalt welke rijen in het resultaat komen.
SELECT *
FROM
  TabelA TA
LEFT JOIN TabelB TB 
  ON TA.IdA = TB.IdB
;


-- 2. RIGHT JOIN TabelB en TabelA.
-- Merk op: zelfde rijen als LEFT JOIN hierboven.
SELECT *
FROM TabelB TB
RIGHT JOIN TabelA TA
  ON TA.IdA = TB.IdB
;


-- 3. INNER JOIN TabelA en TabelB.
-- Alleen gedeelde IDs in het resultaat.
SELECT *
FROM TabelA TA
INNER JOIN TabelB TB
  ON TA.IdA = TB.IdB
;


-- 4. Standaard JOIN TabelA en TabelB.
-- Komt overeen met de INNER JOIN hierboven.
SELECT *
FROM TabelA TA
JOIN TabelB TB
  ON TA.IdA = TB.IdB
;
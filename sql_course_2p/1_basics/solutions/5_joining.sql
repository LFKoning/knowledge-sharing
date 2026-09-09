-- 1. LEFT JOIN TabelA en TabelB.
-- TabelA bepaalt welke rijen in het resultaat komen.
SELECT 
	TabelA.*,
	TabelB.*
FROM TabelA
LEFT JOIN TabelB USING (Id);


-- 2. RIGHT JOIN TabelB en TabelA.
-- Merk op: zelfde rijen als LEFT JOIN hierboven.
SELECT
	TabelA.*,
	TabelB.*
FROM TabelB
RIGHT JOIN TabelA USING (Id);


-- 3. INNER JOIN TabelA en TabelB.
-- Alleen gedeelde IDs in het resultaat.
SELECT
	TabelA.*,
	TabelB.*
FROM TabelA
INNER JOIN TabelB USING (Id);


-- 4. Standaard JOIN TabelA en TabelB.
-- Komt overeen met de INNER JOIN hierboven.
SELECT
	TabelA.*,
	TabelB.*
FROM TabelA
JOIN TabelB USING (Id);
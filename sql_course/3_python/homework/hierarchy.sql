-- Categorie tabel met verwijzing naar zichzelf.
CREATE TABLE ProductCategorie (
	CategorieId		INTEGER PRIMARY KEY,
	ValtOnderId		INTEGER,
	Omschrijving	TEXT NOT NULL,
	
	FOREIGN KEY(ValtOnderId)
		REFERENCES ProductCategorie(CategorieId)
);


-- Dummy categorie data.
INSERT INTO ProductCategorie (ValtOnderId, Omschrijving)
VALUES
	(NULL, 'Voeding'),
	(1, 'Vers'),
	(2, 'Fruit'),
	(3, 'Groente')
;


WITH RECURSIVE Hierarchie AS (
    VALUES(3)
    UNION
    SELECT CategorieId FROM org, works_for_alice
     WHERE org.boss=works_for_alice.n
  )
SELECT avg(height) FROM org
 WHERE org.name IN works_for_alice;



-- Recursieve query.
WITH RECURSIVE
	Hierarchie AS (
		-- Selecteer doel categorie.
		SELECT
			CategorieId,
			ValtOnderId,
			Omschrijving
		FROM ProductCategorie
		WHERE Omschrijving = 'Fruit'
	UNION
		-- Ga omhoog in de hierarchie.
		SELECT
			cat.CategorieId,
			cat.ValtOnderId,
			cat.Omschrijving
		FROM ProductCategorie cat
		JOIN Hierarchie hrc
			ON hrc.ValtOnderId = cat.CategorieId
)
SELECT * FROM Hierarchie
;
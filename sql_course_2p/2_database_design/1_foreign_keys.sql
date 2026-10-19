/* Create tables */

CREATE TABLE Klanten (
	KlantId INTEGER PRIMARY KEY,
	Naam TEXT
);

CREATE TABLE Transacties (
	TransactieId INTEGER PRIMARY KEY,
	KlantId INTEGER,
	Beschrijving TEXT,

	-- Koppelsleutel die verwijderingen doorvoert.
	FOREIGN KEY(KlantId)
		REFERENCES Klanten(KlantId)
		ON DELETE CASCADE
);


/* Invoeren */


-- Turn FOREIGN KEY contraints on!
PRAGMA foreign_keys = ON;

-- Klant invoeren.
INSERT INTO Klanten (Naam) VALUES("Piet Klaasen");

-- Transacties voor KlantId = 1.
INSERT INTO Transacties (KlantId, Beschrijving)
VALUES (1, 'Transactie 1'), (1, 'Transactie 2');

-- Transacties voor KlantId = 2 => foutmelding.
INSERT INTO Transacties (KlantId, Beschrijving)
VALUES (2, 'Transactie niet bestaande klant1');


/* Verwijderen */


-- Turn FOREIGN KEY contraints on!
PRAGMA foreign_keys = ON;

-- Verwijderen KlantId 1 verwijdert ook alle transacties.
DELETE FROM Klanten WHERE KlantId = 1;
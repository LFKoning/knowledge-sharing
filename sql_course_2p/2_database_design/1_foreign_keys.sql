-- Opschonen database.
DROP TABLE IF EXISTS Transacties;
DROP TABLE IF EXISTS Klanten;

-- Aanmaken tabellen.
CREATE TABLE Klanten (
	KlantId INTEGER PRIMARY KEY,
	Naam TEXT
);

CREATE TABLE Transacties (
	TransactieId INTEGER PRIMARY KEY,
	KlantId INTEGER,
	Beschrijving TEXT,

	-- Verwijzende sleutel die verwijderingen doorvoert.
	FOREIGN KEY(KlantId)
		REFERENCES Klanten(KlantId)
		ON DELETE CASCADE
);


-- Klant invoeren.
INSERT INTO Klanten (Naam) VALUES("Piet Klaasen");

-- Transacties KlantId 1 invoeren.
INSERT INTO Transacties (KlantId, Beschrijving)
VALUES (1, 'Transactie 1'), (1, 'Transactie 2');

-- Foutmelding: KlantId 2 bestaat niet...
INSERT INTO Transacties (KlantId, Beschrijving)
VALUES (2, 'Transactie niet bestaande klant1');


-- Verwijderen transactie (geen effect).
DELETE FROM Transacties WHERE TransactieId = 2;

-- Verwijderen klant verwijdert ook alle transacties.
DELETE FROM Klanten WHERE KlantId = 1;

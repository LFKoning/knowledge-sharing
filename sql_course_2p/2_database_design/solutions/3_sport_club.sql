/*=====================================================
  Maak eerst alle tabellen zonder verwijzende sleutels.
=====================================================*/

-- Categorie waarin een lid speelt.
CREATE TABLE SpelerCategorie (
	CategorieId		INTEGER PRIMARY KEY,
	Omschrijving	TEXT NOT NULL
);


-- Contributie bedrag per jaar.
CREATE TABLE Contributie (
	ContributieId	INTEGER PRIMARY KEY,
	Jaar			INTEGER NOT NULL,
	Bedrag			REAL NOT NULL
);


-- Toernooien.
CREATE TABLE Toernooien (
	ToernooiId		INTEGER PRIMARY KEY,
	Omschrijving	TEXT NOT NULL,
	Jaar			INTEGER NOT NULL,
	Bedrag			REAL NOT NULL
);


-- BetalingStatusCode.
CREATE TABLE BetalingStatusCodes (
	StatusCodeId	INTEGER PRIMARY KEY,
	Omschrijving	TEXT
);


/*=====================================================
  Maak daarna alle tabellen met verwijzende sleutels.
=====================================================*/

-- Leden tabel, verwijzing naar categorie.
CREATE TABLE Leden (
	LedenId			INTEGER PRIMARY KEY,
	CategorieId		INTEGER NOT NULL,
	Voornaam		TEXT NOT NULL,
	Achternaam		TEXT NOT NULL,
	Geboortedatum	DATE,

	UNIQUE(Voornaam, Achternaam),

	FOREIGN KEY(CategorieId)
	  REFERENCES SpelerCategorie(CategorieId)
);


-- Toernooi inschrijvingen, verwijzingen naar Toernooien en Leden.
CREATE TABLE ToernooiInschrijving (
	InschrijvingId	INTEGER PRIMARY KEY,
	ToernooiId		INTEGER NOT NULL,
	LedenId			INTEGER NOT NULL,
	Uitslag			INTEGER,

	UNIQUE(ToernooiId, LedenId),

	FOREIGN KEY(ToernooiId)
	  REFERENCES Toernooien(ToernooiId),

	FOREIGN KEY(LedenId)
	  REFERENCES Leden(LedenId)
);


-- Betalingen, verwijzingen naar Toernooien en Leden.
CREATE TABLE Betalingen (
	BetalingId		INTEGER PRIMARY KEY,
	LedenId			INTEGER NOT NULL,
	ContributieId	INTEGER DEFAULT NULL,
	ToernooiId		INTEGER DEFAULT NULL,

	FOREIGN KEY(LedenId)
	  REFERENCES Leden(LedenId),

	FOREIGN KEY(ContributieId)
	  REFERENCES Contributie(ContributieId),

	FOREIGN KEY(ToernooiId)
	  REFERENCES Toernooien(ToernooiId),

	CHECK (
		ContributieId IS NOT NULL
		OR ToernooiId IS NOT NULL
	)
);


-- BetalingStatus, verwijzingen naar Toernooien en Leden.
CREATE TABLE BetalingStatus (
	StatusId		INTEGER PRIMARY KEY,
	BetalingId		INTEGER NOT NULL,
	StatusCodeId	INTEGER NOT NULL,
	Datum			DATETIME NOT NULL,

	FOREIGN KEY(BetalingId)
	  REFERENCES Betalingen(BetalingId),

	FOREIGN KEY(StatusCodeId)
	  REFERENCES BetalingStatusCodes(StatusCodeId)
);

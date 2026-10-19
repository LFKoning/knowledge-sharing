/*=====================================================
  Maak eerst alle tabellen zonder verwijzende sleutels.
=====================================================*/

-- Categorie waarin een lid speelt.
CREATE TABLE SpelerCategorie (
	CategorieId		INTEGER PRIMARY KEY,
	Omschrijving	TEXT NOT NULL
);

-- Specificatie jaarlijkse contributie.
CREATE TABLE Contributie (
	ContributieId	INTEGER PRIMARY KEY,
	Jaar			INTEGER NOT NULL,
	Bedrag			REAL NOT NULL
);

-- Specificatie toernooien.
CREATE TABLE Toernooien (
	ToernooiId		INTEGER PRIMARY KEY,
	Omschrijving	TEXT NOT NULL,
	Jaar			INTEGER NOT NULL,
	Bedrag			REAL NOT NULL
);

-- Status codes van betalingen.
CREATE TABLE BetaalStatusCodes (
	StatusCodeId	INTEGER PRIMARY KEY,
	Omschrijving	TEXT
);


/*=====================================================
  Maak daarna alle tabellen met verwijzende sleutels.
=====================================================*/

-- Leden tabel, verwijzing naar SpelerCategorie.
CREATE TABLE Leden (
	LedenId			INTEGER PRIMARY KEY,
	CategorieId		INTEGER NOT NULL,
	Voornaam		TEXT NOT NULL,
	Achternaam		TEXT NOT NULL,

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

-- Contributiebetalingen, verwijzingen naar Leden, Contributie en BetaalStatusCodes.
CREATE TABLE BetaalStatusContributie (
	StatusId		INTEGER PRIMARY KEY,
	LedenId			INTEGER NOT NULL,
	ContributieId	INTEGER NOT NULL,
	StatusCodeId	INTEGER NOT NULL,
	StatusDatum		DATETIME NOT NULL,

	FOREIGN KEY(LedenId)
	  REFERENCES Leden(LedenId),

	FOREIGN KEY(ContributieId)
	  REFERENCES Contributie(ContributieId),
	
	FOREIGN KEY(StatusCodeId)
	  REFERENCES BetaalStatusCodes(StatusCodeId)
);


-- Toernooibetalingen, verwijzingen naar ToernooiInschrijving en BetaalStatusCodes.
CREATE TABLE BetaalStatusInschrijving (
	StatusId		INTEGER PRIMARY KEY,
	InschrijvingId	INTEGER NOT NULL,
	StatusCodeId	INTEGER NOT NULL,
	StatusDatum		DATETIME NOT NULL,
	
	FOREIGN KEY(InschrijvingId)
	  REFERENCES ToernooiInschrijving(InschrijvingId),

	FOREIGN KEY(StatusCodeId)
	  REFERENCES BetaalStatusCodes(StatusCodeId)

);

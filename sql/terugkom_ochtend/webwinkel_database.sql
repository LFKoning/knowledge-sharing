CREATE TABLE Landen (
	LandId				INTEGER PRIMARY KEY,
	Naam				TEXT NOT NULL,
	Taal				Text NOT NULL,
	ISOCode				TEXT NOT NULL,
	Bezorgkosten		REAL NOT NULL
);

CREATE TABLE BetaalMethodes (
	BetaalMethodeId		INTEGER PRIMARY KEY,
	Naam				TEXT NOT NULL,
	Kosten				REAL NOT NULL DEFAULT 0,
	Actief				INTEGER DEFAULT 1
);

CREATE TABLE BetaalStatus (
	BetaalStatusId		INTEGER PRIMARY KEY,
	Omschrijving		TEXT
);

CREATE TABLE Adressen (
	AdresId				INTEGER PRIMARY KEY,
	Straat				TEXT NOT NULL,
	Huisnummer			INTEGER NOT NULL,
	Toevoeging			TEXT,
	Postcode			TEXT NOT NULL,
	Plaats				TEXT NOT NULL,
	LandId				INTEGER NOT NULL,

	CONSTRAINT FK_AdresLand
		FOREIGN KEY(LandId)
		REFERENCES Landen(LandId)
);

CREATE TABLE Klanten (
	KlantId				INTEGER PRIMARY KEY,
	Voornaam			TEXT NOT NULL,
	Achternaam			TEXT NOT NULL,
	BezorgAdresId		INTEGER NOT NULL,
	FactuurAdresId		INTEGER DEFAULT NULL,
	EersteLogin			DATETIME DEFAULT CURRENT_TIMESTAMP,
	LaatsteLogin		DATETIME DEFAULT NULL,
	
	CONSTRAINT FK_BestellingBezorgAdres
		FOREIGN KEY(BezorgAdresId)
		REFERENCES Adressen(AdresId)
		
	CONSTRAINT FK_BestellingFactuurAdres
		FOREIGN KEY(FactuurAdresId)
		REFERENCES Adressen(AdresId)
);

CREATE TABLE Productgroepen (
	ProductgroepId		INTEGER PRIMARY KEY,
	ProductgroepNaam	TEXT NOT NULL
);

CREATE TABLE Producten (
	ProductId			INTEGER PRIMARY KEY,
	ProductgroepId		INTEGER NOT NULL,
	Naam				TEXT NOT NULL,
	EANCode				TEXT NOT NULL,
	
	CONSTRAINT FK_ProductProductgroep
		FOREIGN KEY(ProductgroepId)
		REFERENCES Productgroepen(ProductgroepId)
);

CREATE TABLE ProductKenmerken (
	KenmerkId			INTEGER PRIMARY KEY,
	ProductId			INTEGER NOT NULL,
	Kenmerk				TEXT NOT NULL,
	Waarde				TEXT DEFAULT NULL,
	
	CONSTRAINT FK_ProductKenmerkProduct
		FOREIGN KEY(ProductId)
		REFERENCES Producten(ProductId)
);

CREATE TABLE Bestellingen (
	BestellingId		INTEGER PRIMARY KEY,
	KlantId				INTEGER NOT NULL,
	BezorgAdresId		INTEGER NOT NULL,
	FactuurAdresId		INTEGER DEFAULT NULL,
	KortingId			INTEGER DEFAULT NULL,
	BestelDatum			DATE NOT NULL,
	
	CONSTRAINT FK_BestellingKlant
		FOREIGN KEY(KlantId)
		REFERENCES Klanten(KlantId)

	CONSTRAINT FK_BestellingBezorgAdres
		FOREIGN KEY(BezorgAdresId)
		REFERENCES Adressen(AdresId)
		
	CONSTRAINT FK_BestellingFactuurAdres
		FOREIGN KEY(FactuurAdresId)
		REFERENCES Adressen(AdresId)
	
	CONSTRAINT FK_BestellingKorting
		FOREIGN KEY(KortingId)
		REFERENCES BestellingKortingen(KortingId)
);

CREATE TABLE Betalingen (
	BetalingId			INTEGER PRIMARY KEY,
	BestellingId		INTEGER NOT NULL,
	BetaalMethodeId		INTEGER NOT NULL,
	BetaalStatusId		INTEGER NOT NULL,
	BetaalStatusDatum	DATETIME NOT NULL,

	CONSTRAINT FK_BetalingBestelling
		FOREIGN KEY(BestellingId)
		REFERENCES Bestellingen(BestellingId)

	CONSTRAINT FK_BetalingenBetaalMethode
		FOREIGN KEY(BetaalMethodeId)
		REFERENCES BetaalMethodes(BetaalMethodeId)

	CONSTRAINT FK_BetalingenBetaalStatus
		FOREIGN KEY(BetaalStatusId)
		REFERENCES BetaalStatus(BetaalStatusId)
);

CREATE TABLE BestelRegels (
	BestelRegelId		INTEGER PRIMARY KEY,
	BestellingId		INTEGER NOT NULL,
	ProductId			INTEGER NOT NULL,
	PrijsId				INTEGER NOT NULL,
	KortingId			INTEGER DEFAULT NULL,
	Aantal				INTEGER NOT NULL,

	CONSTRAINT FK_BestelRegelBestelling
		FOREIGN KEY(BestellingId)
		REFERENCES Bestellingen(BestellingId)

	CONSTRAINT FK_BestelRegelProduct
		FOREIGN KEY(ProductId)
		REFERENCES Producten(ProductId)

	CONSTRAINT FK_BestelRegelPrijs
		FOREIGN KEY(PrijsId)
		REFERENCES Prijzen(PrijsId)
	
	CONSTRAINT FK_BestelRegelKorting
		FOREIGN KEY(KortingId)
		REFERENCES ProductKortingen(KortingId)
);

CREATE TABLE Prijzen (
	PrijsId				INTEGER PRIMARY KEY,
	ProductId			INTEGER NOT NULL,
	Prijs				REAL NOT NULL,
	GeldigVan			DATE NOT NULL DEFAULT CURRENT_DATE,
	GeldigTot			DATE NOT NULL DEFAULT "9999-12-31",

	CONSTRAINT FK_PrijzenProduct
		FOREIGN KEY(ProductId)
		REFERENCES Producten(ProductId)
);

CREATE TABLE ProductKortingen (
	KortingId			INTEGER PRIMARY KEY,
	ProductId			INTEGER NOT NULL,
	KortingPercentage	INTEGER DEFAULT 0,
	KortingBedrag		REAL DEFAULT 0,
	MinimumAantal		INTEGER DEFAULT 1,
	GeldigVan			DATE DEFAULT CURRENT_DATE,
	GeldigTot			DATE NOT NULL,
	Omschrijving		TEXT NOT NULL,
	
	CONSTRAINT FK_ProductKortingenProduct
		FOREIGN KEY(ProductId)
		REFERENCES Producten(ProductId)
);

CREATE TABLE BestellingKortingen (
	KortingId			INTEGER PRIMARY KEY,
	KortingPercentage	INTEGER DEFAULT 0,
	KortingBedrag		REAL DEFAULT 0,
	MinimumBedrag		REAL NOT NULL,
	GeldigVan			DATE DEFAULT CURRENT_DATE,
	GeldigTot			DATE NOT NULL,
	Omschrijving		TEXT NOT NULL
);

CREATE TABLE Voorraad (
	VoorraadId			INTEGER PRIMARY KEY,
	ProductId			INTEGER NOT NULL,
	MutatieType			TEXT NOT NULL,
	MutatieAantal		INTEGER NOT NULL,
	MutatieDatum		DATE NOT NULL,

	CONSTRAINT FK_VoorraadProduct
		FOREIGN KEY(ProductId)
		REFERENCES Producten(ProductId)
);
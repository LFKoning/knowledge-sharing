-- Drop existing tables.
DROP TABLE IF EXISTS Klanten;

DROP TABLE IF EXISTS Producten;

DROP TABLE IF EXISTS Transacties;

-- Customer table definition.
CREATE TABLE Klanten (
    KlantId TEXT PRIMARY KEY,
    Naam TEXT,
    Email TEXT,
    Geboortedatum DATE,
    Adres TEXT,
    Postcode TEXT,
    Stad TEXT,
    Aangemaakt DATE
);

-- Product table definition.
CREATE TABLE Producten (
    ProductId TEXT PRIMARY KEY,
    Naam TEXT,
    Verpakking REAL,
    VerpakkingEenheid TEXT,
    Categorie TEXT,
    Subcategorie TEXT,
    Prijs REAL
);

-- Transaction table definition.
CREATE TABLE Transacties (
    TransactieId TEXT,
    KlantId TEXT,
    ProductId TEXT,
    DatumTijd DATETIME,
    RegelNummer INTEGER,
    Aantal INTEGER,
    Prijs REAL,
    PRIMARY KEY(TransactieId, RegelNummer)
);
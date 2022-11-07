INSERT INTO Landen (LandId, Naam, Taal, ISOCode, Bezorgkosten)
	VALUES
		(1, "Nederland", "Nederlands", "NL", 0.0),
		(2, "Duitsland", "Duits", "DE", 5.0)
;
	
INSERT INTO BetaalMethodes (BetaalMethodeId, Naam, Kosten, Actief)
	VALUES
		(1, "iDeal", 0.0, 1),
		(2, "PayPal", 1.0, 1)
;
	
INSERT INTO BetaalStatus (BetaalStatusId, Omschrijving)
	VALUES
		(1, "Nog niet voldaan"),
		(2, "In behandeling"),
		(3, "Voldaan"),
		(4, "Mislukt")
;

INSERT INTO Adressen (
		AdresId, Straat, Huisnummer, Toevoeging, Postcode, Plaats, LandId
	)
	VALUES
		(1, "Blaatstraat", 2, NULL, "1234 AB", "Amsterdam", 1),
		(2, "Kantoorstraat", 3, "A", "5678 CD", "Rotterdam", 1),
		(3, "Thuisstraat", 4, NULL, "9999 XY", "Haarlem", 1)
;

INSERT INTO Klanten (
		KlantId, Voornaam, Achternaam, BezorgAdresId, FactuurAdresId,
		EersteLogin, LaatsteLogin
	)
	VALUES
		(1, "Pieter", "Cornelissen", 1, NULL, "2015-05-21T12:03:09", "2022-03-05T11:14:56"),
		(2, "Ingrid", "Maassen", 3, 3, "2018-03-10T09:44:01", "2022-06-15T17:56:01")
;

INSERT INTO Productgroepen (ProductgroepId, ProductgroepNaam)
	VALUES
		(1, "Boeken"),
		(2, "Speelgoed"),
		(3, "Verzorging")
;

INSERT INTO Producten (ProductId, ProductgroepId, Naam, EANCode)
	VALUES
		(1, 1, "Jip en Janneke voorleesboek", "EAN0010001"),
		(2, 2, "LEGO DUPLO Brandweerauto", "EAN0020001"),
		(3, 3, "Huismerk shampoo", "EAN0030001")
;

INSERT INTO ProductKenmerken (KenmerkId, ProductId, Kenmerk, Waarde)
	VALUES
		(1, 1, "Aantal pagina's", "535"),
		(2, 1, "Auteur", "Annie M.G. Schmidt"),
		(3, 2, "Setnummer", "10969"),
		(4, 2, "Aantal onderdelen", "5000"),
		(5, 3, "Inhoud", "500 ml")
;

INSERT INTO Prijzen (PrijsId, ProductId, Prijs, GeldigVan, GeldigTot)
	VALUES
		(1, 1, 16.50, "2022-01-01", "9999-12-31"),
		(2, 2, 8.99, "2022-01-01", "9999-12-31"),
		(3, 3, 2.35, "2022-01-01", "2022-01-15"),
		(4, 3, 2.69, "2022-01-15", "2022-01-31"),
		(5, 3, 2.35, "2022-01-31", "9999-12-31")
;

INSERT INTO ProductKortingen (
		KortingId, ProductId, KortingPercentage, KortingBedrag,
		MinimumAantal, GeldigVan, GeldigTot, Omschrijving
	)
	VALUES
		(1, 3, 33.33, NULL, 3, "2022-01-17", "2022-01-23", "Deze week: 3 flessen shampoo voor de prijs van 2!")
;

INSERT INTO BestellingKortingen (
		KortingId, KortingPercentage, KortingBedrag, MinimumBedrag,
		GeldigVan, GeldigTot, Omschrijving
	)
	VALUES
		(1, NULL, 5, 50, "2022-01-01", "2022-01-31", "Heel januari: 5 EURO KORTING bij besteding van 50 euro!")
;

INSERT INTO Bestellingen (
		BestellingId, KlantId, BezorgAdresId, FactuurAdresId, BestelDatum, KortingId
	)
	VALUES
		(1, 1, 1, NULL, "2022-01-15", 1),
		(2, 2, 2, 3, "2022-01-17", NULL)
;

INSERT INTO BestelRegels
		(BestelRegelId, BestellingId, ProductId, PrijsId, KortingId, Aantal)
	VALUES
		(1, 1, 1, 1, NULL, 1),
		(2, 1, 2, 2, NULL, 1),
		(3, 2, 3, 4, 1, 3)
;
 
INSERT INTO Betalingen (
		BetalingId, BestellingId, BetaalMethodeId, BetaalStatusId, BetaalStatusDatum
	)
	VALUES
		(1, 1, 1, 1, "2022-01-15T13:37:00"),
		(2, 1, 1, 2, "2022-01-15T13:37:10"),
		(3, 1, 1, 3, "2022-01-15T13:38:15"),
		(4, 2, 1, 1, "2022-01-17T19:30:13"),
		(5, 2, 1, 2, "2022-01-17T19:30:37"),
		(6, 2, 1, 4, "2022-01-17T19:44:51"),
		(7, 2, 2, 1, "2022-01-17T19:45:20"),
		(8, 2, 2, 2, "2022-01-17T19:45:25"),
		(9, 2, 2, 3, "2022-01-17T19:45:58")
;
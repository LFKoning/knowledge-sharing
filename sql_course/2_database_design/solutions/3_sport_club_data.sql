INSERT INTO SpelerCategorie (Omschrijving)
VALUES
	('Beginner'),
	('Ervaren'),
	('Expert')
;


INSERT INTO Contributie (Jaar, Bedrag)
VALUES
	(2022, 165.99),
	(2023, 169.99),
	(2024, 174.99)
;


INSERT INTO Toernooien (Omschrijving, Jaar, Bedrag)
VALUES
	('Voorjaarstoernooi', 2022, 5.99),
	('De grote finale', 2022, 9.99),
	('Voorjaarstoernooi', 2023, 5.99),
	('De grote finale', 2023, 9.99),
	('Voorjaarstoernooi', 2024, 6.99),
	('De grote finale', 2024, 10.99)
;

INSERT INTO BetalingStatusCode (Omschrijving)
VALUES
	('Open'),
	('Herinnering'),
	('Voldaan'),
	('Mislukt')
;


INSERT INTO Leden
	(CategorieId, Voornaam, Achternaam, Geboortedatum)
VALUES
	(1, 'Mark', 'Vos', '2002-10-04'),
	(2, 'Ingrid', 'Jansen', '1977-05-04'),
	(3, 'Henk', 'Knol', '1967-06-09'),
	(1, 'Lisa', 'van Balen', '1989-03-30'),
	(2, 'Vincent', 'Molenaar', '1999-09-22'),
	(3, 'Roos', 'Geerts', '1987-05-03')
;


INSERT INTO ToernooiInschrijving
	(LedenId, ToernooiId, Uitslag)
VALUES
	(1, 4, 120),
	(1, 5, 80),
	(1, 6, 170),
	(2, 1, 200),
	(2, 3, 240),
	(3, 1, 250),
	(3, 2, 200),
	(3, 3, 280),
	(3, 4, 310),
	(3, 5, 220),
	(3, 6, 300),
	(4, 5, 250),
	(5, 4, 100),
	(5, 5, 220),
	(6, 6, 350)
;


-- Contributie betalingen.
INSERT INTO Betalingen
	(LedenId, ContributieId, ToernooiId)
VALUES
	(2, 1, NULL),
	(3, 1, NULL),
	(1, 2, NULL),
	(2, 2, NULL),
	(3, 2, NULL),
	(4, 2, NULL),
	(1, 3, NULL),
	(3, 3, NULL),
	(5, 3, NULL),
	(6, 3, NULL)
;


-- Toernooi inschrijvingen.
INSERT INTO Betalingen
	(LedenId, ContributieId, ToernooiId)
VALUES
	(2, NULL, 1),
	(3, NULL, 1),
	(3, NULL, 2),
	(2, NULL, 3),
	(3, NULL, 3),
	(1, NULL, 4),
	(3, NULL, 4),
	(5, NULL, 4),
	(1, NULL, 5),
	(3, NULL, 5),
	(4, NULL, 5),
	(5, NULL, 5),
	(1, NULL, 6),
	(3, NULL, 6),
	(6, NULL, 6)
;


-- Betalingen contributies.
INSERT INTO BetalingStatus
	(BetalingId, Datum, Status)
VALUES
	-- 2022 contributies.
	(1, '2021-11-15 00:00:00', 1),
	(2, '2021-11-15 00:00:00', 1),
	(1, '2021-12-17 15:24:12', 3),
	(2, '2021-12-28 21:10:45', 3),

	-- 2023 contributies.
	(3, '2022-11-15 00:00:00', 1),
	(4, '2022-11-15 00:00:00', 1),
	(5, '2022-11-15 00:00:00', 1),
	(6, '2022-11-15 00:00:00', 1),

	(6, '2022-12-15 00:00:00', 2),

	(3, '2022-11-16 16:42:13', 3),
	(4, '2022-12-20 09:13:56', 3),
	(5, '2022-12-04 12:10:01', 3),
	(6, '2023-01-04 18:02:43', 3),

	-- 2024 contributies.
	( 7, '2023-11-15 00:00:00', 1),
	( 8, '2023-11-15 00:00:00', 1),
	( 9, '2023-11-15 00:00:00', 1),
	(10, '2023-11-15 00:00:00', 1),

	( 9, '2022-12-15 00:00:00', 2),

	( 7, '2023-12-01 11:05:58', 3),
	( 8, '2023-11-25 20:13:02', 1),
	( 9, '2024-01-11 16:56:04', 1)

;


-- Betalingen toernooi inschrijvingen
INSERT INTO BetalingStatus
	(BetalingId, Datum, Status)
VALUES
	(10, '2022-01-15 12:00:00', 3),
	(11, '2022-01-15 12:00:00', 3),

	(12, '2022-11-15 12:00:00', 3),

	(13, '2023-01-15 12:00:00', 3),
	(14, '2023-01-15 12:00:00', 3),

	(15, '2023-11-15 12:00:00', 3),
	(16, '2023-11-15 12:00:00', 3),
	(17, '2023-11-15 12:00:00', 3),

	(18, '2024-01-15 12:00:00', 3),
	(19, '2024-01-15 12:00:00', 3),
	(20, '2024-01-15 12:00:00', 3),
	(21, '2024-01-15 12:00:00', 3),

	(22, '2024-11-15 12:00:00', 3),
	(23, '2024-11-15 12:00:00', 3),
	(24, '2024-11-15 12:00:00', 3)
;
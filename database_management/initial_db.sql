
USE Capstone
IF OBJECT_ID('nations.Nation', 'U') IS NOT NULL
	DROP TABLE nations.Nation

CREATE TABLE nations.Nation
(NationID int primary key NOT NULL,
CurrentDate date NOT NULL,
NationName varchar(35) NOT NULL,
NationPopulation int NOT NULL,
NationGDP float NOT NULL,
NationalDebt float NOT NULL,
NationLeader varchar(35) NOT NULL,
NationStability float NOT NULL,
NationHappiness float NOT NULL,
NationalAlliance varchar(20) NOT NULL
)
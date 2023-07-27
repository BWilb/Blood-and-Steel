if DB_ID('Capstone') IS NULL
	CREATE DATABASE Capstone

GO
USE Capstone

GO
IF SCHEMA_ID('nations') IS NULL
	BEGIN
		EXEC('CREATE SCHEMA nations AUTHORIZATION dbo')
	END
GO

USE Capstone
IF OBJECT_ID('nations.Nation', 'U') IS NOT NULL
	DROP TABLE nations.Nation
USE Capstone
IF OBJECT_ID('nations.Nation', 'U') IS NOT NULL
	DROP TABLE nations.Nation

CREATE TABLE nations.Nation
(NationID int primary key NOT NULL,
CurrentDate date NOT NULL,
NationName varchar(35) NOT NULL,
NationStability FLOAT NOT NULL,
NationLeader VARCHAR(35) NOT NULL,
NationPopulation int NOT NULL,
Births INT NOT NULL,
Deaths INT NOT NULL,
NationHappiness FLOAT NOT NULL,
NationGDP float NOT NULL,
NationalDebt float NOT NULL,
NationLeader varchar(35) NOT NULL,
NationalAlliance varchar(20) NOT NULL
)
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
IF OBJECT_ID('nations.nation', 'U') IS NOT NULL
	DROP TABLE nations.nation

CREATE TABLE nations.Nation
(NationID int primary key NOT NULL,
CurrentDate date NOT NULL,
NationName varchar(25) NOT NULL,
NationPopulation int NOT NULL,
NationGDP float NOT NULL,
NationalDebt float NOT NULL,
NationLeader varchar(25) NOT NULL,
NationStability float NOT NULL,
NationHappiness float NOT NULL,
NationalAlliance varchar(20) NOT NULL
)
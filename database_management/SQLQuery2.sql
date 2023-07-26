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
(NationID int primary key IDENTITY(1,1) NOT NULL,
CurrentDate date NOT NULL,
NationName varchar(35) NOT NULL,
NationStability float NOT NULL,
NationLeader varchar(35) NOT NULL,
NationalMonarch varchar(35) NOT NULL DEFAULT '',
NationPopulation int NOT NULL,
Births INT NOT NULL DEFAULT 0,
Deaths INT NOT NULL DEFAULT 0,
NationHappiness float NOT NULL,
NationGDP float NOT NULL,
NationalDebt float NOT NULL,
NationalAlliance varchar(35) NOT NULL
)
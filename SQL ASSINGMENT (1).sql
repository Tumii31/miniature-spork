  /*=============================================================
FileName: Create_Database_And_Tables.sql
Programmer: TUMI
Description: This file will create the database and tables with the necessary constraints.
=============================================================*/


Use Master
GO

--If this database exist, we will delete it first
IF EXISTS(SELECT name FROM master.dbo.sysdatabases
	       WHERE name = 'SalaryList')
BEGIN
	DROP DATABASE SalaryList
	PRINT 'The database has been deleted'
END



--Creating the database
CREATE DATABASE SalaryList
ON Primary
	(NAME = 'SalaryList_Data',
	 FILENAME = 'C:\SalaryList\SalaryList_data.mdf',
	 SIZE = 5MB,
	 FILEGROWTH = 10%)

LOG ON
	(NAME = 'SalaryList_Log',
	 FILENAME = 'C:\SalaryList\SalaryList_Log.ldf',
	 SIZE = 5MB,
	 FILEGROWTH = 10%)
GO



1.1
USE SalaryList
GO

--Creating table
CREATE TABLE Salary_list(
ID  INT IDENTITY   NOT NULL,
Fname VARCHAR(30) NOT NULL,
Lname VARCHAR(30) NOT NULL,
Salary VARCHAR(15) NOT NULL,
Primary key( ID)
)
GO

1.2
USE SalaryList
GO   

INSERT INTO Salary_list( Fname, Lname, Salary)
VALUES( 'Mandla', 'Nkosi', '12000'),
      ( 'Princewill', 'Goodluck', '28000'),
	  ( 'Angelina', 'Duke', '9000'),
      ( 'Zama', 'Jobert', '16000'),
      ( 'James', 'Stone', '20000'),
      ( 'Martins', 'Duke', '30000')
	  
GO

1.3
SELECT * Lname, Fname
 From Salary_list;





Question 2
2.1
USE SalaryList
GO

--Creating table
CREATE TABLE Salary_list1(
ID  INT IDENTITY   NOT NULL,
Fname VARCHAR(30) NOT NULL,
Lname VARCHAR(30) NOT NULL,
Salary VARCHAR(15) NOT NULL,
Primary key( ID)
)
GO

2.2
USE SalaryList
GO   

INSERT INTO Salary_list1( Fname, Lname, Salary)
VALUES( 'Mandla', 'Nkosi', '12000'),
      ( 'Princewill', 'Goodluck', '28000'),
	  ( 'Angelina', 'Duke', '9000'),
      ( 'Zama', 'Jobert', '16000'),
      ( 'James', 'Stone', '20000'),
      ( 'Blessing', 'Seli_mont', 'NULL'),
	  ( 'Brenda', 'Ti_tus', 'NULL'),
	  ( 'Martins', 'Duke', '30000')
GO

2.3
SELECT * FROM Salary_list1
 WHERE Lname LIKE '_';

2.4
 SELECT * FROM Salary_list1
 WHERE Lname LIKE 'D%';

2.5
 SELECT * FROM Salary_list1
 WHERE Lname LIKE 'K%' AND Salary >=20000;

2.6
 SELECT * FROM Salary_list1
 WHERE Lname LIKE 'G%'
 AND Salary >=20000
 AND <40000;



Question 3

3.1
USE SalaryList
GO


--Creating table
CREATE TABLE Salary_list2(
ID  INT IDENTITY NOT NULL,
Fname VARCHAR(30) NOT NULL,
Lname VARCHAR(30) NOT NULL,
Salary VARCHAR(15) NOT NULL,
Location VARCHAR (50) NOT NULL,
)
GO

3.2
USE SalaryList
GO

INSERT INTO Salary_list2( Fname, Lname, Salary, Location)
VALUES( 'Mandla', 'Nkosi', '12000', 'Midrand '),
      ( 'Princewill', 'Goodluck', '28000', 'Johannesburg'),
	  ( 'Angelina', 'Duke', '9000', 'Pretoria'),
      ( 'Zama', 'Jobert', '16000', 'Durban '),
      ( 'James', 'Stone', '20000', 'Cape Town'),
      ( 'Martins', 'Duke', '30000', 'Port Elizabeth')
GO

3.2
SELECT Fname
FROM Salary_list2
WHERE Salary>=16000;

3.3
SELECT Fname
FROM Salary_list2
WHERE Salary=12000, 28000 OR 30000 ;

3.5
SELECT *
FROM Salary_list2
ORDER BY Lname ;

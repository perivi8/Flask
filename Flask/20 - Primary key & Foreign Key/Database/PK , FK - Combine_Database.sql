create database practice1

use practice1

-- Region Table

create table Region(RegionID int primary key , RegionDescription varchar(50))

select * from Region

-- Territories Table

create table Territories(TerritoryID varchar(20) , TerritoryDescription varchar(50) , RegionID int references Region(RegionID))

select * from Territories



select * from Region
select * from Territories



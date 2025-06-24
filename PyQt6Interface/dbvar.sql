-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 24, 2025 at 04:46 AM
-- Server version: 5.7.24
-- PHP Version: 8.3.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `generaltourdatabase`
--

-- --------------------------------------------------------

--
-- Table structure for table `carinfo`
--

CREATE TABLE `carinfo` (
  `CarID` int(11) NOT NULL,
  `CarBrand` varchar(60) NOT NULL,
  `CarNumber` varchar(60) NOT NULL,
  `CarColor` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `carinfo`
--

INSERT INTO `carinfo` (`CarID`, `CarBrand`, `CarNumber`, `CarColor`) VALUES
(1, 'MecredesTEST', 'РУ923', 'RedTEST');

-- --------------------------------------------------------

--
-- Table structure for table `customerinfo`
--

CREATE TABLE `customerinfo` (
  `IdCustomer` int(11) NOT NULL,
  `CustomerName` varchar(60) NOT NULL,
  `CustomerPhone` varchar(70) NOT NULL,
  `CustomerPassport` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `customerinfo`
--

INSERT INTO `customerinfo` (`IdCustomer`, `CustomerName`, `CustomerPhone`, `CustomerPassport`) VALUES
(1, 'CustomerTestName', '+79257538412', '4620 922724');

-- --------------------------------------------------------

--
-- Table structure for table `drivertransferinfo`
--

CREATE TABLE `drivertransferinfo` (
  `idDriver` int(11) NOT NULL,
  `DriverName` varchar(70) NOT NULL,
  `DriverPhoneNumber` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `drivertransferinfo`
--

INSERT INTO `drivertransferinfo` (`idDriver`, `DriverName`, `DriverPhoneNumber`) VALUES
(1, 'TestName', '89257538412');

-- --------------------------------------------------------

--
-- Table structure for table `orderid`
--

CREATE TABLE `orderid` (
  `Order_Number` int(11) NOT NULL,
  `idOrder` int(11) NOT NULL,
  `customerID` int(11) NOT NULL,
  `Tour_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `orderid`
--

INSERT INTO `orderid` (`Order_Number`, `idOrder`, `customerID`, `Tour_ID`) VALUES
(1, 1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `orderinfo`
--

CREATE TABLE `orderinfo` (
  `OrderID` int(11) NOT NULL,
  `Order_Number_Monthly` bigint(20) NOT NULL,
  `Order_Number_Yearly` bigint(20) NOT NULL,
  `Order_Number_All` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `orderinfo`
--

INSERT INTO `orderinfo` (`OrderID`, `Order_Number_Monthly`, `Order_Number_Yearly`, `Order_Number_All`) VALUES
(1, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `touragent`
--

CREATE TABLE `touragent` (
  `idAgent` int(11) NOT NULL,
  `ToursToPay` bigint(20) NOT NULL,
  `TotalProfit` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `touragent`
--

INSERT INTO `touragent` (`idAgent`, `ToursToPay`, `TotalProfit`) VALUES
(1, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `tourtable`
--

CREATE TABLE `tourtable` (
  `idTour` int(11) NOT NULL,
  `TourName` varchar(60) NOT NULL,
  `Price` varchar(60) NOT NULL,
  `FlyOutDate` date NOT NULL,
  `Touroperator` varchar(60) NOT NULL,
  `Destination_country` varchar(60) NOT NULL,
  `Airport` varchar(60) NOT NULL,
  `FlyInDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tourtable`
--

INSERT INTO `tourtable` (`idTour`, `TourName`, `Price`, `FlyOutDate`, `Touroperator`, `Destination_country`, `Airport`, `FlyInDate`) VALUES
(1, 'Arthurs Spa Hotel By MercureTEST', '1231000', '2022-06-16', 'Arlean', 'RUSSIA', 'SVO', '2029-06-16');

-- --------------------------------------------------------

--
-- Table structure for table `transferinfo`
--

CREATE TABLE `transferinfo` (
  `Transfer_ID` int(11) NOT NULL,
  `tourID` int(11) NOT NULL,
  `driverID` int(11) NOT NULL,
  `CarID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `transferinfo`
--

INSERT INTO `transferinfo` (`Transfer_ID`, `tourID`, `driverID`, `CarID`) VALUES
(1, 1, 1, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `carinfo`
--
ALTER TABLE `carinfo`
  ADD PRIMARY KEY (`CarID`);

--
-- Indexes for table `customerinfo`
--
ALTER TABLE `customerinfo`
  ADD PRIMARY KEY (`IdCustomer`);

--
-- Indexes for table `drivertransferinfo`
--
ALTER TABLE `drivertransferinfo`
  ADD PRIMARY KEY (`idDriver`);

--
-- Indexes for table `orderid`
--
ALTER TABLE `orderid`
  ADD PRIMARY KEY (`Order_Number`),
  ADD UNIQUE KEY `idOrder` (`idOrder`),
  ADD UNIQUE KEY `customerID` (`customerID`),
  ADD UNIQUE KEY `tourID` (`Tour_ID`);

--
-- Indexes for table `orderinfo`
--
ALTER TABLE `orderinfo`
  ADD PRIMARY KEY (`OrderID`);

--
-- Indexes for table `touragent`
--
ALTER TABLE `touragent`
  ADD PRIMARY KEY (`idAgent`);

--
-- Indexes for table `tourtable`
--
ALTER TABLE `tourtable`
  ADD PRIMARY KEY (`idTour`);

--
-- Indexes for table `transferinfo`
--
ALTER TABLE `transferinfo`
  ADD PRIMARY KEY (`Transfer_ID`),
  ADD UNIQUE KEY `tourID` (`tourID`),
  ADD UNIQUE KEY `driverID` (`driverID`),
  ADD UNIQUE KEY `CarID` (`CarID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `carinfo`
--
ALTER TABLE `carinfo`
  MODIFY `CarID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `customerinfo`
--
ALTER TABLE `customerinfo`
  MODIFY `IdCustomer` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `drivertransferinfo`
--
ALTER TABLE `drivertransferinfo`
  MODIFY `idDriver` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `orderid`
--
ALTER TABLE `orderid`
  MODIFY `Order_Number` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `orderinfo`
--
ALTER TABLE `orderinfo`
  MODIFY `OrderID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `touragent`
--
ALTER TABLE `touragent`
  MODIFY `idAgent` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tourtable`
--
ALTER TABLE `tourtable`
  MODIFY `idTour` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `transferinfo`
--
ALTER TABLE `transferinfo`
  MODIFY `Transfer_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `orderid`
--
ALTER TABLE `orderid`
  ADD CONSTRAINT `orderid_ibfk_1` FOREIGN KEY (`idOrder`) REFERENCES `orderinfo` (`OrderID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `orderid_ibfk_2` FOREIGN KEY (`customerID`) REFERENCES `customerinfo` (`IdCustomer`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `orderid_ibfk_3` FOREIGN KEY (`Tour_ID`) REFERENCES `tourtable` (`idTour`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `transferinfo`
--
ALTER TABLE `transferinfo`
  ADD CONSTRAINT `transferinfo_ibfk_1` FOREIGN KEY (`tourID`) REFERENCES `tourtable` (`idTour`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `transferinfo_ibfk_2` FOREIGN KEY (`driverID`) REFERENCES `drivertransferinfo` (`idDriver`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `transferinfo_ibfk_3` FOREIGN KEY (`CarID`) REFERENCES `carinfo` (`CarID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
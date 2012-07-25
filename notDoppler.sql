-- phpMyAdmin SQL Dump
-- version 3.5.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jul 25, 2012 at 04:34 PM
-- Server version: 5.1.63-0ubuntu0.11.10.1
-- PHP Version: 5.4.4-1~oneiric+1

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `online_games`
--

-- --------------------------------------------------------

--
-- Table structure for table `notDoppler`
--

CREATE TABLE IF NOT EXISTS `notDoppler` (
  `game_id` int(11) NOT NULL AUTO_INCREMENT,
  `game_name` varchar(255) NOT NULL,
  `game_type` varchar(20) NOT NULL,
  `game_thumb` varchar(255) NOT NULL,
  `game_link` varchar(255) NOT NULL,
  PRIMARY KEY (`game_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `notDoppler`
--

INSERT INTO `notDoppler` (`game_id`, `game_name`, `game_type`, `game_thumb`, `game_link`) VALUES
(1, 'asdf', 'asdf', 'asdf', 'asdf'),
(2, 'asdf', 'asdf', 'asdf', 'asdf');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

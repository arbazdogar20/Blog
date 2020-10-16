-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 16, 2020 at 08:56 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `amtechgamer`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sn` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(40) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `message` varchar(500) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sn`, `name`, `email`, `phone`, `message`, `date`) VALUES
(24, 'Ahmad', 'ahmad@gmail.com', '030000000', 'Please Add New Feature In This Blog.', '2020-10-16 23:54:29');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sn` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `sub_title` varchar(100) NOT NULL,
  `slug` varchar(40) NOT NULL,
  `content` varchar(1000) NOT NULL,
  `img_file` varchar(20) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sn`, `title`, `sub_title`, `slug`, `content`, `img_file`, `date`) VALUES
(1, 'New iPhone 12', 'release date, price, specs and leaks', 'post-iphone12', 'Iphone 12 Good Ho geya Gee chaa Gaye Ho. Nai Yar Android Ka Apna Maza ha.', 'post-bg.jpg', '2020-10-15 12:47:05'),
(2, 'Iphone 11 Pro Max', 'Specs, Price, Design', 'post-iphone11-pro-max', 'iPhone 11 Pro and iPhone 11 Pro Max embody Apple’s continuing environmental progress. They are desig', 'about-bg.jpg', '2020-10-13 02:07:27'),
(3, 'Project I.G.I', 'Very Popular Game', 'post-project-igi', 'Project I.G.I. (released in North America as Project I.G.I.: I\'m Going In) is a tactical first-person shooter video game developed by Innerloop Studios and released in December 2000 by Eidos Interactive.[1] Upon release the game received mixed reviews due to a number of shortcomings including poorly programmed A.I., lack of a mid-game save option, and the lack of multiplayer features. However it was praised for its sound design and graphics, thanks in part to its use of a proprietary game engine that was previously used in Innerloop\'s Joint Strike Fighter.\r\n\r\nIt was followed up in 2003 by I.G.I.-2: Covert Strike.\r\n\r\nA prequel titled I.G.I.: Origins was announced by publisher Toadman Interactive in 2019 and will be released in 2021', '', '2020-10-15 11:01:24'),
(5, 'Iphone X', 'Specs, Price, Detail', 'post-iphone-x', 'This Is Very Acha Phone.', '1.jpg', '2020-10-16 00:02:31');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sn`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sn`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sn` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sn` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

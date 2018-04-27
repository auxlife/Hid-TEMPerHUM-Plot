--
-- Table structure for table `readings`
--

CREATE TABLE `readings` (
  `ID` int(11) NOT NULL,
  `datetime` datetime NOT NULL,
  `temp` float NOT NULL,
  `hum` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `readings`
--
ALTER TABLE `readings`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `datetime` (`datetime`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `readings`
--
ALTER TABLE `readings`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

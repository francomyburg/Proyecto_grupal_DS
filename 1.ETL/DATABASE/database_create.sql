DROP DATABASE IF EXISTS `dw_taxis`;
CREATE DATABASE IF NOT EXISTS `dw_taxis`;
USE `dw_taxis`;

DROP TABLE IF EXISTS `borough`;
CREATE TABLE IF NOT EXISTS `borough` (
    `id_borough` INT NOT NULL PRIMARY KEY,
    `borough_name` VARCHAR(15)
);

DROP TABLE IF EXISTS `air_pollution`;
CREATE TABLE IF NOT EXISTS `air_pollution` (
    `fecha` DATETIME,
    `id_cd` INT NOT NULL,
    `cd_name` VARCHAR(30),
    `id_borough` INT NOT NULL PRIMARY KEY,
    `borough_name` VARCHAR(15),
    `polluting_agent` VARCHAR(5),
    `data_value` FLOAT,
    FOREIGN KEY (id_borough)
    REFERENCES borough (id_borough)
);
  
DROP TABLE IF EXISTS `vehicular_volume`;
CREATE TABLE IF NOT EXISTS `vehicular_volume` (
    `fecha` DATETIME,
    `id_borough` INT NOT NULL PRIMARY KEY,
    `borough_name` VARCHAR(15),
    `volume` FLOAT,
    FOREIGN KEY (id_borough)
    REFERENCES borough (id_borough)
);

DROP TABLE IF EXISTS `noise_pollution`;
CREATE TABLE IF NOT EXISTS `noise_pollution` (
    `id_borough` INT NOT NULL PRIMARY KEY,
    `borough_name` VARCHAR(15),
    `year` int,
    `week` int,
    `day` int,
    `hour` int,
    `engine_sounds` int,
    `alarm_sounds` int,
    FOREIGN KEY (id_borough)
    REFERENCES borough (id_borough)
);

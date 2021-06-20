-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema bitcoin
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema bitcoin
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bitcoin` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `bitcoin` ;

-- -----------------------------------------------------
-- Table `bitcoin`.`bitcoinshist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bitcoin`.`bitcoinshist` (
  `fecha` DATE NULL DEFAULT NULL,
  `euro` INT NULL DEFAULT NULL,
  `Id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`Id`))
ENGINE = InnoDB
AUTO_INCREMENT = 190
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bitcoin`.`cryptomarker`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bitcoin`.`cryptomarker` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `compra` INT NULL DEFAULT NULL,
  `venta` INT NULL DEFAULT NULL,
  `ultPrecio` INT NULL DEFAULT NULL,
  `fecha` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`Id`))
ENGINE = InnoDB
AUTO_INCREMENT = 17
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bitcoin`.`datosfinales`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bitcoin`.`datosfinales` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `puntuaciontrain` INT NULL DEFAULT NULL,
  `puntuaciontest` INT NULL DEFAULT NULL,
  `pronostico` INT NULL DEFAULT NULL,
  `fecha` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`Id`))
ENGINE = InnoDB
AUTO_INCREMENT = 14
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

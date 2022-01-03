-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`pallet`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`pallet` (
  `idpallet` INT NOT NULL,
  `descricao_pallet` VARCHAR(45) NOT NULL,
  `quantidade_pallet` INT NOT NULL,
  PRIMARY KEY (`idpallet`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`tecnico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`tecnico` (
  `idtecnico` INT NOT NULL AUTO_INCREMENT,
  `nome_tecnico` VARCHAR(45) NOT NULL,
  `cpf_tecnico` VARCHAR(45) NOT NULL,
  `matricula_tecnico` INT NOT NULL,
  PRIMARY KEY (`idtecnico`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`cliente` (
  `idcliente` INT NOT NULL AUTO_INCREMENT,
  `nome_cliente` VARCHAR(70) NOT NULL,
  `cpf_cliente` INT NOT NULL,
  `rg_cliente` INT NOT NULL,
  PRIMARY KEY (`idcliente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`movimentacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`movimentacao` (
  `idmovimentacao` INT NOT NULL AUTO_INCREMENT,
  `data_hora_movimento` DATETIME(1) NOT NULL,
  `tipo_movimento` VARCHAR(45) NOT NULL,
  `tecnico_idtecnico` INT NOT NULL,
  `cliente_idcliente` INT NOT NULL,
  PRIMARY KEY (`idmovimentacao`),
  INDEX `fk_movimentacao_tecnico1_idx` (`tecnico_idtecnico` ASC) VISIBLE,
  INDEX `fk_movimentacao_cliente1_idx` (`cliente_idcliente` ASC) VISIBLE,
  CONSTRAINT `fk_movimentacao_tecnico1`
    FOREIGN KEY (`tecnico_idtecnico`)
    REFERENCES `mydb`.`tecnico` (`idtecnico`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_movimentacao_cliente1`
    FOREIGN KEY (`cliente_idcliente`)
    REFERENCES `mydb`.`cliente` (`idcliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`itens`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`itens` (
  `iditens` INT NOT NULL AUTO_INCREMENT,
  `quantidade_itens` INT NOT NULL,
  `pallet_idpallet` INT NOT NULL,
  `movimentacao_idmovimentacao` INT NOT NULL,
  PRIMARY KEY (`iditens`),
  INDEX `fk_itens_pallet1_idx` (`pallet_idpallet` ASC) VISIBLE,
  INDEX `fk_itens_movimentacao1_idx` (`movimentacao_idmovimentacao` ASC) VISIBLE,
  CONSTRAINT `fk_itens_pallet1`
    FOREIGN KEY (`pallet_idpallet`)
    REFERENCES `mydb`.`pallet` (`idpallet`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_itens_movimentacao1`
    FOREIGN KEY (`movimentacao_idmovimentacao`)
    REFERENCES `mydb`.`movimentacao` (`idmovimentacao`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

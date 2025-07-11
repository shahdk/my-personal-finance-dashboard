-- Personal Finance Dashboard Database Schema

-- Create database (run this separately if needed)
-- CREATE DATABASE personal_finance;

-- Connect to the database and create tables

----------------------------------------------------------
-- Income
----------------------------------------------------------
DROP TABLE IF EXISTS income;

CREATE TABLE IF NOT EXISTS income (
    source VARCHAR(255) NOT NULL,
    source_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    category VARCHAR(255) NOT NULL,
    updated_at TIMESTAMP DEFAULT NOW() NOT NULL,
    PRIMARY KEY (source, source_date)
);

-- Creating indexes
CREATE INDEX IF NOT EXISTS idx_income_category ON income (category);
CREATE INDEX IF NOT EXISTS idx_income_updated_at ON income (updated_at);
CREATE INDEX IF NOT EXISTS idx_income_amount ON income (amount);

----------------------------------------------------------
-- Expense
----------------------------------------------------------
DROP TABLE IF EXISTS expense;

CREATE TABLE IF NOT EXISTS expense (
  source VARCHAR(255) NOT NULL,
  source_date DATE NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  category VARCHAR(255) NOT NULL,
  updated_at TIMESTAMP DEFAULT NOW() NOT NULL,
  PRIMARY KEY (source, source_date)
);

-- Creating indexes
CREATE INDEX IF NOT EXISTS idx_expense_category ON expense (category);
CREATE INDEX IF NOT EXISTS idx_expense_updated_at ON expense (updated_at);
CREATE INDEX IF NOT EXISTS idx_expense_amount ON expense (amount);

----------------------------------------------------------
-- Vacation
----------------------------------------------------------
DROP TABLE IF EXISTS vacation;

CREATE TABLE IF NOT EXISTS vacation (
    iso_code VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    city varchar(255) NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    updated_at TIMESTAMP DEFAULT NOW() NOT NULL,
    PRIMARY KEY (iso_code, start_date, end_date, city)
);

-- Creating indexes
CREATE INDEX IF NOT EXISTS idx_vacation_updated_at ON vacation (updated_at);
CREATE INDEX IF NOT EXISTS idx_vacation_amount ON vacation (amount);
CREATE INDEX IF NOT EXISTS idx_vacation_lat_long ON vacation (latitude, longitude);


----------------------------------------------------------
-- Net Worth
----------------------------------------------------------
DROP TABLE IF EXISTS net_worth;

CREATE TABLE IF NOT EXISTS net_worth (
  source VARCHAR(255) NOT NULL,
  source_date DATE NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  category VARCHAR(255) NOT NULL,
  updated_at TIMESTAMP DEFAULT NOW() NOT NULL,
  PRIMARY KEY (source, source_date)
);

-- Creating indexes
CREATE INDEX IF NOT EXISTS idx_net_worth_category ON net_worth (category);
CREATE INDEX IF NOT EXISTS idx_net_worth_updated_at ON net_worth (updated_at);
CREATE INDEX IF NOT EXISTS idx_net_worth_amount ON net_worth (amount);


----------------------------------------------------------
-- Accounts
----------------------------------------------------------
DROP TABLE IF EXISTS account_info;

CREATE TABLE IF NOT EXISTS account_info (
    source VARCHAR(255) PRIMARY KEY,
    description VARCHAR,
    updated_at TIMESTAMP DEFAULT NOW() NOT NULL
);

-- Creating indexes
CREATE INDEX IF NOT EXISTS idx_account_info_description ON account_info (description);
CREATE INDEX IF NOT EXISTS idx_account_info_updated_at ON account_info (updated_at);

-- Create full-text search index for account_info
CREATE INDEX IF NOT EXISTS idx_account_info_search 
ON account_info USING gin(to_tsvector('english', source || ' ' || description));
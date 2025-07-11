
-- Inserting entries for January 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2025-01-01', 2200, 'taxes'),
('federal_income_tax_person2', '2025-01-01', 1100, 'taxes'),
('state_income_tax_person1', '2025-01-01', 650, 'taxes'),
('state_income_tax_person2', '2025-01-01', 320, 'taxes'),
('medicare_person1', '2025-01-01', 100, 'taxes'),
('medicare_person2', '2025-01-01', 30, 'taxes'),
('social_security_person1', '2025-01-01', 500, 'taxes'),
('social_security_person2', '2025-01-01', 200, 'taxes'),
-- Needs
('mortgage', '2025-01-01', 2000, 'needs'),
('hoa', '2025-01-01', 500, 'needs'),
('car_insurance', '2025-01-01', 100, 'needs'),
('car_registration', '2025-01-01', 0, 'needs'),
('health_insurance', '2025-01-01', 350, 'needs'),
('phone_bill', '2025-01-01', 200, 'needs'),
('internet_bill', '2025-01-01', 100, 'needs'),
('electricity_bill', '2025-01-01', 150, 'needs'),
('gas_bill', '2025-01-01', 100, 'needs'),
('trash_bill', '2025-01-01', 60, 'needs'),
('water_bill', '2025-01-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2025-01-01', 5, 'wants'),
('netflix_subscription', '2025-01-01', 16, 'wants'),
('prime_subscription', '2025-01-01', 15, 'wants'),
('credit_card1', '2025-01-01', 720, 'wants'),
('credit_card2', '2025-01-01', 350, 'wants'),
('car_payment', '2025-01-01', 200, 'wants'),
-- Investments
('401k_person1', '2025-01-01', 2000, 'investments'),
('401k_person2', '2025-01-01', 2000, 'investments'),
('edu_529', '2025-01-01', 625, 'investments'),
('HSA', '2025-01-01', 525, 'investments'),
('stocks', '2025-01-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for February 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2025-02-01', 2200, 'taxes'),
('federal_income_tax_person2', '2025-02-01', 1100, 'taxes'),
('state_income_tax_person1', '2025-02-01', 650, 'taxes'),
('state_income_tax_person2', '2025-02-01', 320, 'taxes'),
('medicare_person1', '2025-02-01', 100, 'taxes'),
('medicare_person2', '2025-02-01', 30, 'taxes'),
('social_security_person1', '2025-02-01', 500, 'taxes'),
('social_security_person2', '2025-02-01', 200, 'taxes'),
-- Needs
('mortgage', '2025-02-01', 2000, 'needs'),
('hoa', '2025-02-01', 500, 'needs'),
('car_insurance', '2025-02-01', 100, 'needs'),
('car_registration', '2025-02-01', 0, 'needs'),
('health_insurance', '2025-02-01', 350, 'needs'),
('phone_bill', '2025-02-01', 200, 'needs'),
('internet_bill', '2025-02-01', 100, 'needs'),
('electricity_bill', '2025-02-01', 150, 'needs'),
('gas_bill', '2025-02-01', 100, 'needs'),
('trash_bill', '2025-02-01', 60, 'needs'),
('water_bill', '2025-02-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2025-02-01', 5, 'wants'),
('netflix_subscription', '2025-02-01', 16, 'wants'),
('prime_subscription', '2025-02-01', 15, 'wants'),
('credit_card1', '2025-02-01', 720, 'wants'),
('credit_card2', '2025-02-01', 350, 'wants'),
('car_payment', '2025-02-01', 200, 'wants'),
-- Investments
('401k_person1', '2025-02-01', 2000, 'investments'),
('401k_person2', '2025-02-01', 2000, 'investments'),
('edu_529', '2025-02-01', 625, 'investments'),
('HSA', '2025-02-01', 525, 'investments'),
('stocks', '2025-02-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for March 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2025-03-01', 2200, 'taxes'),
('federal_income_tax_person2', '2025-03-01', 1100, 'taxes'),
('state_income_tax_person1', '2025-03-01', 650, 'taxes'),
('state_income_tax_person2', '2025-03-01', 320, 'taxes'),
('medicare_person1', '2025-03-01', 100, 'taxes'),
('medicare_person2', '2025-03-01', 30, 'taxes'),
('social_security_person1', '2025-03-01', 500, 'taxes'),
('social_security_person2', '2025-03-01', 200, 'taxes'),
-- Needs
('mortgage', '2025-03-01', 2000, 'needs'),
('hoa', '2025-03-01', 500, 'needs'),
('car_insurance', '2025-03-01', 100, 'needs'),
('car_registration', '2025-03-01', 0, 'needs'),
('health_insurance', '2025-03-01', 350, 'needs'),
('phone_bill', '2025-03-01', 200, 'needs'),
('internet_bill', '2025-03-01', 100, 'needs'),
('electricity_bill', '2025-03-01', 150, 'needs'),
('gas_bill', '2025-03-01', 100, 'needs'),
('trash_bill', '2025-03-01', 60, 'needs'),
('water_bill', '2025-03-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2025-03-01', 5, 'wants'),
('netflix_subscription', '2025-03-01', 16, 'wants'),
('prime_subscription', '2025-03-01', 15, 'wants'),
('credit_card1', '2025-03-01', 720, 'wants'),
('credit_card2', '2025-03-01', 350, 'wants'),
('car_payment', '2025-03-01', 200, 'wants'),
-- Investments
('401k_person1', '2025-03-01', 2000, 'investments'),
('401k_person2', '2025-03-01', 2000, 'investments'),
('edu_529', '2025-03-01', 625, 'investments'),
('HSA', '2025-03-01', 525, 'investments'),
('stocks', '2025-03-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for April 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2025-04-01', 2200, 'taxes'),
('federal_income_tax_person2', '2025-04-01', 1100, 'taxes'),
('state_income_tax_person1', '2025-04-01', 650, 'taxes'),
('state_income_tax_person2', '2025-04-01', 320, 'taxes'),
('medicare_person1', '2025-04-01', 100, 'taxes'),
('medicare_person2', '2025-04-01', 30, 'taxes'),
('social_security_person1', '2025-04-01', 500, 'taxes'),
('social_security_person2', '2025-04-01', 200, 'taxes'),
-- Needs
('mortgage', '2025-04-01', 2000, 'needs'),
('hoa', '2025-04-01', 500, 'needs'),
('car_insurance', '2025-04-01', 100, 'needs'),
('car_registration', '2025-04-01', 0, 'needs'),
('health_insurance', '2025-04-01', 350, 'needs'),
('phone_bill', '2025-04-01', 200, 'needs'),
('internet_bill', '2025-04-01', 100, 'needs'),
('electricity_bill', '2025-04-01', 150, 'needs'),
('gas_bill', '2025-04-01', 100, 'needs'),
('trash_bill', '2025-04-01', 60, 'needs'),
('water_bill', '2025-04-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2025-04-01', 5, 'wants'),
('netflix_subscription', '2025-04-01', 16, 'wants'),
('prime_subscription', '2025-04-01', 15, 'wants'),
('credit_card1', '2025-04-01', 720, 'wants'),
('credit_card2', '2025-04-01', 350, 'wants'),
('car_payment', '2025-04-01', 200, 'wants'),
-- Investments
('401k_person1', '2025-04-01', 2000, 'investments'),
('401k_person2', '2025-04-01', 2000, 'investments'),
('edu_529', '2025-04-01', 625, 'investments'),
('HSA', '2025-04-01', 525, 'investments'),
('stocks', '2025-04-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for May 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2025-05-01', 2200, 'taxes'),
('federal_income_tax_person2', '2025-05-01', 1100, 'taxes'),
('state_income_tax_person1', '2025-05-01', 650, 'taxes'),
('state_income_tax_person2', '2025-05-01', 320, 'taxes'),
('medicare_person1', '2025-05-01', 100, 'taxes'),
('medicare_person2', '2025-05-01', 30, 'taxes'),
('social_security_person1', '2025-05-01', 500, 'taxes'),
('social_security_person2', '2025-05-01', 200, 'taxes'),
-- Needs
('mortgage', '2025-05-01', 2000, 'needs'),
('hoa', '2025-05-01', 500, 'needs'),
('car_insurance', '2025-05-01', 100, 'needs'),
('car_registration', '2025-05-01', 0, 'needs'),
('health_insurance', '2025-05-01', 350, 'needs'),
('phone_bill', '2025-05-01', 200, 'needs'),
('internet_bill', '2025-05-01', 100, 'needs'),
('electricity_bill', '2025-05-01', 150, 'needs'),
('gas_bill', '2025-05-01', 100, 'needs'),
('trash_bill', '2025-05-01', 60, 'needs'),
('water_bill', '2025-05-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2025-05-01', 5, 'wants'),
('netflix_subscription', '2025-05-01', 16, 'wants'),
('prime_subscription', '2025-05-01', 15, 'wants'),
('credit_card1', '2025-05-01', 720, 'wants'),
('credit_card2', '2025-05-01', 350, 'wants'),
('car_payment', '2025-05-01', 200, 'wants'),
-- Investments
('401k_person1', '2025-05-01', 2000, 'investments'),
('401k_person2', '2025-05-01', 2000, 'investments'),
('edu_529', '2025-05-01', 625, 'investments'),
('HSA', '2025-05-01', 525, 'investments'),
('stocks', '2025-05-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for June 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2025-06-01', 2200, 'taxes'),
('federal_income_tax_person2', '2025-06-01', 1100, 'taxes'),
('state_income_tax_person1', '2025-06-01', 650, 'taxes'),
('state_income_tax_person2', '2025-06-01', 320, 'taxes'),
('medicare_person1', '2025-06-01', 100, 'taxes'),
('medicare_person2', '2025-06-01', 30, 'taxes'),
('social_security_person1', '2025-06-01', 500, 'taxes'),
('social_security_person2', '2025-06-01', 200, 'taxes'),
-- Needs
('mortgage', '2025-06-01', 2000, 'needs'),
('hoa', '2025-06-01', 500, 'needs'),
('car_insurance', '2025-06-01', 100, 'needs'),
('car_registration', '2025-06-01', 0, 'needs'),
('health_insurance', '2025-06-01', 350, 'needs'),
('phone_bill', '2025-06-01', 200, 'needs'),
('internet_bill', '2025-06-01', 100, 'needs'),
('electricity_bill', '2025-06-01', 150, 'needs'),
('gas_bill', '2025-06-01', 100, 'needs'),
('trash_bill', '2025-06-01', 60, 'needs'),
('water_bill', '2025-06-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2025-06-01', 5, 'wants'),
('netflix_subscription', '2025-06-01', 16, 'wants'),
('prime_subscription', '2025-06-01', 15, 'wants'),
('credit_card1', '2025-06-01', 720, 'wants'),
('credit_card2', '2025-06-01', 350, 'wants'),
('car_payment', '2025-06-01', 200, 'wants'),
-- Investments
('401k_person1', '2025-06-01', 2000, 'investments'),
('401k_person2', '2025-06-01', 2000, 'investments'),
('edu_529', '2025-06-01', 625, 'investments'),
('HSA', '2025-06-01', 525, 'investments'),
('stocks', '2025-06-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for July 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2025-07-01', 2200, 'taxes'),
('federal_income_tax_person2', '2025-07-01', 1100, 'taxes'),
('state_income_tax_person1', '2025-07-01', 650, 'taxes'),
('state_income_tax_person2', '2025-07-01', 320, 'taxes'),
('medicare_person1', '2025-07-01', 100, 'taxes'),
('medicare_person2', '2025-07-01', 30, 'taxes'),
('social_security_person1', '2025-07-01', 500, 'taxes'),
('social_security_person2', '2025-07-01', 200, 'taxes'),
-- Needs
('mortgage', '2025-07-01', 2000, 'needs'),
('hoa', '2025-07-01', 500, 'needs'),
('car_insurance', '2025-07-01', 100, 'needs'),
('car_registration', '2025-07-01', 0, 'needs'),
('health_insurance', '2025-07-01', 350, 'needs'),
('phone_bill', '2025-07-01', 200, 'needs'),
('internet_bill', '2025-07-01', 100, 'needs'),
('electricity_bill', '2025-07-01', 150, 'needs'),
('gas_bill', '2025-07-01', 100, 'needs'),
('trash_bill', '2025-07-01', 60, 'needs'),
('water_bill', '2025-07-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2025-07-01', 5, 'wants'),
('netflix_subscription', '2025-07-01', 16, 'wants'),
('prime_subscription', '2025-07-01', 15, 'wants'),
('credit_card1', '2025-07-01', 720, 'wants'),
('credit_card2', '2025-07-01', 350, 'wants'),
('car_payment', '2025-07-01', 200, 'wants'),
-- Investments
('401k_person1', '2025-07-01', 2000, 'investments'),
('401k_person2', '2025-07-01', 2000, 'investments'),
('edu_529', '2025-07-01', 625, 'investments'),
('HSA', '2025-07-01', 525, 'investments'),
('stocks', '2025-07-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for August 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2025-08-01', 2200, 'taxes'),
('federal_income_tax_person2', '2025-08-01', 1100, 'taxes'),
('state_income_tax_person1', '2025-08-01', 650, 'taxes'),
('state_income_tax_person2', '2025-08-01', 320, 'taxes'),
('medicare_person1', '2025-08-01', 100, 'taxes'),
('medicare_person2', '2025-08-01', 30, 'taxes'),
('social_security_person1', '2025-08-01', 500, 'taxes'),
('social_security_person2', '2025-08-01', 200, 'taxes'),
-- Needs
('mortgage', '2025-08-01', 2000, 'needs'),
('hoa', '2025-08-01', 500, 'needs'),
('car_insurance', '2025-08-01', 100, 'needs'),
('car_registration', '2025-08-01', 0, 'needs'),
('health_insurance', '2025-08-01', 350, 'needs'),
('phone_bill', '2025-08-01', 200, 'needs'),
('internet_bill', '2025-08-01', 100, 'needs'),
('electricity_bill', '2025-08-01', 150, 'needs'),
('gas_bill', '2025-08-01', 100, 'needs'),
('trash_bill', '2025-08-01', 60, 'needs'),
('water_bill', '2025-08-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2025-08-01', 5, 'wants'),
('netflix_subscription', '2025-08-01', 16, 'wants'),
('prime_subscription', '2025-08-01', 15, 'wants'),
('credit_card1', '2025-08-01', 720, 'wants'),
('credit_card2', '2025-08-01', 350, 'wants'),
('car_payment', '2025-08-01', 200, 'wants'),
-- Investments
('401k_person1', '2025-08-01', 2000, 'investments'),
('401k_person2', '2025-08-01', 2000, 'investments'),
('edu_529', '2025-08-01', 625, 'investments'),
('HSA', '2025-08-01', 525, 'investments'),
('stocks', '2025-08-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for September 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2025-09-01', 2200, 'taxes'),
('federal_income_tax_person2', '2025-09-01', 1100, 'taxes'),
('state_income_tax_person1', '2025-09-01', 650, 'taxes'),
('state_income_tax_person2', '2025-09-01', 320, 'taxes'),
('medicare_person1', '2025-09-01', 100, 'taxes'),
('medicare_person2', '2025-09-01', 30, 'taxes'),
('social_security_person1', '2025-09-01', 500, 'taxes'),
('social_security_person2', '2025-09-01', 200, 'taxes'),
-- Needs
('mortgage', '2025-09-01', 2000, 'needs'),
('hoa', '2025-09-01', 500, 'needs'),
('car_insurance', '2025-09-01', 100, 'needs'),
('car_registration', '2025-09-01', 0, 'needs'),
('health_insurance', '2025-09-01', 350, 'needs'),
('phone_bill', '2025-09-01', 200, 'needs'),
('internet_bill', '2025-09-01', 100, 'needs'),
('electricity_bill', '2025-09-01', 150, 'needs'),
('gas_bill', '2025-09-01', 100, 'needs'),
('trash_bill', '2025-09-01', 60, 'needs'),
('water_bill', '2025-09-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2025-09-01', 5, 'wants'),
('netflix_subscription', '2025-09-01', 16, 'wants'),
('prime_subscription', '2025-09-01', 15, 'wants'),
('credit_card1', '2025-09-01', 720, 'wants'),
('credit_card2', '2025-09-01', 350, 'wants'),
('car_payment', '2025-09-01', 200, 'wants'),
-- Investments
('401k_person1', '2025-09-01', 2000, 'investments'),
('401k_person2', '2025-09-01', 2000, 'investments'),
('edu_529', '2025-09-01', 625, 'investments'),
('HSA', '2025-09-01', 525, 'investments'),
('stocks', '2025-09-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for October 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2025-10-01', 2200, 'taxes'),
('federal_income_tax_person2', '2025-10-01', 1100, 'taxes'),
('state_income_tax_person1', '2025-10-01', 650, 'taxes'),
('state_income_tax_person2', '2025-10-01', 320, 'taxes'),
('medicare_person1', '2025-10-01', 100, 'taxes'),
('medicare_person2', '2025-10-01', 30, 'taxes'),
('social_security_person1', '2025-10-01', 500, 'taxes'),
('social_security_person2', '2025-10-01', 200, 'taxes'),
-- Needs
('mortgage', '2025-10-01', 2000, 'needs'),
('hoa', '2025-10-01', 500, 'needs'),
('car_insurance', '2025-10-01', 100, 'needs'),
('car_registration', '2025-10-01', 0, 'needs'),
('health_insurance', '2025-10-01', 350, 'needs'),
('phone_bill', '2025-10-01', 200, 'needs'),
('internet_bill', '2025-10-01', 100, 'needs'),
('electricity_bill', '2025-10-01', 150, 'needs'),
('gas_bill', '2025-10-01', 100, 'needs'),
('trash_bill', '2025-10-01', 60, 'needs'),
('water_bill', '2025-10-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2025-10-01', 5, 'wants'),
('netflix_subscription', '2025-10-01', 16, 'wants'),
('prime_subscription', '2025-10-01', 15, 'wants'),
('credit_card1', '2025-10-01', 720, 'wants'),
('credit_card2', '2025-10-01', 350, 'wants'),
('car_payment', '2025-10-01', 200, 'wants'),
-- Investments
('401k_person1', '2025-10-01', 2000, 'investments'),
('401k_person2', '2025-10-01', 2000, 'investments'),
('edu_529', '2025-10-01', 625, 'investments'),
('HSA', '2025-10-01', 525, 'investments'),
('stocks', '2025-10-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for November 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2025-11-01', 2200, 'taxes'),
('federal_income_tax_person2', '2025-11-01', 1100, 'taxes'),
('state_income_tax_person1', '2025-11-01', 650, 'taxes'),
('state_income_tax_person2', '2025-11-01', 320, 'taxes'),
('medicare_person1', '2025-11-01', 100, 'taxes'),
('medicare_person2', '2025-11-01', 30, 'taxes'),
('social_security_person1', '2025-11-01', 500, 'taxes'),
('social_security_person2', '2025-11-01', 200, 'taxes'),
-- Needs
('mortgage', '2025-11-01', 2000, 'needs'),
('hoa', '2025-11-01', 500, 'needs'),
('car_insurance', '2025-11-01', 100, 'needs'),
('car_registration', '2025-11-01', 0, 'needs'),
('health_insurance', '2025-11-01', 350, 'needs'),
('phone_bill', '2025-11-01', 200, 'needs'),
('internet_bill', '2025-11-01', 100, 'needs'),
('electricity_bill', '2025-11-01', 150, 'needs'),
('gas_bill', '2025-11-01', 100, 'needs'),
('trash_bill', '2025-11-01', 60, 'needs'),
('water_bill', '2025-11-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2025-11-01', 5, 'wants'),
('netflix_subscription', '2025-11-01', 16, 'wants'),
('prime_subscription', '2025-11-01', 15, 'wants'),
('credit_card1', '2025-11-01', 720, 'wants'),
('credit_card2', '2025-11-01', 350, 'wants'),
('car_payment', '2025-11-01', 200, 'wants'),
-- Investments
('401k_person1', '2025-11-01', 2000, 'investments'),
('401k_person2', '2025-11-01', 2000, 'investments'),
('edu_529', '2025-11-01', 625, 'investments'),
('HSA', '2025-11-01', 525, 'investments'),
('stocks', '2025-11-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for December 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2025-12-01', 2200, 'taxes'),
('federal_income_tax_person2', '2025-12-01', 1100, 'taxes'),
('state_income_tax_person1', '2025-12-01', 650, 'taxes'),
('state_income_tax_person2', '2025-12-01', 320, 'taxes'),
('medicare_person1', '2025-12-01', 100, 'taxes'),
('medicare_person2', '2025-12-01', 30, 'taxes'),
('social_security_person1', '2025-12-01', 500, 'taxes'),
('social_security_person2', '2025-12-01', 200, 'taxes'),
-- Needs
('mortgage', '2025-12-01', 2000, 'needs'),
('hoa', '2025-12-01', 500, 'needs'),
('car_insurance', '2025-12-01', 100, 'needs'),
('car_registration', '2025-12-01', 0, 'needs'),
('health_insurance', '2025-12-01', 350, 'needs'),
('phone_bill', '2025-12-01', 200, 'needs'),
('internet_bill', '2025-12-01', 100, 'needs'),
('electricity_bill', '2025-12-01', 150, 'needs'),
('gas_bill', '2025-12-01', 100, 'needs'),
('trash_bill', '2025-12-01', 60, 'needs'),
('water_bill', '2025-12-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2025-12-01', 5, 'wants'),
('netflix_subscription', '2025-12-01', 16, 'wants'),
('prime_subscription', '2025-12-01', 15, 'wants'),
('credit_card1', '2025-12-01', 720, 'wants'),
('credit_card2', '2025-12-01', 350, 'wants'),
('car_payment', '2025-12-01', 200, 'wants'),
-- Investments
('401k_person1', '2025-12-01', 2000, 'investments'),
('401k_person2', '2025-12-01', 2000, 'investments'),
('edu_529', '2025-12-01', 625, 'investments'),
('HSA', '2025-12-01', 525, 'investments'),
('stocks', '2025-12-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;




-- Inserting entries for January 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2024-01-01', 2000, 'taxes'),
('federal_income_tax_person2', '2024-01-01', 1000, 'taxes'),
('state_income_tax_person1', '2024-01-01', 600, 'taxes'),
('state_income_tax_person2', '2024-01-01', 300, 'taxes'),
('medicare_person1', '2024-01-01', 100, 'taxes'),
('medicare_person2', '2024-01-01', 30, 'taxes'),
('social_security_person1', '2024-01-01', 500, 'taxes'),
('social_security_person2', '2024-01-01', 200, 'taxes'),
-- Needs
('mortgage', '2024-01-01', 2000, 'needs'),
('hoa', '2024-01-01', 500, 'needs'),
('car_insurance', '2024-01-01', 100, 'needs'),
('car_registration', '2024-01-01', 0, 'needs'),
('health_insurance', '2024-01-01', 350, 'needs'),
('phone_bill', '2024-01-01', 200, 'needs'),
('internet_bill', '2024-01-01', 100, 'needs'),
('electricity_bill', '2024-01-01', 150, 'needs'),
('gas_bill', '2024-01-01', 75, 'needs'),
('trash_bill', '2024-01-01', 60, 'needs'),
('water_bill', '2024-01-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2024-01-01', 5, 'wants'),
('netflix_subscription', '2024-01-01', 16, 'wants'),
('prime_subscription', '2024-01-01', 15, 'wants'),
('credit_card1', '2024-01-01', 700, 'wants'),
('credit_card2', '2024-01-01', 300, 'wants'),
('car_payment', '2024-01-01', 200, 'wants'),
-- Investments
('401k_person1', '2024-01-01', 1960, 'investments'),
('401k_person2', '2024-01-01', 1960, 'investments'),
('edu_529', '2024-01-01', 625, 'investments'),
('HSA', '2024-01-01', 525, 'investments'),
('stocks', '2024-01-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for February 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2024-02-01', 2000, 'taxes'),
('federal_income_tax_person2', '2024-02-01', 1000, 'taxes'),
('state_income_tax_person1', '2024-02-01', 600, 'taxes'),
('state_income_tax_person2', '2024-02-01', 300, 'taxes'),
('medicare_person1', '2024-02-01', 100, 'taxes'),
('medicare_person2', '2024-02-01', 30, 'taxes'),
('social_security_person1', '2024-02-01', 500, 'taxes'),
('social_security_person2', '2024-02-01', 200, 'taxes'),
-- Needs
('mortgage', '2024-02-01', 2000, 'needs'),
('hoa', '2024-02-01', 500, 'needs'),
('car_insurance', '2024-02-01', 100, 'needs'),
('car_registration', '2024-02-01', 0, 'needs'),
('health_insurance', '2024-02-01', 350, 'needs'),
('phone_bill', '2024-02-01', 200, 'needs'),
('internet_bill', '2024-02-01', 100, 'needs'),
('electricity_bill', '2024-02-01', 150, 'needs'),
('gas_bill', '2024-02-01', 75, 'needs'),
('trash_bill', '2024-02-01', 60, 'needs'),
('water_bill', '2024-02-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2024-02-01', 5, 'wants'),
('netflix_subscription', '2024-02-01', 16, 'wants'),
('prime_subscription', '2024-02-01', 15, 'wants'),
('credit_card1', '2024-02-01', 700, 'wants'),
('credit_card2', '2024-02-01', 300, 'wants'),
('car_payment', '2024-02-01', 200, 'wants'),
-- Investments
('401k_person1', '2024-02-01', 1960, 'investments'),
('401k_person2', '2024-02-01', 1960, 'investments'),
('edu_529', '2024-02-01', 625, 'investments'),
('HSA', '2024-02-01', 525, 'investments'),
('stocks', '2024-02-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for March 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2024-03-01', 2000, 'taxes'),
('federal_income_tax_person2', '2024-03-01', 1000, 'taxes'),
('state_income_tax_person1', '2024-03-01', 600, 'taxes'),
('state_income_tax_person2', '2024-03-01', 300, 'taxes'),
('medicare_person1', '2024-03-01', 100, 'taxes'),
('medicare_person2', '2024-03-01', 30, 'taxes'),
('social_security_person1', '2024-03-01', 500, 'taxes'),
('social_security_person2', '2024-03-01', 200, 'taxes'),
-- Needs
('mortgage', '2024-03-01', 2000, 'needs'),
('hoa', '2024-03-01', 500, 'needs'),
('car_insurance', '2024-03-01', 100, 'needs'),
('car_registration', '2024-03-01', 0, 'needs'),
('health_insurance', '2024-03-01', 350, 'needs'),
('phone_bill', '2024-03-01', 200, 'needs'),
('internet_bill', '2024-03-01', 100, 'needs'),
('electricity_bill', '2024-03-01', 150, 'needs'),
('gas_bill', '2024-03-01', 75, 'needs'),
('trash_bill', '2024-03-01', 60, 'needs'),
('water_bill', '2024-03-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2024-03-01', 5, 'wants'),
('netflix_subscription', '2024-03-01', 16, 'wants'),
('prime_subscription', '2024-03-01', 15, 'wants'),
('credit_card1', '2024-03-01', 700, 'wants'),
('credit_card2', '2024-03-01', 300, 'wants'),
('car_payment', '2024-03-01', 200, 'wants'),
-- Investments
('401k_person1', '2024-03-01', 1960, 'investments'),
('401k_person2', '2024-03-01', 1960, 'investments'),
('edu_529', '2024-03-01', 625, 'investments'),
('HSA', '2024-03-01', 525, 'investments'),
('stocks', '2024-03-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for April 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2024-04-01', 2000, 'taxes'),
('federal_income_tax_person2', '2024-04-01', 1000, 'taxes'),
('state_income_tax_person1', '2024-04-01', 600, 'taxes'),
('state_income_tax_person2', '2024-04-01', 300, 'taxes'),
('medicare_person1', '2024-04-01', 100, 'taxes'),
('medicare_person2', '2024-04-01', 30, 'taxes'),
('social_security_person1', '2024-04-01', 500, 'taxes'),
('social_security_person2', '2024-04-01', 200, 'taxes'),
-- Needs
('mortgage', '2024-04-01', 2000, 'needs'),
('hoa', '2024-04-01', 500, 'needs'),
('car_insurance', '2024-04-01', 100, 'needs'),
('car_registration', '2024-04-01', 0, 'needs'),
('health_insurance', '2024-04-01', 350, 'needs'),
('phone_bill', '2024-04-01', 200, 'needs'),
('internet_bill', '2024-04-01', 100, 'needs'),
('electricity_bill', '2024-04-01', 150, 'needs'),
('gas_bill', '2024-04-01', 75, 'needs'),
('trash_bill', '2024-04-01', 60, 'needs'),
('water_bill', '2024-04-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2024-04-01', 5, 'wants'),
('netflix_subscription', '2024-04-01', 16, 'wants'),
('prime_subscription', '2024-04-01', 15, 'wants'),
('credit_card1', '2024-04-01', 700, 'wants'),
('credit_card2', '2024-04-01', 300, 'wants'),
('car_payment', '2024-04-01', 200, 'wants'),
-- Investments
('401k_person1', '2024-04-01', 1960, 'investments'),
('401k_person2', '2024-04-01', 1960, 'investments'),
('edu_529', '2024-04-01', 625, 'investments'),
('HSA', '2024-04-01', 525, 'investments'),
('stocks', '2024-04-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for May 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2024-05-01', 2000, 'taxes'),
('federal_income_tax_person2', '2024-05-01', 1000, 'taxes'),
('state_income_tax_person1', '2024-05-01', 600, 'taxes'),
('state_income_tax_person2', '2024-05-01', 300, 'taxes'),
('medicare_person1', '2024-05-01', 100, 'taxes'),
('medicare_person2', '2024-05-01', 30, 'taxes'),
('social_security_person1', '2024-05-01', 500, 'taxes'),
('social_security_person2', '2024-05-01', 200, 'taxes'),
-- Needs
('mortgage', '2024-05-01', 2000, 'needs'),
('hoa', '2024-05-01', 500, 'needs'),
('car_insurance', '2024-05-01', 100, 'needs'),
('car_registration', '2024-05-01', 0, 'needs'),
('health_insurance', '2024-05-01', 350, 'needs'),
('phone_bill', '2024-05-01', 200, 'needs'),
('internet_bill', '2024-05-01', 100, 'needs'),
('electricity_bill', '2024-05-01', 150, 'needs'),
('gas_bill', '2024-05-01', 75, 'needs'),
('trash_bill', '2024-05-01', 60, 'needs'),
('water_bill', '2024-05-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2024-05-01', 5, 'wants'),
('netflix_subscription', '2024-05-01', 16, 'wants'),
('prime_subscription', '2024-05-01', 15, 'wants'),
('credit_card1', '2024-05-01', 700, 'wants'),
('credit_card2', '2024-05-01', 300, 'wants'),
('car_payment', '2024-05-01', 200, 'wants'),
-- Investments
('401k_person1', '2024-05-01', 1960, 'investments'),
('401k_person2', '2024-05-01', 1960, 'investments'),
('edu_529', '2024-05-01', 625, 'investments'),
('HSA', '2024-05-01', 525, 'investments'),
('stocks', '2024-05-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for June 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2024-06-01', 2000, 'taxes'),
('federal_income_tax_person2', '2024-06-01', 1000, 'taxes'),
('state_income_tax_person1', '2024-06-01', 600, 'taxes'),
('state_income_tax_person2', '2024-06-01', 300, 'taxes'),
('medicare_person1', '2024-06-01', 100, 'taxes'),
('medicare_person2', '2024-06-01', 30, 'taxes'),
('social_security_person1', '2024-06-01', 500, 'taxes'),
('social_security_person2', '2024-06-01', 200, 'taxes'),
-- Needs
('mortgage', '2024-06-01', 2000, 'needs'),
('hoa', '2024-06-01', 500, 'needs'),
('car_insurance', '2024-06-01', 100, 'needs'),
('car_registration', '2024-06-01', 0, 'needs'),
('health_insurance', '2024-06-01', 350, 'needs'),
('phone_bill', '2024-06-01', 200, 'needs'),
('internet_bill', '2024-06-01', 100, 'needs'),
('electricity_bill', '2024-06-01', 150, 'needs'),
('gas_bill', '2024-06-01', 75, 'needs'),
('trash_bill', '2024-06-01', 60, 'needs'),
('water_bill', '2024-06-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2024-06-01', 5, 'wants'),
('netflix_subscription', '2024-06-01', 16, 'wants'),
('prime_subscription', '2024-06-01', 15, 'wants'),
('credit_card1', '2024-06-01', 700, 'wants'),
('credit_card2', '2024-06-01', 300, 'wants'),
('car_payment', '2024-06-01', 200, 'wants'),
-- Investments
('401k_person1', '2024-06-01', 1960, 'investments'),
('401k_person2', '2024-06-01', 1960, 'investments'),
('edu_529', '2024-06-01', 625, 'investments'),
('HSA', '2024-06-01', 525, 'investments'),
('stocks', '2024-06-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for July 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2024-07-01', 2000, 'taxes'),
('federal_income_tax_person2', '2024-07-01', 1000, 'taxes'),
('state_income_tax_person1', '2024-07-01', 600, 'taxes'),
('state_income_tax_person2', '2024-07-01', 300, 'taxes'),
('medicare_person1', '2024-07-01', 100, 'taxes'),
('medicare_person2', '2024-07-01', 30, 'taxes'),
('social_security_person1', '2024-07-01', 500, 'taxes'),
('social_security_person2', '2024-07-01', 200, 'taxes'),
-- Needs
('mortgage', '2024-07-01', 2000, 'needs'),
('hoa', '2024-07-01', 500, 'needs'),
('car_insurance', '2024-07-01', 100, 'needs'),
('car_registration', '2024-07-01', 0, 'needs'),
('health_insurance', '2024-07-01', 350, 'needs'),
('phone_bill', '2024-07-01', 200, 'needs'),
('internet_bill', '2024-07-01', 100, 'needs'),
('electricity_bill', '2024-07-01', 150, 'needs'),
('gas_bill', '2024-07-01', 75, 'needs'),
('trash_bill', '2024-07-01', 60, 'needs'),
('water_bill', '2024-07-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2024-07-01', 5, 'wants'),
('netflix_subscription', '2024-07-01', 16, 'wants'),
('prime_subscription', '2024-07-01', 15, 'wants'),
('credit_card1', '2024-07-01', 700, 'wants'),
('credit_card2', '2024-07-01', 300, 'wants'),
('car_payment', '2024-07-01', 200, 'wants'),
-- Investments
('401k_person1', '2024-07-01', 1960, 'investments'),
('401k_person2', '2024-07-01', 1960, 'investments'),
('edu_529', '2024-07-01', 625, 'investments'),
('HSA', '2024-07-01', 525, 'investments'),
('stocks', '2024-07-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for August 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2024-08-01', 2000, 'taxes'),
('federal_income_tax_person2', '2024-08-01', 1000, 'taxes'),
('state_income_tax_person1', '2024-08-01', 600, 'taxes'),
('state_income_tax_person2', '2024-08-01', 300, 'taxes'),
('medicare_person1', '2024-08-01', 100, 'taxes'),
('medicare_person2', '2024-08-01', 30, 'taxes'),
('social_security_person1', '2024-08-01', 500, 'taxes'),
('social_security_person2', '2024-08-01', 200, 'taxes'),
-- Needs
('mortgage', '2024-08-01', 2000, 'needs'),
('hoa', '2024-08-01', 500, 'needs'),
('car_insurance', '2024-08-01', 100, 'needs'),
('car_registration', '2024-08-01', 0, 'needs'),
('health_insurance', '2024-08-01', 350, 'needs'),
('phone_bill', '2024-08-01', 200, 'needs'),
('internet_bill', '2024-08-01', 100, 'needs'),
('electricity_bill', '2024-08-01', 150, 'needs'),
('gas_bill', '2024-08-01', 75, 'needs'),
('trash_bill', '2024-08-01', 60, 'needs'),
('water_bill', '2024-08-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2024-08-01', 5, 'wants'),
('netflix_subscription', '2024-08-01', 16, 'wants'),
('prime_subscription', '2024-08-01', 15, 'wants'),
('credit_card1', '2024-08-01', 700, 'wants'),
('credit_card2', '2024-08-01', 300, 'wants'),
('car_payment', '2024-08-01', 200, 'wants'),
-- Investments
('401k_person1', '2024-08-01', 1960, 'investments'),
('401k_person2', '2024-08-01', 1960, 'investments'),
('edu_529', '2024-08-01', 625, 'investments'),
('HSA', '2024-08-01', 525, 'investments'),
('stocks', '2024-08-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for September 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2024-09-01', 2000, 'taxes'),
('federal_income_tax_person2', '2024-09-01', 1000, 'taxes'),
('state_income_tax_person1', '2024-09-01', 600, 'taxes'),
('state_income_tax_person2', '2024-09-01', 300, 'taxes'),
('medicare_person1', '2024-09-01', 100, 'taxes'),
('medicare_person2', '2024-09-01', 30, 'taxes'),
('social_security_person1', '2024-09-01', 500, 'taxes'),
('social_security_person2', '2024-09-01', 200, 'taxes'),
-- Needs
('mortgage', '2024-09-01', 2000, 'needs'),
('hoa', '2024-09-01', 500, 'needs'),
('car_insurance', '2024-09-01', 100, 'needs'),
('car_registration', '2024-09-01', 0, 'needs'),
('health_insurance', '2024-09-01', 350, 'needs'),
('phone_bill', '2024-09-01', 200, 'needs'),
('internet_bill', '2024-09-01', 100, 'needs'),
('electricity_bill', '2024-09-01', 150, 'needs'),
('gas_bill', '2024-09-01', 75, 'needs'),
('trash_bill', '2024-09-01', 60, 'needs'),
('water_bill', '2024-09-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2024-09-01', 5, 'wants'),
('netflix_subscription', '2024-09-01', 16, 'wants'),
('prime_subscription', '2024-09-01', 15, 'wants'),
('credit_card1', '2024-09-01', 700, 'wants'),
('credit_card2', '2024-09-01', 300, 'wants'),
('car_payment', '2024-09-01', 200, 'wants'),
-- Investments
('401k_person1', '2024-09-01', 1960, 'investments'),
('401k_person2', '2024-09-01', 1960, 'investments'),
('edu_529', '2024-09-01', 625, 'investments'),
('HSA', '2024-09-01', 525, 'investments'),
('stocks', '2024-09-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for October 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2024-10-01', 2000, 'taxes'),
('federal_income_tax_person2', '2024-10-01', 1000, 'taxes'),
('state_income_tax_person1', '2024-10-01', 600, 'taxes'),
('state_income_tax_person2', '2024-10-01', 300, 'taxes'),
('medicare_person1', '2024-10-01', 100, 'taxes'),
('medicare_person2', '2024-10-01', 30, 'taxes'),
('social_security_person1', '2024-10-01', 500, 'taxes'),
('social_security_person2', '2024-10-01', 200, 'taxes'),
-- Needs
('mortgage', '2024-10-01', 2000, 'needs'),
('hoa', '2024-10-01', 500, 'needs'),
('car_insurance', '2024-10-01', 100, 'needs'),
('car_registration', '2024-10-01', 0, 'needs'),
('health_insurance', '2024-10-01', 350, 'needs'),
('phone_bill', '2024-10-01', 200, 'needs'),
('internet_bill', '2024-10-01', 100, 'needs'),
('electricity_bill', '2024-10-01', 150, 'needs'),
('gas_bill', '2024-10-01', 75, 'needs'),
('trash_bill', '2024-10-01', 60, 'needs'),
('water_bill', '2024-10-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2024-10-01', 5, 'wants'),
('netflix_subscription', '2024-10-01', 16, 'wants'),
('prime_subscription', '2024-10-01', 15, 'wants'),
('credit_card1', '2024-10-01', 700, 'wants'),
('credit_card2', '2024-10-01', 300, 'wants'),
('car_payment', '2024-10-01', 200, 'wants'),
-- Investments
('401k_person1', '2024-10-01', 1960, 'investments'),
('401k_person2', '2024-10-01', 1960, 'investments'),
('edu_529', '2024-10-01', 625, 'investments'),
('HSA', '2024-10-01', 525, 'investments'),
('stocks', '2024-10-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for November 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2024-11-01', 2000, 'taxes'),
('federal_income_tax_person2', '2024-11-01', 1000, 'taxes'),
('state_income_tax_person1', '2024-11-01', 600, 'taxes'),
('state_income_tax_person2', '2024-11-01', 300, 'taxes'),
('medicare_person1', '2024-11-01', 100, 'taxes'),
('medicare_person2', '2024-11-01', 30, 'taxes'),
('social_security_person1', '2024-11-01', 500, 'taxes'),
('social_security_person2', '2024-11-01', 200, 'taxes'),
-- Needs
('mortgage', '2024-11-01', 2000, 'needs'),
('hoa', '2024-11-01', 500, 'needs'),
('car_insurance', '2024-11-01', 100, 'needs'),
('car_registration', '2024-11-01', 0, 'needs'),
('health_insurance', '2024-11-01', 350, 'needs'),
('phone_bill', '2024-11-01', 200, 'needs'),
('internet_bill', '2024-11-01', 100, 'needs'),
('electricity_bill', '2024-11-01', 150, 'needs'),
('gas_bill', '2024-11-01', 75, 'needs'),
('trash_bill', '2024-11-01', 60, 'needs'),
('water_bill', '2024-11-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2024-11-01', 5, 'wants'),
('netflix_subscription', '2024-11-01', 16, 'wants'),
('prime_subscription', '2024-11-01', 15, 'wants'),
('credit_card1', '2024-11-01', 700, 'wants'),
('credit_card2', '2024-11-01', 300, 'wants'),
('car_payment', '2024-11-01', 200, 'wants'),
-- Investments
('401k_person1', '2024-11-01', 1960, 'investments'),
('401k_person2', '2024-11-01', 1960, 'investments'),
('edu_529', '2024-11-01', 625, 'investments'),
('HSA', '2024-11-01', 525, 'investments'),
('stocks', '2024-11-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



-- Inserting entries for December 2024
INSERT INTO expense (source, source_date, amount, category)
VALUES
-- Taxes
('federal_income_tax_person1', '2024-12-01', 2000, 'taxes'),
('federal_income_tax_person2', '2024-12-01', 1000, 'taxes'),
('state_income_tax_person1', '2024-12-01', 600, 'taxes'),
('state_income_tax_person2', '2024-12-01', 300, 'taxes'),
('medicare_person1', '2024-12-01', 100, 'taxes'),
('medicare_person2', '2024-12-01', 30, 'taxes'),
('social_security_person1', '2024-12-01', 500, 'taxes'),
('social_security_person2', '2024-12-01', 200, 'taxes'),
-- Needs
('mortgage', '2024-12-01', 2000, 'needs'),
('hoa', '2024-12-01', 500, 'needs'),
('car_insurance', '2024-12-01', 100, 'needs'),
('car_registration', '2024-12-01', 0, 'needs'),
('health_insurance', '2024-12-01', 350, 'needs'),
('phone_bill', '2024-12-01', 200, 'needs'),
('internet_bill', '2024-12-01', 100, 'needs'),
('electricity_bill', '2024-12-01', 150, 'needs'),
('gas_bill', '2024-12-01', 75, 'needs'),
('trash_bill', '2024-12-01', 60, 'needs'),
('water_bill', '2024-12-01', 35, 'needs'),
-- Wants
('spotify_subscription', '2024-12-01', 5, 'wants'),
('netflix_subscription', '2024-12-01', 16, 'wants'),
('prime_subscription', '2024-12-01', 15, 'wants'),
('credit_card1', '2024-12-01', 700, 'wants'),
('credit_card2', '2024-12-01', 300, 'wants'),
('car_payment', '2024-12-01', 200, 'wants'),
-- Investments
('401k_person1', '2024-12-01', 1960, 'investments'),
('401k_person2', '2024-12-01', 1960, 'investments'),
('edu_529', '2024-12-01', 625, 'investments'),
('HSA', '2024-12-01', 525, 'investments'),
('stocks', '2024-12-01', 1000, 'investments')
ON CONFLICT (source, source_date) DO UPDATE
    SET amount = excluded.amount, category = excluded.category;



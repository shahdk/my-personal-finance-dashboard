-- Inserting entries for January 2024
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2024-01-01', 8000, 'earned_income'),
    ('paycheck_person2', '2024-01-01', 5000, 'earned_income'),
    ('stocks', '2024-01-01', 500, 'earned_income'),
    ('cash_bonus', '2024-01-01', 100, 'earned_income'),
    ('ordinary_dividends', '2024-01-01', 150, 'passive_income'),
    ('interest_income', '2024-01-01', 750, 'passive_income'),
    ('short_term_gains', '2024-01-01', 0, 'passive_income'),
    ('qualifying_dividends', '2024-01-01', 300, 'passive_income'),
    ('long_term_gains', '2024-01-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Inserting entries for February 2024
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2024-02-01', 8000, 'earned_income'),
    ('paycheck_person2', '2024-02-01', 5000, 'earned_income'),
    ('stocks', '2024-02-01', 500, 'earned_income'),
    ('cash_bonus', '2024-02-01', 100, 'earned_income'),
    ('ordinary_dividends', '2024-02-01', 150, 'passive_income'),
    ('interest_income', '2024-02-01', 750, 'passive_income'),
    ('short_term_gains', '2024-02-01', 0, 'passive_income'),
    ('qualifying_dividends', '2024-02-01', 300, 'passive_income'),
    ('long_term_gains', '2024-02-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Inserting entries for March 2024
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2024-03-01', 8000, 'earned_income'),
    ('paycheck_person2', '2024-03-01', 5000, 'earned_income'),
    ('stocks', '2024-03-01', 500, 'earned_income'),
    ('cash_bonus', '2024-03-01', 100, 'earned_income'),
    ('ordinary_dividends', '2024-03-01', 150, 'passive_income'),
    ('interest_income', '2024-03-01', 750, 'passive_income'),
    ('short_term_gains', '2024-03-01', 0, 'passive_income'),
    ('qualifying_dividends', '2024-03-01', 300, 'passive_income'),
    ('long_term_gains', '2024-03-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Inserting entries for April 2024
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2024-04-01', 8000, 'earned_income'),
    ('paycheck_person2', '2024-04-01', 5000, 'earned_income'),
    ('stocks', '2024-04-01', 500, 'earned_income'),
    ('cash_bonus', '2024-04-01', 100, 'earned_income'),
    ('ordinary_dividends', '2024-04-01', 150, 'passive_income'),
    ('interest_income', '2024-04-01', 750, 'passive_income'),
    ('short_term_gains', '2024-04-01', 0, 'passive_income'),
    ('qualifying_dividends', '2024-04-01', 300, 'passive_income'),
    ('long_term_gains', '2024-04-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Inserting entries for May 2024
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2024-05-01', 8000, 'earned_income'),
    ('paycheck_person2', '2024-05-01', 5000, 'earned_income'),
    ('stocks', '2024-05-01', 500, 'earned_income'),
    ('cash_bonus', '2024-05-01', 100, 'earned_income'),
    ('ordinary_dividends', '2024-05-01', 150, 'passive_income'),
    ('interest_income', '2024-05-01', 750, 'passive_income'),
    ('short_term_gains', '2024-05-01', 0, 'passive_income'),
    ('qualifying_dividends', '2024-05-01', 300, 'passive_income'),
    ('long_term_gains', '2024-05-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Inserting entries for June 2024
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2024-06-01', 8000, 'earned_income'),
    ('paycheck_person2', '2024-06-01', 5000, 'earned_income'),
    ('stocks', '2024-06-01', 500, 'earned_income'),
    ('cash_bonus', '2024-06-01', 100, 'earned_income'),
    ('ordinary_dividends', '2024-06-01', 150, 'passive_income'),
    ('interest_income', '2024-06-01', 750, 'passive_income'),
    ('short_term_gains', '2024-06-01', 0, 'passive_income'),
    ('qualifying_dividends', '2024-06-01', 300, 'passive_income'),
    ('long_term_gains', '2024-06-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Inserting entries for July 2024
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2024-07-01', 8000, 'earned_income'),
    ('paycheck_person2', '2024-07-01', 5000, 'earned_income'),
    ('stocks', '2024-07-01', 500, 'earned_income'),
    ('cash_bonus', '2024-07-01', 100, 'earned_income'),
    ('ordinary_dividends', '2024-07-01', 150, 'passive_income'),
    ('interest_income', '2024-07-01', 750, 'passive_income'),
    ('short_term_gains', '2024-07-01', 0, 'passive_income'),
    ('qualifying_dividends', '2024-07-01', 300, 'passive_income'),
    ('long_term_gains', '2024-07-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Inserting entries for August 2024
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2024-08-01', 8000, 'earned_income'),
    ('paycheck_person2', '2024-08-01', 5000, 'earned_income'),
    ('stocks', '2024-08-01', 500, 'earned_income'),
    ('cash_bonus', '2024-08-01', 100, 'earned_income'),
    ('ordinary_dividends', '2024-08-01', 150, 'passive_income'),
    ('interest_income', '2024-08-01', 750, 'passive_income'),
    ('short_term_gains', '2024-08-01', 0, 'passive_income'),
    ('qualifying_dividends', '2024-08-01', 300, 'passive_income'),
    ('long_term_gains', '2024-08-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Inserting entries for September 2024
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2024-09-01', 8000, 'earned_income'),
    ('paycheck_person2', '2024-09-01', 5000, 'earned_income'),
    ('stocks', '2024-09-01', 500, 'earned_income'),
    ('cash_bonus', '2024-09-01', 100, 'earned_income'),
    ('ordinary_dividends', '2024-09-01', 150, 'passive_income'),
    ('interest_income', '2024-09-01', 750, 'passive_income'),
    ('short_term_gains', '2024-09-01', 0, 'passive_income'),
    ('qualifying_dividends', '2024-09-01', 300, 'passive_income'),
    ('long_term_gains', '2024-09-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Inserting entries for October 2024
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2024-10-01', 8000, 'earned_income'),
    ('paycheck_person2', '2024-10-01', 5000, 'earned_income'),
    ('stocks', '2024-10-01', 500, 'earned_income'),
    ('cash_bonus', '2024-10-01', 100, 'earned_income'),
    ('ordinary_dividends', '2024-10-01', 150, 'passive_income'),
    ('interest_income', '2024-10-01', 750, 'passive_income'),
    ('short_term_gains', '2024-10-01', 0, 'passive_income'),
    ('qualifying_dividends', '2024-10-01', 300, 'passive_income'),
    ('long_term_gains', '2024-10-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Inserting entries for November 2024
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2024-11-01', 8000, 'earned_income'),
    ('paycheck_person2', '2024-11-01', 5000, 'earned_income'),
    ('stocks', '2024-11-01', 500, 'earned_income'),
    ('cash_bonus', '2024-11-01', 100, 'earned_income'),
    ('ordinary_dividends', '2024-11-01', 150, 'passive_income'),
    ('interest_income', '2024-11-01', 750, 'passive_income'),
    ('short_term_gains', '2024-11-01', 0, 'passive_income'),
    ('qualifying_dividends', '2024-11-01', 300, 'passive_income'),
    ('long_term_gains', '2024-11-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;
--
--
-- Inserting entries for December 2024
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2024-12-01', 8000, 'earned_income'),
    ('paycheck_person2', '2024-12-01', 5000, 'earned_income'),
    ('stocks', '2024-12-01', 500, 'earned_income'),
    ('cash_bonus', '2024-12-01', 100, 'earned_income'),
    ('ordinary_dividends', '2024-12-01', 150, 'passive_income'),
    ('interest_income', '2024-12-01', 750, 'passive_income'),
    ('short_term_gains', '2024-12-01', 0, 'passive_income'),
    ('qualifying_dividends', '2024-12-01', 300, 'passive_income'),
    ('long_term_gains', '2024-12-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


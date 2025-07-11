-- Inserting entries for January 2025
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2025-01-01', 9000, 'earned_income'),
    ('paycheck_person2', '2025-01-01', 7000, 'earned_income'),
    ('stocks', '2025-01-01', 500, 'earned_income'),
    ('cash_bonus', '2025-01-01', 100, 'earned_income'),
    ('ordinary_dividends', '2025-01-01', 250, 'passive_income'),
    ('interest_income', '2025-01-01', 750, 'passive_income'),
    ('short_term_gains', '2025-01-01', 0, 'passive_income'),
    ('qualifying_dividends', '2025-01-01', 300, 'passive_income'),
    ('long_term_gains', '2025-01-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Inserting entries for February 2025
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2025-02-01', 9000, 'earned_income'),
    ('paycheck_person2', '2025-02-01', 7000, 'earned_income'),
    ('stocks', '2025-02-01', 500, 'earned_income'),
    ('cash_bonus', '2025-02-01', 100, 'earned_income'),
    ('ordinary_dividends', '2025-02-01', 250, 'passive_income'),
    ('interest_income', '2025-02-01', 750, 'passive_income'),
    ('short_term_gains', '2025-02-01', 0, 'passive_income'),
    ('qualifying_dividends', '2025-02-01', 300, 'passive_income'),
    ('long_term_gains', '2025-02-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Inserting entries for March 2025
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2025-03-01', 9000, 'earned_income'),
    ('paycheck_person2', '2025-03-01', 7000, 'earned_income'),
    ('stocks', '2025-03-01', 500, 'earned_income'),
    ('cash_bonus', '2025-03-01', 100, 'earned_income'),
    ('ordinary_dividends', '2025-03-01', 250, 'passive_income'),
    ('interest_income', '2025-03-01', 750, 'passive_income'),
    ('short_term_gains', '2025-03-01', 0, 'passive_income'),
    ('qualifying_dividends', '2025-03-01', 300, 'passive_income'),
    ('long_term_gains', '2025-03-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Inserting entries for April 2025
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2025-04-01', 9000, 'earned_income'),
    ('paycheck_person2', '2025-04-01', 7000, 'earned_income'),
    ('stocks', '2025-04-01', 500, 'earned_income'),
    ('cash_bonus', '2025-04-01', 100, 'earned_income'),
    ('ordinary_dividends', '2025-04-01', 250, 'passive_income'),
    ('interest_income', '2025-04-01', 750, 'passive_income'),
    ('short_term_gains', '2025-04-01', 0, 'passive_income'),
    ('qualifying_dividends', '2025-04-01', 300, 'passive_income'),
    ('long_term_gains', '2025-04-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Inserting entries for May 2025
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2025-05-01', 9000, 'earned_income'),
    ('paycheck_person2', '2025-05-01', 7000, 'earned_income'),
    ('stocks', '2025-05-01', 500, 'earned_income'),
    ('cash_bonus', '2025-05-01', 100, 'earned_income'),
    ('ordinary_dividends', '2025-05-01', 250, 'passive_income'),
    ('interest_income', '2025-05-01', 750, 'passive_income'),
    ('short_term_gains', '2025-05-01', 0, 'passive_income'),
    ('qualifying_dividends', '2025-05-01', 300, 'passive_income'),
    ('long_term_gains', '2025-05-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Inserting entries for June 2025
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2025-06-01', 9000, 'earned_income'),
    ('paycheck_person2', '2025-06-01', 7000, 'earned_income'),
    ('stocks', '2025-06-01', 500, 'earned_income'),
    ('cash_bonus', '2025-06-01', 100, 'earned_income'),
    ('ordinary_dividends', '2025-06-01', 250, 'passive_income'),
    ('interest_income', '2025-06-01', 750, 'passive_income'),
    ('short_term_gains', '2025-06-01', 0, 'passive_income'),
    ('qualifying_dividends', '2025-06-01', 300, 'passive_income'),
    ('long_term_gains', '2025-06-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Inserting entries for July 2025
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2025-07-01', 9000, 'earned_income'),
    ('paycheck_person2', '2025-07-01', 7000, 'earned_income'),
    ('stocks', '2025-07-01', 500, 'earned_income'),
    ('cash_bonus', '2025-07-01', 100, 'earned_income'),
    ('ordinary_dividends', '2025-07-01', 250, 'passive_income'),
    ('interest_income', '2025-07-01', 750, 'passive_income'),
    ('short_term_gains', '2025-07-01', 0, 'passive_income'),
    ('qualifying_dividends', '2025-07-01', 300, 'passive_income'),
    ('long_term_gains', '2025-07-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Inserting entries for August 2025
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2025-08-01', 9000, 'earned_income'),
    ('paycheck_person2', '2025-08-01', 7000, 'earned_income'),
    ('stocks', '2025-08-01', 500, 'earned_income'),
    ('cash_bonus', '2025-08-01', 100, 'earned_income'),
    ('ordinary_dividends', '2025-08-01', 250, 'passive_income'),
    ('interest_income', '2025-08-01', 750, 'passive_income'),
    ('short_term_gains', '2025-08-01', 0, 'passive_income'),
    ('qualifying_dividends', '2025-08-01', 300, 'passive_income'),
    ('long_term_gains', '2025-08-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Inserting entries for September 2025
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2025-09-01', 9000, 'earned_income'),
    ('paycheck_person2', '2025-09-01', 7000, 'earned_income'),
    ('stocks', '2025-09-01', 500, 'earned_income'),
    ('cash_bonus', '2025-09-01', 100, 'earned_income'),
    ('ordinary_dividends', '2025-09-01', 250, 'passive_income'),
    ('interest_income', '2025-09-01', 750, 'passive_income'),
    ('short_term_gains', '2025-09-01', 0, 'passive_income'),
    ('qualifying_dividends', '2025-09-01', 300, 'passive_income'),
    ('long_term_gains', '2025-09-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Inserting entries for October 2025
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2025-10-01', 9000, 'earned_income'),
    ('paycheck_person2', '2025-10-01', 7000, 'earned_income'),
    ('stocks', '2025-10-01', 500, 'earned_income'),
    ('cash_bonus', '2025-10-01', 100, 'earned_income'),
    ('ordinary_dividends', '2025-10-01', 250, 'passive_income'),
    ('interest_income', '2025-10-01', 750, 'passive_income'),
    ('short_term_gains', '2025-10-01', 0, 'passive_income'),
    ('qualifying_dividends', '2025-10-01', 300, 'passive_income'),
    ('long_term_gains', '2025-10-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Inserting entries for November 2025
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2025-11-01', 9000, 'earned_income'),
    ('paycheck_person2', '2025-11-01', 7000, 'earned_income'),
    ('stocks', '2025-11-01', 500, 'earned_income'),
    ('cash_bonus', '2025-11-01', 100, 'earned_income'),
    ('ordinary_dividends', '2025-11-01', 250, 'passive_income'),
    ('interest_income', '2025-11-01', 750, 'passive_income'),
    ('short_term_gains', '2025-11-01', 0, 'passive_income'),
    ('qualifying_dividends', '2025-11-01', 300, 'passive_income'),
    ('long_term_gains', '2025-11-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;
--
--
-- Inserting entries for December 2025
INSERT INTO income (source, source_date, amount, category)
VALUES
    ('paycheck_person1', '2025-12-01', 9000, 'earned_income'),
    ('paycheck_person2', '2025-12-01', 7000, 'earned_income'),
    ('stocks', '2025-12-01', 500, 'earned_income'),
    ('cash_bonus', '2025-12-01', 100, 'earned_income'),
    ('ordinary_dividends', '2025-12-01', 250, 'passive_income'),
    ('interest_income', '2025-12-01', 750, 'passive_income'),
    ('short_term_gains', '2025-12-01', 0, 'passive_income'),
    ('qualifying_dividends', '2025-12-01', 300, 'passive_income'),
    ('long_term_gains', '2025-12-01', 200, 'passive_income')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


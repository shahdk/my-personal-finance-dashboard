-- 529
INSERT INTO net_worth (source, source_date, amount, category)
VALUES
    ('529', '2024-12-31', 10000, 'Retirement'),
    ('529', '2025-12-31', 18000, 'Retirement')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;

-- Car
INSERT INTO net_worth (source, source_date, amount, category)
VALUES
    ('Camry', '2024-12-31', 22000, 'Car'),
    ('Camry', '2025-12-31', 20000, 'Car')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Chase Checkings
INSERT INTO net_worth (source, source_date, amount, category)
VALUES
    ('Chase Checkings', '2024-12-31', 5000, 'Cash'),
    ('Chase Checkings', '2025-12-31', 5500, 'Cash')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Chase Savings
INSERT INTO net_worth (source, source_date, amount, category)
VALUES
    ('Chase Savings', '2024-12-31', 1000, 'Cash'),
    ('Chase Savings', '2025-12-31', 1100, 'Cash')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Credit Card
INSERT INTO net_worth (source, source_date, amount, category)
VALUES
    ('Credit Cards', '2024-12-31', -500, 'Liability'),
    ('Credit Cards', '2025-12-31', -700, 'Liability')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;

-- 401k
INSERT INTO net_worth (source, source_date, amount, category)
VALUES
    ('401k Person1', '2024-12-31', 23000, 'Retirement'),
    ('401k Person1', '2025-12-31', 23500, 'Retirement')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- 401k
INSERT INTO net_worth (source, source_date, amount, category)
VALUES
    ('401k Person2', '2024-12-31', 23000, 'Retirement'),
    ('401k Person2', '2025-12-31', 23500, 'Retirement')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- ETrade Brokerage
INSERT INTO net_worth (source, source_date, amount, category)
VALUES
    ('ETrade Brokerage', '2024-12-31', 5000, 'Stock Investment'),
    ('ETrade Brokerage', '2025-12-31', 6000, 'Stock Investment')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- HSA
INSERT INTO net_worth (source, source_date, amount, category)
VALUES
    ('HSA', '2024-12-31', 8300, 'Health Savings Account'),
    ('HSA', '2025-12-31', 8550, 'Health Savings Account')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;

-- Marcus
INSERT INTO net_worth (source, source_date, amount, category)
VALUES
    ('Marcus Savings', '2024-12-31', 10000, 'Cash'),
    ('Marcus Savings', '2025-12-31', 12000, 'Cash')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;


-- Roth IRA
INSERT INTO net_worth (source, source_date, amount, category)
VALUES
    ('Roth IRA', '2024-12-31', 5000, 'Retirement'),
    ('Roth IRA', '2025-12-31', 5500, 'Retirement')
ON CONFLICT (source, source_date) DO UPDATE
SET amount = excluded.amount, category = excluded.category;
INSERT INTO vacation (iso_code, start_date, end_date, city, amount, latitude, longitude)
VALUES
    ('US-TN', '2023-01-01', '2023-01-04', 'Nashville', 1000, 36.174465, -86.767960),
    ('US-AZ', '2023-08-01', '2023-08-05', 'Phoenix', 2000, 33.448376, -112.074036),
    ('US-HI', '2024-01-01', '2024-01-06', 'Kailua', 5000, 19.639994, -155.996933),
    ('US-TX', '2024-12-01', '2024-12-08', 'Austin', 3000, 30.266666, -97.733330),
    ('US-TX', '2025-03-01', '2025-03-04', 'Houston', 2500, 29.749907, -95.358421),
    ('US-HI', '2025-07-01', '2025-07-15', 'Honolulu', 6000, 21.315603, -157.858093)
ON CONFLICT (iso_code, start_date, end_date, city) DO UPDATE
    SET amount = excluded.amount, latitude = excluded.latitude, longitude = excluded.longitude;
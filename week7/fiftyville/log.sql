-- Keep a log of any SQL queries you execute as you solve the mystery.
.tables
.schema

-- Seeing the descriptions of the crime
SELECT description
FROM crime_scene_reports
WHERE day = 28 AND month = 7 AND year = 2021 AND street = 'Humphrey Street';

-- Seeing the interviews notes
SELECT transcript
FROM interviews
WHERE day = 28 AND month = 7 AND year = 2021 AND transcript LIKE "%bakery%";

-- Searching by the banking clues
-- Seeing the accounts
SELECT account_number, amount
FROM atm_transactions
WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';
--Seeing their names
SELECT name, t.amount
FROM people p JOIN bank_accounts b JOIN atm_transactions t
ON p.id = b.person_id AND b.account_number = t.account_number
WHERE t.year = 2021 AND t.month = 7 AND t.day = 28 AND t.atm_location = 'Leggett Street' AND t.transaction_type = 'withdraw';

-- Searching by the airplanes clues
-- Finding the firsts flights on the following day
SELECT f.id, full_name, city, f.hour, f.minute
FROM airports a JOIN flights f
ON a.id = f.destination_airport_id
WHERE f.origin_airport_id =
(  SELECT id
   FROM airports
   WHERE city = 'Fiftyville')
AND f.year = 2021 AND f.month = 7 AND f.day = 29
ORDER BY f.hour, f.minute;
-- Seeing the people on the NYC flight (our suspects)
SELECT p.name
FROM people p JOIN passengers ps
ON p.passport_number = ps.passport_number
JOIN flights f
ON ps.flight_id = f.id
WHERE f.year = 2021 AND f.month = 7 AND f.day = 29 AND f.hour = 8 AND f.minute = 20
ORDER BY p.name;
-- Finding the caller who bought the ticket according to the calls (our accomplices)
SELECT p.name, pc.duration
FROM people p
JOIN phone_calls pc
ON p.phone_number = pc.caller
WHERE pc.year = 2021 AND pc.month = 7 AND pc.day = 28 AND pc.duration <= 60
ORDER BY pc.duration;
-- Finding who was participating to the call
SELECT p.name, pc.duration
FROM people p JOIN phone_calls pc
ON p.phone_number = pc.receiver
WHERE pc.year = 2021 AND pc.month = 7 AND pc.day = 28 AND pc.duration <= 60
ORDER BY pc.duration;

-- Searching by the cars clue
SELECT p.name, l.hour, l.minute
FROM people p JOIN bakery_security_logs l
ON p.license_plate = l.license_plate
WHERE l.year = 2021 AND l.month = 7 AND l.day = 28 AND l.activity = 'exit'
AND l.hour = 10 AND l.minute >= 15 AND l.minute <= 25
ORDER BY l.minute;
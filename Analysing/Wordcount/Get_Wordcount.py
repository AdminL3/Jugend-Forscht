-- Step 1: Create a database
CREATE DATABASE IF NOT EXISTS DateNumbersDB

-- Step 2: Use the new database
USE DateNumbersDB

-- Step 3: Create the table to store dates and numbers
CREATE TABLE IF NOT EXISTS DateNumbers(
    id INT AUTO_INCREMENT PRIMARY KEY, -- unique identifier for each entry
    date DATE NOT NULL,                -- column to store the date
    number INT NOT NULL - - column to store the associated number
)

-- Step 4: Insert sample data
INSERT INTO DateNumbers(date, number)
VALUES
('2024-11-11', 10),
('2024-11-11', 20),
('2024-11-12', 30),
('2024-11-13', 40),
('2024-11-13', 50),
('2024-11-14', 60)

-- Step 5: Query the data(optional example queries)
-- Example query to get all numbers for a specific date
SELECT number FROM DateNumbers WHERE date = '2024-11-11'

-- Example query to get all dates and associated numbers
SELECT date, number FROM DateNumbers ORDER BY date

-- Example query to count how many numbers are associated with each date
SELECT date, COUNT(number) AS count_of_numbers
FROM DateNumbers
GROUP BY date

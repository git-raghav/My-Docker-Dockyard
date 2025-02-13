CREATE TABLE IF NOT EXISTS passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL
);

INSERT INTO passengers (name, location) VALUES
('Raghav Agarwal', 'Dehradun'),
('Aryan Soni', 'Delhi');

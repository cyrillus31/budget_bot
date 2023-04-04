CREATE TABLE IF NOT EXISTS  expenses (
    amount INT,
    category VARCHAR NULL,
    time TIMESTAMP,
    limit_id TIMESTAMP,
    FOREIGN KEY(limit_id) REFERENCES limits(moth)
);

CREATE TABLE IF NOT EXISTS  limits (
    month TIMESTAMP TIMESTAMP PRIMARY KEY,
    monthly_limit INT
);
CREATE TABLE IF NOT EXISTS  expenses (
    amount INT,
    category VARCHAR NULL,
    time TIMESTAMP,
    limit_id TIMESTAMP,
    FOREIGN KEY(limit_id) REFERENCES limits(month)
);

CREATE TABLE IF NOT EXISTS  limits (
    month TIMESTAMP PRIMARY KEY,
    monthly_limit INTEGER,
    daily_limit INTEGER
);
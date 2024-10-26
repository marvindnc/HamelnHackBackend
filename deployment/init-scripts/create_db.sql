
CREATE TABLE complaints (
    id SERIAL PRIMARY KEY,  -- PostgreSQL uses SERIAL for auto-incrementing integers
    description VARCHAR(255) NOT NULL,
    image_location VARCHAR(255) NOT NULL,
    capture_time DATE NOT NULL
);

COMMIT;
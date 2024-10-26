
CREATE TABLE complaints (
    id SERIAL PRIMARY KEY,  -- PostgreSQL uses SERIAL for auto-incrementing integers
    description VARCHAR(255) NOT NULL,
    image_location VARCHAR(255) NOT NULL,
    capture_time DATE NOT NULL
);

CREATE TABLE images (
    id SERIAL PRIMARY KEY,
    image BYTEA,
    image_class VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    classes TEXT,
    category VARCHAR(255) NOT NULL
);

COMMIT;
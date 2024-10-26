
CREATE TABLE complaints (
    id SERIAL PRIMARY KEY,
    image BYTEA,
    image_class VARCHAR(255) NOT NULL,
    category INT,
    description VARCHAR(255) NOT NULL,
    capture_time DATE NOT NULL
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    classes TEXT,
    category VARCHAR(255) NOT NULL
);

COMMIT;
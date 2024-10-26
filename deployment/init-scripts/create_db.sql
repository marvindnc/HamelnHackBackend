
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

INSERT INTO categories (classes, category) VALUES ('Straßenbeleuchtung', 'traffic light');
INSERT INTO categories (classes, category) VALUES ('Grünflächen und Parks', 'bird');
INSERT INTO categories (classes, category) VALUES ('Grünflächen und Parks', 'cat');
INSERT INTO categories (classes, category) VALUES ('Grünflächen und Parks', 'dog');

INSERT INTO categories (classes, category) VALUES ('Müll und Umweltverschmutzung', 'banana');
INSERT INTO categories (classes, category) VALUES ('Müll und Umweltverschmutzung', 'apple');

INSERT INTO categories (classes, category) VALUES ('Straßen-, Gehwege und Radwege Schäden', 'bicycle');

INSERT INTO categories (classes, category) VALUES ('Spielplatz', 'sports ball');

INSERT INTO categories (classes, category) VALUES ('Verkehr und Straßeninfrastruktur', 'person');
INSERT INTO categories (classes, category) VALUES ('Verkehr und Straßeninfrastruktur', 'car');

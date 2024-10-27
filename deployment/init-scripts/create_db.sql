
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

INSERT INTO categories (category, classes) VALUES ('Straßenbeleuchtung', 'traffic light');
INSERT INTO categories (category, classes) VALUES ('Grünflächen und Parks', 'bird');
INSERT INTO categories (category, classes) VALUES ('Grünflächen und Parks', 'cat');
INSERT INTO categories (category, classes) VALUES ('Grünflächen und Parks', 'dog');

INSERT INTO categories (category, classes) VALUES ('Müll und Umweltverschmutzung', 'banana');
INSERT INTO categories (category, classes) VALUES ('Müll und Umweltverschmutzung', 'apple');

INSERT INTO categories (category, classes) VALUES ('Straßen-, Gehwege und Radwege Schäden', 'bicycle');

INSERT INTO categories (category, classes) VALUES ('Spielplatz', 'sports ball');

INSERT INTO categories (category, classes) VALUES ('Verkehr und Straßeninfrastruktur', 'person');
INSERT INTO categories (category, classes) VALUES ('Verkehr und Straßeninfrastruktur', 'car');

INSERT INTO categories (category, classes) VALUES ('Bürgeranliegen', 'laptop');
INSERT INTO categories (category, classes) VALUES ('Bürgeranliegen', 'remote control');
INSERT INTO categories (category, classes) VALUES ('Bürgeranliegen', 'keyboard');
INSERT INTO categories (category, classes) VALUES ('Bürgeranliegen', 'cell phone');

INSERT INTO categories (category, classes) VALUES ('Öffentliche Anlagen', 'bench');
INSERT INTO categories (category, classes) VALUES ('Öffentliche Anlagen', 'chair');
INSERT INTO categories (category, classes) VALUES ('Öffentliche Anlagen', 'couch');
INSERT INTO categories (category, classes) VALUES ('Öffentliche Anlagen', 'dining table');

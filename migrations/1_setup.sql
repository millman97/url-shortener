DROP TABLE IF EXISTS links;

CREATE TABLE links (
    id serial PRIMARY KEY,
    link VARCHAR(60000) UNIQUE,
    uid VARCHAR(8) UNIQUE
    );

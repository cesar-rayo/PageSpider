CREATE TABLE main.words(
    word TEXT PRIMARY KEY NOT NULL,
    usage_count INT DEFAULT 1 NOT NULL
);
CREATE UNIQUE INDEX words_word_unidex ON words(word);
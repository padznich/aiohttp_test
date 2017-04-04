-- Prepare for new tables
DROP TABLE IF EXISTS choice;
DROP TABLE IF EXISTS question;

-- tables
-- Table: question
CREATE TABLE question (
    id serial  NOT NULL,
    question_text varchar(200) NULL,
    pub_date date NOT NULL,
    CONSTRAINT question_pk PRIMARY KEY (id)
);

-- Table: choice
CREATE TABLE choice (
    id serial  NOT NULL,
    question_id int NOT NULL,
    choice_text varchar(200)  NULL,
    votes int DEFAULT 0,
    CONSTRAINT choice_pk PRIMARY KEY (id)
);

-- foreign keys
-- Reference: detail_description_grid_detail (table: detail_description)
ALTER TABLE choice ADD CONSTRAINT choice_question
    FOREIGN KEY (question_id)
    REFERENCES question (id) ON DELETE CASCADE
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- End of file.
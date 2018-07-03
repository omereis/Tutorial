DROP TABLE jobs;

CREATE TABLE jobs (
	token VARCHAR (20) NOT NULL,
	job_id INTEGER NOT NULL,
	PRIMARY KEY (token,job_id)
);

SELECT * FROM jobs;
DELETE FROM jobs WHERE token='a' AND job_id=3;

INSERT INTO jobs (token,job_id) VALUES ('a',1),('a',2),('a',3),('b',1),('b',2);

CREATE TABLE params (
	token VARCHAR (20) NOT NULL,
	job_id INTEGER NOT NULL,
	param VARCHAR(100),
	CONSTRAINT fk_p_j FOREIGN KEY (token,job_id) REFERENCES jobs(token,job_id) ON UPDATE CASCADE ON DELETE CASCADE
);
SELECT * FROM params;
DELETE FROM params;

INSERT INTO params (token,job_id,param) VALUES ('a',1,'abcdefg'),('a',1,'ghfbvnd'),('a',1,'ghfbvnd');

DROP TABLE params;

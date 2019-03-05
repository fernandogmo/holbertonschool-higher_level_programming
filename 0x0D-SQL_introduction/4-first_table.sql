-- a script that creates a table called first_table in the current database
-- with an id INt and a name less than 256 characters
CREATE TABLE if not EXISTS first_table (
	id INT NOT NULL,
	name VARCHAR(256) NOT NULL );

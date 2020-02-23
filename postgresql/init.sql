CREATE USER casting WITH PASSWORD 'pass';
CREATE DATABASE casting;
GRANT ALL PRIVILEGES ON DATABASE casting TO casting;

\connect casting casting

\connect postgres postgres
CREATE DATABASE casting_test;
GRANT ALL PRIVILEGES ON DATABASE casting_test TO casting;
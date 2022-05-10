CREATE DATABASE greenthumb_with_auth;
CREATE USER tim WITH PASSWORD 'greenthumbadminpw1129';
GRANT ALL PRIVILEGES ON DATABASE greenthumb TO tim;
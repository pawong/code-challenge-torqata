# TORQATA

### Local Deploy

From the root directory,
```
% docker-compose up --build -d
```

Server can be reached at `http://localhost:81/docs`, with following credentials, `torqata@mazookie.com`:`password123`.


### Cloud Run

Server can be reached at `https://torqata-tqfzurneya-uw.a.run.app/docs` with following credentials, `torqata@mazookie.com`:`password123`.

#### GCP Build Container and push
```
% gcloud builds submit --tag gcr.io/mazookie-1480821640022/torqata
```

#### GCP Deploy
```
% gcloud run deploy \
--set-env-vars="SERVER_NAME=api" \
--set-env-vars="SERVER_HOST=http://api/" \
--set-env-vars="SENTRY_DSN=" \
--set-env-vars="PROJECT_NAME=Torqata Assignment API" \
--set-env-vars="PROJECT_DESCRIPTION=Access to Torqata Assignment data archives" \
--set-env-vars="FIRST_SUPERUSER=torqata@mazookie.com" \
--set-env-vars="FIRST_SUPERUSER_PASSWORD=password123" \
--set-env-vars="POSTGRES_SERVER=34.105.45.176" \
--set-env-vars="POSTGRES_USER=torqata_worker" \
--set-env-vars="POSTGRES_PASSWORD=password123" \
--set-env-vars="POSTGRES_DB=torqata" \
--image=gcr.io/mazookie-1480821640022/torqata \
--platform=managed \
--add-cloudsql-instances=${POSTGRES_SERVER}
--region=${REGION} \
--project=${PROJECT}
```

### Database Initialization

#### Source
https://www.kaggle.com/shivamb/netflix-shows/data

#### Initialization script
```sql
CREATE TABLE IF NOT EXISTS users (
	id SERIAL PRIMARY KEY,
	full_name character varying,
	email character varying NOT NULL,
	hashed_password character varying NOT NULL,
	is_active boolean,
	is_superuser boolean,
	date_created timestamp without time zone DEFAULT now() NOT NULL,
	date_modified timestamp without time zone
);

INSERT INTO users (
	full_name,
	email,
	hashed_password,
	is_active,
	is_superuser
)
VALUES (
	'torqata worker',
	'torqata@mazookie.com',
	'$2b$12$qRAvvgSg7WK34hQk/Mwije6lpAprxgMSbZX7WcISnbZgtgiG.8D56',
	'True',
	'True'
);

CREATE TABLE IF NOT EXISTS titles (
	id SERIAL PRIMARY KEY,
	show_id text,
	category text,
	title text,
	director text,
	cast_members text,
	country text,
	date_added datetime,
	release_year integer,
	rating text,
	duration text,
	listed_in text,
	description text
);

COPY titles(
	show_id,
	category,
	title,
	director,
	cast_members,
	country,
	date_added,
	release_year,
	rating,
	duration,
	listed_in,
	description
)
FROM stdin CSV;
<< initialization data >>
```

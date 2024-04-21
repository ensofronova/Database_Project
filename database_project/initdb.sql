CREATE OR REPLACE FUNCTION init_tables()
	returns void
	language sql
	as $$

	create table if not exists "Business" (
		id serial not null primary key,
		name text not null,
		address text not null,
		supplier text not null,
		owner text not null,
		feature text not null
		);

	create table if not exists "Suppliers" (
		organisation text not null primary key,
		reviews text not null,
		phone_number varchar(11) not null
		);

	create table if not exists "Owners" (
		name text not null primary key,
		foundation_date date not null,
		email text not null
		);

	create table if not exists "Ratings" (
		business_name text not null,
		feedback text not null,
		grade integer not null
		);


	create index if not exists name on "Business" (name);
	create index if not exists owner on "Owners" (email);
	create index if not exists supplier on "Suppliers" (phone_number);
$$;
select i.region_economy from inflow i 
union 
select o.region_economy  from outflow o ;

create table paises (
	 id INTEGER PRIMARY KEY GENERATED ALWAYS AS identity,
	 pais varchar(255) not null
);

select * from outflow o ;

INSERT INTO paises (pais)
SELECT region_economy FROM inflow
UNION
SELECT region_economy FROM outflow;



ALTER TABLE inflow ADD COLUMN pais_id integer references paises(id);
ALTER TABLE outflow ADD COLUMN pais_id integer references paises(id);

UPDATE inflow i
SET pais_id = p.id
FROM paises p
WHERE p.pais = i.region_economy;

UPDATE outflow o
SET pais_id = p.id
FROM paises p
WHERE p.pais = o.region_economy;

select i.pais_id , i.region_economy from inflow i 
union 
select o.pais_id, o.region_economy  from outflow o ;

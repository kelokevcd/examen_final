*Los 10 países con el costo de vida más alto
SELECT 
    "Countries" AS "País",
    "Cost of living, 2017" AS "Costo de Vida",
    "Global rank" AS "Ranking Global"
FROM living
ORDER BY "Cost of living, 2017" DESC
LIMIT 10;

*Los 10 países con el costo de vida más bajo
SELECT 
    "Countries" AS "País",
    "Cost of living, 2017" AS "Costo de Vida",
    "Global rank" AS "Ranking Global"
FROM living
ORDER BY "Cost of living, 2017" ASC
LIMIT 10;

*El costo de vida de los países de América
SELECT 
    "Countries" AS "País",
    "Cost of living, 2017" AS "Costo de Vida",
    "Global rank" AS "Ranking Global",
    "Continent" AS "Continente"
FROM living
WHERE "Continent" = 'America'
ORDER BY "Cost of living, 2017" DESC;

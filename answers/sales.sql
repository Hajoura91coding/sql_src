SELECT client, sum(montant)
FROM sales
GROUP BY client
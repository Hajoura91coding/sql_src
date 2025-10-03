SELECT market_type, COUNT(market_type)
FROM df
GROUP BY market_type

SELECT market_type, COUNT(market_type)
FROM weights_turnover_retail
GROUP BY market_type

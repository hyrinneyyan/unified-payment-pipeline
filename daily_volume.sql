SELECT
    DATE(event_timestamp) AS payment_date,
    payment_type,
    SUM(amount) AS total_volume
FROM unified_payments
GROUP BY 1,2
ORDER BY 1;

SELECT
    customer_id,
    SUM(amount) AS total_spend
FROM unified_payments
WHERE status = 'SUCCESS'
GROUP BY customer_id;

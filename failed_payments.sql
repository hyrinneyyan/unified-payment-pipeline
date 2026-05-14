SELECT
    payment_type,
    COUNT(*) AS failed_count
FROM unified_payments
WHERE status = 'FAILED'
GROUP BY payment_type;

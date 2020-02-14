-- Get cjk charaters rows from table
SELECT count(product_id)  FROM products  WHERE not REGEXP_CONTAINS(title, r"[A-Za-z0-9]");

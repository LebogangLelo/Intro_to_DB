USE alx_book_store;


-- Query to print the full description of the books table
SELECT 
    COLUMN_NAME, 
    COLUMN_TYPE, 
    IS_NULLABLE, 
    COLUMN_KEY, 
    COLUMN_DEFAULT, 
    EXTRA 
FROM 
    information_schema.columns 
WHERE 
    table_schema = DATABASE() 
    AND table_name = 'books';


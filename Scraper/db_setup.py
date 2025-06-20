import sqlite3

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect('././Data/reviews.db')
cursor = conn.cursor()

# Create reviews table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        category TEXT,
        review_text TEXT,
        rating INTEGER,
        review_date TEXT,
        verified TEXT,
        UNIQUE(product_name, review_text, review_date)
    )
''')

print("Database and 'reviews' table created successfully.")

# Close connection
conn.commit()
conn.close()
# Analyzing trends

# Filtering read books
read_books = df[df['Exclusive Shelf'] == 'read']

# Number of books read
num_books_read = read_books.shape[0]

# Average rating given
average_rating_given = read_books['My Rating'].mean()

# Average rating of read books
average_rating_read_books = read_books['Average Rating'].mean()

# Total pages read
total_pages_read = read_books['Number of Pages'].dropna().astype(int).sum()

# Average pages per book
average_pages_per_book = read_books['Number of Pages'].dropna().astype(int).mean()

# Most read authors
most_read_authors = read_books['Author'].value_counts().head(10)

# Average rating by author
average_rating_by_author = read_books.groupby('Author')['My Rating'].mean().sort_values(ascending=False).head(10)

# Books read over time (by year)
read_books['Date Read'] = pd.to_datetime(read_books['Date Read'], errors='coerce')
books_read_over_time = read_books['Date Read'].dt.year.value_counts().sort_index()

# Pages read over time (by year)
read_books['Number of Pages'] = read_books['Number of Pages'].dropna().astype(int)
pages_read_over_time = read_books.groupby(read_books['Date Read'].dt.year)['Number of Pages'].sum().sort_index()

{
    "Number of Books Read": num_books_read,
    "Average Rating Given": average_rating_given,
    "Average Rating of Read Books": average_rating_read_books,
    "Total Pages Read": total_pages_read,
    "Average Pages per Book": average_pages_per_book,
    "Most Read Authors": most_read_authors,
    "Average Rating by Author": average_rating_by_author,
    "Books Read Over Time": books_read_over_time,
    "Pages Read Over Time": pages_read_over_time
}

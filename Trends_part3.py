# 1. Average rating for books in the "to-read" list
average_rating_to_read = to_read_books['Average Rating'].mean()

# 2. Preferred binding type
preferred_binding = read_books['Binding'].value_counts().idxmax()

# 3. Publication year - finding the most common publication year for read books
most_common_publication_year = read_books['Year Published'].mode().iloc[0]

# 4. Time a book sits in "to-read" before it goes to "read"
to_read_books['Date Added'] = pd.to_datetime(to_read_books['Date Added'], errors='coerce')
read_books['Date Added'] = pd.to_datetime(read_books['Date Added'], errors='coerce')
read_books['Time in To-Read'] = (read_books['Date Read'] - read_books['Date Added']).dt.days

average_time_in_to_read = read_books['Time in To-Read'].mean()

{
    "Average Rating of To-Read Books": average_rating_to_read,
    "Preferred Binding Type": preferred_binding,
    "Most Common Publication Year": most_common_publication_year,
    "Average Time in To-Read": average_time_in_to_read
}

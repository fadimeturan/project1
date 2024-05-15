# Library Organizer
#### Video Demo: <https://youtu.be/-wIMXGH4Y00>
#### Description: This is my Python project, named Library Organizer, aims to organize a book dataset stored in a CSV file into a structured library format. The input CSV file, named books.csv, contains information about various books such as title, author, genre, and page count. The program processes this dataset and generates a new CSV file named library.csv, where the books are organized based on their genre and shelf location.

# Usage
To run the program, execute the following command in the terminal: `python project.py books.csv library.csv`. Here, <books.csv> is the path to the input CSV file containing book information, and <library.csv> is the path where the organized library CSV file will be saved.

# Functionality
The program performs the following main tasks:

1- Input Validation: It checks if the correct number of command-line arguments is provided and verifies that the input and output files are CSV files.

2-Reading Input: The program reads the book information from the input CSV file and stores it in a list of dictionaries.

3- Genre Classification: It classifies each book into one of the predefined genres based on its theme. If the theme does not match any predefined genres, it is labeled as "GENRE NOT FOUND".

4- Shelf Assignment: Each book is assigned to a shelf based on its page count. The shelves are categorized into six sections based on the page count ranges.

5- Sorting: The books are sorted based on their shelf locations.

6- Writing Output: Finally, the organized book information is written to the output CSV file in the specified format.

# Functions
-> main()
This function serves as the entry point of the program. It calls other functions to perform various tasks such as input validation, data processing, and output generation.

-> len_arg()
This function validates the number of command-line arguments provided to the program. It checks if the correct number of arguments is provided and if the input and output files are CSV files. For this project, the correct number of command-line arguments is three.

-> genre(info)
This function classifies the genre of each book based on its theme. It takes the theme information as input and returns the corresponding genre. For example, if the theme of the book is "well-being", its genre is determined as "psychology".

-> shelf(num)
This function assigns a shelf location to each book based on its page count. It takes the page count as input and returns the shelf location. For example, if the page count of the book is 250, its shelf is determined as "4. shelf"

# Error Handling
The program handles various error scenarios such as incorrect command-line arguments, file not found, invalid data types, and unrecognized genres. Error messages are displayed to the user to guide them on how to resolve the issues.

# Conclusion
The Library Organizer project provides a convenient way to organize and categorize book data, making it easier for users to browse and locate books based on their interests. By leveraging Python's data processing capabilities, the program efficiently handles large datasets and produces well-structured library records.

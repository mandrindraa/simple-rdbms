# Simple RDBMS Implementation

## Project Overview
This project is a basic implementation of a Relational Database Management System (RDBMS) designed for educational purposes. It demonstrates fundamental database concepts such as tables, rows, columns, and basic SQL-like operations.

## Features
- Create, read, update, and delete (CRUD) operations on tables.
- Support for basic SQL-like queries.
- In-memory data storage for simplicity.
- Command-line interface for interaction.

## Technologies Used
- **Python**: Core programming language for the implementation.
- **SQLite** (optional): For comparison and testing purposes.

## How to Run
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/simple-rdbms.git
    cd simple-rdbms
    ```
2. Run the main script:
    ```bash
    python main.py
    ```

## Example Usage
```plaintext
> CREATE TABLE students (id INT, name TEXT, age INT);
> INSERT INTO students VALUES (1, 'Alice', 20);
> SELECT * FROM students;
```
<!--
## Project Structure
- `main.py`: Entry point of the application.
- `rdbms/`: Contains core logic for the RDBMS.
- `tests/`: Unit tests for the project.
-->

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
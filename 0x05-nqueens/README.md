# N-Queens Solver

Welcome to the N-Queens Solver! This Python script solves the N-Queens problem, which is the challenge of placing N non-attacking queens on an N×N chessboard. The program prints every possible solution to the problem, with one solution per line.

## Usage

To use the N-Queens Solver, run the script from the command line with the desired value for N:

```bash
python nqueens.py N
```

Replace `N` with an integer greater than or equal to 4. The program will print each solution to the N-Queens problem on a new line.

## Input Validation

The script performs input validation to ensure that the user provides the correct arguments:

- If the user calls the program with the wrong number of arguments, it prints:

  ```bash
  Usage: nqueens N
  ```

  and exits with status 1.

- If N is not an integer, it prints:

  ```bash
  N must be a number
  ```

  and exits with status 1.

- If N is smaller than 4, it prints:

  ```bash
  N must be at least 4
  ```

  and exits with status 1.

## Example

```bash
python nqueens.py 4
```

Output:

```
.Q..
...Q
Q...
..Q.

..Q.
Q...
...Q
.Q..

```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it according to your needs. See the [LICENSE](LICENSE) file for details.
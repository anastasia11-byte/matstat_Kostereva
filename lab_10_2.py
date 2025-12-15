def write_a_file(filename: str, lines: int = 9) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        for i in range(1, lines + 1):
            f.write("a" * i + "\n")

def main() -> None:
    filename = input("Enter output filename (e.g., a9.txt): ").strip()
    if not filename:
        filename = "a9.txt"

    write_a_file(filename, 9)
    print(f"Created file '{filename}' with 9 lines of 'a'.")

if __name__ == "__main__":
    main()
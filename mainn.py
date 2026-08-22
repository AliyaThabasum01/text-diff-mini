from difflib import unified_diff


file1 = input("First file: ")
file2 = input("Second file: ")

try:
    with open(file1, "r", encoding="utf-8") as f:
        old = f.readlines()

    with open(file2, "r", encoding="utf-8") as f:
        new = f.readlines()

    changes = list(
        unified_diff(
            old,
            new,
            fromfile=file1,
            tofile=file2
        )
    )

    print("\n📝 Text Diff")
    print("=" * 40)

    if changes:
        print("".join(changes))
    else:
        print("✅ Files are identical.")

except FileNotFoundError:
    print("❌ One of the files was not found.")

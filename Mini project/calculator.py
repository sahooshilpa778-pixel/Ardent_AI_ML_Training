# ╔══════════════════════════════════════════════════╗
# ║           CALC//STUDIO  — Python Edition         ║
# ╚══════════════════════════════════════════════════╝

from statistics import mean, median, mode, multimode

# ─── Helpers ────────────────────────────────────────
def separator():
    print("\n" + "─" * 45)

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ✗ Invalid number. Try again.")

def get_numbers(prompt="Enter numbers (comma-separated): "):
    while True:
        raw = input(prompt)
        try:
            nums = [float(x.strip()) for x in raw.split(",") if x.strip()]
            if not nums:
                raise ValueError
            return nums
        except ValueError:
            print("  ✗ Enter valid numbers separated by commas.")

def fmt(n):
    """Format: show int if whole, else up to 6 decimal places."""
    return int(n) if isinstance(n, float) and n.is_integer() else round(n, 6)

# ─── Menus ──────────────────────────────────────────
def basic_calc():
    separator()
    print("  BASIC CALCULATOR  (+  −  ×  ÷  %)")
    separator()
    a = get_float("  Enter first number  : ")
    print("  Operations: +  -  *  /  %")
    op = input("  Choose operation    : ").strip()
    b = get_float("  Enter second number : ")

    ops = {
        "+": ("Addition",       lambda x, y: x + y),
        "-": ("Subtraction",    lambda x, y: x - y),
        "*": ("Multiplication", lambda x, y: x * y),
        "/": ("Division",       lambda x, y: x / y if y != 0 else None),
        "%": ("Percentage",     lambda x, y: (x / 100) * y),
    }

    if op not in ops:
        print(f"\n  ✗ Unknown operator '{op}'")
        return

    name, fn = ops[op]
    result = fn(a, b)
    if result is None:
        print("\n  ✗ Error: Division by zero!")
    else:
        print(f"\n  {fmt(a)} {op} {fmt(b)}  =  {fmt(result)}  [{name}]")

def stats_calc():
    separator()
    print("  STATISTICS CALCULATOR")
    separator()
    nums = get_numbers("  Enter numbers (comma-separated): ")

    m  = mean(nums)
    md = median(nums)
    modes = multimode(nums)
    total = sum(nums)
    count = len(nums)

    print(f"""
  ┌────────────────────────────────────┐
  │  Count   : {str(count):<26}│
  │  Sum     : {str(fmt(total)):<26}│
  │  Mean    : {str(fmt(m)):<26}│
  │  Average : {str(fmt(m)):<26}│  (same as mean)
  │  Median  : {str(fmt(md)):<26}│
  │  Mode    : {str([fmt(x) for x in modes] if len(modes) > 1 else fmt(modes[0])):<26}│
  │  Min     : {str(fmt(min(nums))):<26}│
  │  Max     : {str(fmt(max(nums))):<26}│
  │  Range   : {str(fmt(max(nums)-min(nums))):<26}│
  └────────────────────────────────────┘""")

def pct_calc():
    separator()
    print("  PERCENTAGE CALCULATOR")
    separator()
    print("  [1] X% of Y")
    print("  [2] % Change from X to Y")
    print("  [3] X is what % of Y?")
    print("  [4] Add X% to Y")
    print("  [5] Remove X% from Y")
    choice = input("\n  Choose [1-5]: ").strip()

    if choice == "1":
        p = get_float("  Enter % (X): ")
        y = get_float("  Enter value (Y): ")
        print(f"\n  {fmt(p)}% of {fmt(y)}  =  {fmt((p/100)*y)}")

    elif choice == "2":
        x = get_float("  Original value (X): ")
        y = get_float("  New value (Y): ")
        if x == 0:
            print("\n  ✗ Original value cannot be zero.")
        else:
            change = ((y - x) / abs(x)) * 100
            direction = "increase" if change >= 0 else "decrease"
            print(f"\n  % Change: {fmt(abs(change))}% {direction}")

    elif choice == "3":
        x = get_float("  Enter X: ")
        y = get_float("  Enter Y: ")
        if y == 0:
            print("\n  ✗ Y cannot be zero.")
        else:
            print(f"\n  {fmt(x)} is {fmt((x/y)*100)}% of {fmt(y)}")

    elif choice == "4":
        y = get_float("  Enter value (Y): ")
        p = get_float("  Enter % to add (X): ")
        print(f"\n  {fmt(y)} + {fmt(p)}%  =  {fmt(y * (1 + p/100))}")

    elif choice == "5":
        y = get_float("  Enter value (Y): ")
        p = get_float("  Enter % to remove (X): ")
        print(f"\n  {fmt(y)} − {fmt(p)}%  =  {fmt(y * (1 - p/100))}")

    else:
        print("  ✗ Invalid choice.")

# ─── Main Loop ──────────────────────────────────────
def main():
    print("""
╔══════════════════════════════════════════════╗
║            C A L C // S T U D I O           ║
║         Basic · Statistical · Percent       ║
╚══════════════════════════════════════════════╝""")

    while True:
        print("""
  MAIN MENU
  ─────────────────────────────────────
  [1]  Basic Calculator  (+ − × ÷ %)
  [2]  Statistics        (mean/median/mode/avg)
  [3]  Percentage        (%, change, add/remove)
  [0]  Exit
  ─────────────────────────────────────""")

        choice = input("  Choose [0-3]: ").strip()

        if choice == "1":
            basic_calc()
        elif choice == "2":
            stats_calc()
        elif choice == "3":
            pct_calc()
        elif choice == "0":
            print("\n  Goodbye! ✓\n")
            break
        else:
            print("  ✗ Invalid option. Enter 0, 1, 2, or 3.")

if __name__ == "__main__":
    main()

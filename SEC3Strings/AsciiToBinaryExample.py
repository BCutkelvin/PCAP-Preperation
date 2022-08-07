def make_bitseq(s: str) -> str:
    if not s.isascii():
        raise ValueError("ASCII only allowed")
    return " ".join(f"{ord(i):08b}" for i in s)


print(f'\nmake_bitseq("bits"): {make_bitseq("bits")}')
print(f'make_bitseq("CAPS"): {make_bitseq("CAPS")}')
print(f'make_bitseq("$25.43"): {make_bitseq("$25.43")}')
print(f'make_bitseq("~5"): {make_bitseq("~5")}')



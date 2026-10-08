def check_dna(seq):
    """Проверяет корректность последовательности ДНК."""
    seq = seq.upper().replace(" ", "").replace("\n", "")
    
    # Проверка на допустимые символы
    valid = set("ATGC")
    if not set(seq).issubset(valid):
        bad = set(seq) - valid
        return None, f"Недопустимые символы: {', '.join(bad)}"
    
    # Проверка на чётность длины (две цепи)
    if len(seq) % 2 != 0:
        return None, "Длина последовательности нечётная — не может быть двух цепей"
    
    # Разделяем на две цепи
    half = len(seq) // 2
    strand1 = seq[:half]
    strand2 = seq[half:]
    
    # Проверка комплементарности с учётом антипараллельности
    # Вторая цепь должна быть комплементарна первой и развёрнута на 180°
    complement = {"A": "T", "T": "A", "G": "C", "C": "G"}
    
    # Ожидаемая вторая цепь: комплемент первой, записанный в обратном порядке
    expected_strand2 = "".join(complement[n] for n in reversed(strand1))
    
    if strand2 != expected_strand2:
        return None, "Нарушена комплементарность или антипараллельность"
    
    return (strand1, strand2), None


def count_nucleotides(seq):
    """Считает количество каждого нуклеотида."""
    counts = {n: seq.count(n) for n in "ATGC"}
    return counts


def main():
    print("Введите последовательность ДНК (например, ATGCATGC или две цепи подряд):")
    seq = input("> ").strip()
    
    result, error = check_dna(seq)
    if error:
        print(f"Ошибка: {error}")
        return
    
    strand1, strand2 = result
    print(f"\nЦепь 1 (5'->3'): {strand1}")
    print(f"Цепь 2 (3'->5'): {strand2}")
    
    # Считаем нуклеотиды в обеих цепях
    full = strand1 + strand2
    counts = count_nucleotides(full)
    
    print("\nКоличество нуклеотидов во всей молекуле:")
    total = 0
    for n, c in counts.items():
        print(f"  {n}: {c}")
        total += c
    print(f"  Всего: {total}")
    
    # Дополнительно: по каждой цепи отдельно
    print("\nПо цепям отдельно:")
    for i, strand in enumerate([strand1, strand2], 1):
        c = count_nucleotides(strand)
        print(f"  Цепь {i}: A={c['A']}, T={c['T']}, G={c['G']}, C={c['C']}")


if __name__ == "__main__":
    main()
def has_common(l, h):
    if l > h:
        l, h = h, l
    for n in range(2, l + 1):
        if l % n == 0 and h % n == 0:
            return True
    return False


def primitive_triplets(number_in_triplet):
    result = []
    if number_in_triplet % 4 != 0:
        raise ValueError("bad value")
    else:
        for n in range(1, number_in_triplet // 2):
            for m in range(n, number_in_triplet):
                if 2 * n * m == number_in_triplet:
                    if m == n:
                        continue
                    elif has_common(m, n):
                        continue
                    candidate = [m**2 - n ** 2, 2 * m * n, m**2 + n**2]
                    candidate.sort()
                    result.insert(
                        0, (candidate[0], candidate[1], candidate[2]))
    return set(result)


def triplets_in_range(range_start, range_end):
    result = []
    if range_start < 1:
        range_start = 1
    for i in range(range_start, range_end - 1):
        for j in range(i + 1, range_end):
            for k in range(j + 1, range_end + 1):
                if i ** 2 + j ** 2 > k ** 2:
                    continue
                elif i ** 2 + j ** 2 == k ** 2:
                    result.append((i, j, k))
                else:
                    break
    return set(result)


def is_triplet(triplet):
    triplet = list(triplet)
    triplet.sort()
    return triplet[0] ** 2 + triplet[1] ** 2 == triplet[2] ** 2

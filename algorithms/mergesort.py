def td_sort(a, aux, low, high):
    if high <= low: return
    mid = low + (high - low) / 2
    td_sort(a, aux, low, mid) 
    td_sort(a, aux, mid + 1, high)
    merge(a, aux, low, mid, high)

def bu_sort(a, low, mid, high):
    i = 1
    N = len(a)
    aux = list(a)
    while i < N:
        j = 0
        while j < N - i:
            merge(a, aux, j, j + i - 1, min(j + i + i - 1, N-1))
            j += i + i
        i += i

def merge(a, aux, low, mid, high):
    for i in range(low, high + 1):
        aux[i] = a[i]

    i = low
    j = mid + 1

    for k in range(low, high + 1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > high:
                a[k] = aux[i]
                i += 1
        elif aux[j] < aux[i]:
                a[k] = aux[j]
                j += 1
        else:
            a[k] = aux[i]
            i += 1

def topdown(data):
    td_sort(data, list(data), 0, len(data) -1)

def bottomup(data):
    bu_sort(data, 0, len(data)/3, len(data)/2)

if __name__ == "__main__":
    a = [99, 543, 32, 87, 39, 46, 47]
    print 'pre top down sort', a
    topdown(a)
    print 'post top down sort', a

    b = [54, 23, 787, 0, 43, 12, 56, 78]
    print 'pre bottom up sort', b
    bottomup(b)
    print 'post bottom up sort', b

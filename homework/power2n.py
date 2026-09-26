import time

# 方法 1: 直接次方的運算 (Direct exponentiation)
def power2n_1(n):
    return 2**n


# 方法 2a: 用遞迴 (樹狀雙重遞迴 Tree recursion)
def power2n_2a(n):
    if n == 0:
        return 1
    return power2n_2a(n - 1) + power2n_2a(n - 1)


# 方法 2b: 用遞迴 (單一遞迴 Linear recursion)
def power2n_2b(n):
    if n == 0:
        return 1
    return 2 * power2n_2b(n - 1)


# 方法 3: 用遞迴 + 查表 (Memoization / 動態規劃)
memo = {}


def power2n_3(n):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1

    # 依題目要求使用 power2n(n-1) + power2n(n-1) 結構，配合 Memoization 記錄中間結果
    memo[n] = power2n_3(n - 1) + power2n_3(n - 1)
    return memo[n]


# 效能測試與比較
def benchmark(n_value=25):
    print(f"=== 效能測試比較 (N = {n_value}) ===")

    # 測量 方法 1
    start = time.perf_counter()
    res1 = power2n_1(n_value)
    t1 = time.perf_counter() - start
    print(f"[方法 1] 內建運算子 : {t1:.8f} 秒")

    # 測量 方法 2a
    start = time.perf_counter()
    res2a = power2n_2a(n_value)
    t2a = time.perf_counter() - start
    print(f"[方法 2a] 樹狀雙重遞迴: {t2a:.8f} 秒")

    # 測量 方法 2b
    start = time.perf_counter()
    res2b = power2n_2b(n_value)
    t2b = time.perf_counter() - start
    print(f"[方法 2b] 單線條遞迴 : {t2b:.8f} 秒")

    # 測量 方法 3
    global memo
    memo = {}  # 清空快取
    start = time.perf_counter()
    res3 = power2n_3(n_value)
    t3 = time.perf_counter() - start
    print(f"[方法 3] 遞迴 + 查表 : {t3:.8f} 秒")

    # 驗證結果是否一致
    assert res1 == res2a == res2b == res3
    print("\n所有方法計算結果一致！")


if __name__ == "__main__":
    benchmark(25)

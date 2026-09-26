# 遞迴關係式與主定理 (Master Theorem) 分析指南

本文件收錄了演算法中常見遞迴關係式的精確數學推導，以及如何運用主定理（Master Theorem）快速判斷分治法（Divide and Conquer）的時間複雜度。

## 習題 2：四個遞迴方程式的精確求解與 Big O

### 1. $T(n) = T(n-1) + 8, \quad T(1) = 1$

* **展開推導**：
  

  $$
  \begin{aligned}   T(n) &= T(n-1) + 8 \\   &= T(n-2) + 2 \times 8 \\   &= T(n-k) + k \times 8   \end{aligned}
  $$

  
  令 $n - k = 1 \implies k = n - 1$：
  

  $$
  T(n) = T(1) + 8(n-1) = 1 + 8n - 8 = 8n - 7
  $$

* **精確解**：$T(n) = 8n - 7$

* **時間複雜度**：$\mathcal{O}(n)$

### 2. $T(n) = 2T(n-1) + 9, \quad T(1) = 1$

* **展開推導**：
  

  $$
  \begin{aligned}   T(n) &= 2T(n-1) + 9 \\   &= 2^2 T(n-2) + 2 \times 9 + 9 \\   &= 2^k T(n-k) + 9 \sum_{i=0}^{k-1} 2^i   \end{aligned}
  $$

  
  令 $n - k = 1 \implies k = n - 1$，並套用等比級數求和 $\sum_{i=0}^{n-2} 2^i = 2^{n-1} - 1$：
  

  $$
  T(n) = 2^{n-1} (1) + 9(2^{n-1} - 1) = 10 \cdot 2^{n-1} - 9 = 5 \cdot 2^n - 9
  $$

* **精確解**：$T(n) = 5 \cdot 2^n - 9$

* **時間複雜度**：$\mathcal{O}(2^n)$

### 3. $T(n) = 2T(n/2) + 1, \quad T(1) = 1$

* **展開推導**（設 $n = 2^k \implies k = \log_2 n$）：
  

  $$
  \begin{aligned}   T(n) &= 2T(n/2) + 1 \\   &= 2^2 T(n/2^2) + 2 + 1 \\   &= 2^k T(n/2^k) + \sum_{i=0}^{k-1} 2^i   \end{aligned}
  $$

  
  代入 $k = \log_2 n$：
  

  $$
  T(n) = 2^{\log_2 n} T(1) + (2^{\log_2 n} - 1) = n \cdot 1 + (n - 1) = 2n - 1
  $$

* **精確解**：$T(n) = 2n - 1$

* **時間複雜度**：$\mathcal{O}(n)$

### 4. $T(n) = T(n/2) + 1, \quad T(1) = 1$

* **展開推導**（設 $n = 2^k \implies k = \log_2 n$）：
  

  $$
  \begin{aligned}   T(n) &= T(n/2) + 1 \\   &= T(n/2^2) + 2 \\   &= T(n/2^k) + k   \end{aligned}
  $$

  
  代入 $k = \log_2 n$：
  

  $$
  T(n) = T(1) + \log_2 n = \log_2 n + 1
  $$

* **精確解**：$T(n) = \log_2 n + 1$

* **時間複雜度**：$\mathcal{O}(\log n)$

## 總結對照表

| 遞迴關係式 | 精確解 $T(n)$ | Big O 複雜度 | 代表性演算法 / 應用 | 
 | ----- | ----- | ----- | ----- | 
| $T(n) = T(n-1) + 8$ | $8n - 7$ | $\mathcal{O}(n)$ | 單層迴圈 / 線性搜尋 | 
| $T(n) = 2T(n-1) + 9$ | $5 \cdot 2^n - 9$ | $\mathcal{O}(2^n)$ | 樹狀雙重遞迴 / 河內塔 | 
| $T(n) = 2T(n/2) + 1$ | $2n - 1$ | $\mathcal{O}(n)$ | 二元樹節點遍歷 | 
| $T(n) = T(n/2) + 1$ | $\log_2 n + 1$ | $\mathcal{O}(\log n)$ | 二分搜尋法 (Binary Search) | 

## 主定理 (Master Theorem) 快速速查

適用於標準分治遞迴式：

$$
T(n) = a T\left(\frac{n}{b}\right) + f(n)
$$

比較項：$n^{\log_b a}$（葉子節點數）與 $f(n)$（額外工作量）

1. **Case 1**: 若 $f(n) = \mathcal{O}\left(n^{\log_b a - \epsilon}\right)$ $\implies \mathbf{T(n) = \Theta\left(n^{\log_b a}\right)}$

2. **Case 2**: 若 $f(n) = \Theta\left(n^{\log_b a}\right)$ $\implies \mathbf{T(n) = \Theta\left(n^{\log_b a} \log n\right)}$

3. **Case 3**: 若 $f(n) = \Omega\left(n^{\log_b a + \epsilon}\right)$ 且滿足正則條件 $\implies \mathbf{T(n) = \Theta(f(n))}$
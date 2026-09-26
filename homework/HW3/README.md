# 系統性列舉真值表解決 SAT 問題 (Truth Table Enumeration SAT Solver)

本專案為針對 **布林可滿足性問題 (Boolean Satisfiability Problem, SAT)** 實作的暴力列舉法 (Brute-force Search / Truth Table Enumeration) 求解器。

## SAT 問題簡介

SAT 問題是第一個被證明為 **NP-Complete** 的經典電腦科學問題。給定一個包含布林變數及邏輯運算子（AND、OR、NOT 等）的邏輯表達式，詢問是否存在至少一組變數賦值（True/False），使得整個表達式的計算結果為 **True**。

* **Satisfiable (可滿足)**：存在至少一組解使公式為 True。
* **Unsatisfiable (不可滿足)**：不論變數如何組合，公式恆為 False。

---

## 演算法實作說明

本程式採用 **真值表系統化窮舉 (Truth Table Enumeration)** 策略：

1. **變數提取**：解析輸入的邏輯字串，自動辨識出 $n$ 個獨立的布林變數。
2. **空間列舉**：利用 Python 的 `itertools.product([True, False], repeat=n)` 生成大小為 $2^n$ 的完整賦值狀態空間。
3. **邏輯求值**：逐一將 $2^n$ 種變數組合代入邏輯運算式求值。
4. **結果輸出**：排版印出完整真值表，並列出所有可滿足解（Satisfying Assignments）。

---

## 時間與空間複雜度分析

* **時間複雜度**：$\mathcal{O}(2^n \cdot m)$
  * 其中 $n$ 為布林變數數量，$m$ 為邏輯算式的長度。
  * 每增加一個變數，狀態空間翻倍，展現經典的**指數型爆發 (Exponential Time)**。
* **空間複雜度**：$\mathcal{O}(2^n + n)$
  * 儲存 $2^n$ 列真值表紀錄。

---

## 執行與使用方式

執行 Python 程式檔即可看到內建測試集的真值表與 SAT 判定結果：

```bash
python sat_solver.py
```

### 支援語法表

| 邏輯運算 | 支援符號 | 範例 |
| :--- | :--- | :--- |
| **AND** | `&`, `and` | `A & B` |
| **OR** | `\|`, `or` | `A \| B` |
| **NOT** | `~`, `!`, `not` | `~A` |
| **Implication (蘊含)** | `->` | `P -> Q` |
| **Group (優先權)** | `( )` | `(A \| B) & C` |

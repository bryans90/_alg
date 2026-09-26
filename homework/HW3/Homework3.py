import itertools
import re


class SATSolver:

    def __init__(self, expression_str):
        """初始化 SAT 求解器

        支援的邏輯運算子：
        - AND: &, and
        - OR: |, or
        - NOT: ~, not, !
        - IMPLIES: ->
        - EQUIVALENCE: <->
        """
        self.raw_expression = expression_str
        self.parsed_expression = self._preprocess_expression(expression_str)
        self.variables = self._extract_variables()

    def _preprocess_expression(self, expr):
        """將常見邏輯符號轉換為 Python 可執行的表達式"""
        # 替換雙向條件 (Equivalence) A <-> B => (A and B) or (not A and not B)
        # 為簡化，使用 Python 的 == (對布林值而言等價於邏輯等價)
        expr = expr.replace("<->", "==")

        # 替換蘊含 (Implication) A -> B => (not A or B)
        # 用正則處理簡單的 A -> B 模式
        while "->" in expr:
            expr = re.sub(r"(\w+)\s*->\s*(\w+)", r"(not \1 or \2)", expr)

        # 替換符號為 Python 運算子
        expr = expr.replace("~", " not ")
        expr = expr.replace("!", " not ")
        expr = expr.replace("&", " and ")
        expr = expr.replace("|", " or ")

        return expr

    def _extract_variables(self):
        """從表達式中提取所有變數名稱（排除 Python 關鍵字）"""
        keywords = {"and", "or", "not", "True", "False"}
        tokens = re.findall(r"\b[a-zA-Z_]\w*\b", self.parsed_expression)
        vars_set = sorted(
            list(set(token for token in tokens if token not in keywords))
        )
        return vars_set

    def solve_truth_table(self):
        """系統性窮舉真值表（Brute-force Truth Table Enumeration）

        回傳：
        - truth_table: 完整的真值表結果
        - satisfying_assignments: 使公式為真的解 (Satisfying Assignments)
        """
        n = len(self.variables)
        truth_table = []
        satisfying_assignments = []

        # 窮舉 2^n 種可能的布林組合 (True/False)
        for combination in itertools.product([True, False], repeat=n):
            assignment = dict(zip(self.variables, combination))

            try:
                # 在給定變數賦值環境下計算邏輯式的值
                result = bool(eval(self.parsed_expression, {}, assignment))
            except Exception as e:
                raise ValueError(
                    f"邏輯運算式語法錯誤: {e}\n解析後結果為: {self.parsed_expression}"
                )

            truth_table.append((assignment, result))
            if result:
                satisfying_assignments.append(assignment)

        return truth_table, satisfying_assignments

    def print_truth_table(self):
        """印出美麗排版的真值表與 SAT 解驗證"""
        truth_table, satisfying_assignments = self.solve_truth_table()

        print(f"\n原邏輯式: {self.raw_expression}")
        print(f"解析算式: {self.parsed_expression}")
        print(f"辨識變數: {self.variables}\n")

        # 表頭
        header = " | ".join(self.variables) + " || Result "
        print("-" * len(header))
        print(header)
        print("-" * len(header))

        # 表格內容
        for assignment, res in truth_table:
            row_str = " | ".join(
                f"{'T' if assignment[v] else 'F':^{len(v)}}"
                for v in self.variables
            )
            res_str = "T" if res else "F"
            print(f"{row_str} ||   {res_str}")

        print("-" * len(header))

        # 輸出 SAT 判定結果
        if satisfying_assignments:
            print(
                f"\n[結論] SATISFIABLE (可滿足)！找到 {len(satisfying_assignments)} 組解："
            )
            for idx, sol in enumerate(satisfying_assignments, 1):
                sol_formatted = ", ".join(
                    f"{k}={'True' if v else 'False'}" for k, v in sol.items()
                )
                print(f"  解 {idx}: {sol_formatted}")
        else:
            print("\n[結論] UNSATISFIABLE (不可滿足)！無任何賦值能使結果為 True。")


def main():
    print("=== 系統性真值表窮舉 SAT 求解器 (Truth Table Enumeration) ===")
    print("支援語法說明：")
    print("  - AND: & 或 and")
    print("  - OR : | 或 or")
    print("  - NOT: ~ 或 ! 或 not")
    print("  - 蘊含 (Implication) : ->")
    print("  - 括號 : ( )")
    print("範例邏輯式: (A | B) & (~A | C) & (B | C)\n")

    # 內建測試範例
    test_cases = [
        "(A | B) & (~A | B)",  # Satisfiable
        "(A & ~A)",  # Unsatisfiable
        "(P -> Q) & P & ~Q",  # Unsatisfiable (Modus Ponens 矛盾測試)
        "(A | B | C) & (~A | ~B) & (B | C)",  # Satisfiable
    ]

    print("--- 執行內建測試範例 ---")
    for expr in test_cases:
        solver = SATSolver(expr)
        solver.print_truth_table()
        print("\n" + "=" * 50)


if __name__ == "__main__":
    main()

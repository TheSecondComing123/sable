class Var:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Variable({self.name})"


class Equation:
    def __init__(self, lhs: BinaryOp, rhs: float) -> None:
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self) -> str:
        return f"{self.lhs} == {self.rhs}"


class Op:
    def __init__(self, name: str, arity: int) -> None:
        self.name = name
        self.arity = arity

    def __repr__(self) -> str:
        return f"Op({self.name}, arity={self.arity})"


class BinaryOp(Op):
    def __init__(self, name: str) -> None:
        super().__init__(name, 2)

    def __eq__(self, other: float) -> Equation:
        return Equation(self, other)


class Add(BinaryOp):
    def __init__(self, left: Var | float, right: Var | float) -> None:
        super().__init__("Add")
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Add({self.left}, {self.right})"


class Sub(BinaryOp):
    def __init__(self, left: Var | float, right: Var | float) -> None:
        super().__init__("Sub")
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Sub({self.left}, {self.right})"


class Mul(BinaryOp):
    def __init__(self, left: Var | float, right: Var | float) -> None:
        super().__init__("Mul")
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Mul({self.left}, {self.right})"


class Div(BinaryOp):
    def __init__(self, left: Var | float, right: Var | float) -> None:
        super().__init__("Div")
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Div({self.left}, {self.right})"


def solve(equation: Equation) -> float:
    match equation.lhs:
        case Add(left=Var(), right=int() | float() as right):
            return equation.rhs - right
        case Add(left=int() | float() as left, right=Var()):
            return equation.rhs - left
        case Sub(left=Var(), right=int() | float() as right):
            return equation.rhs + right
        case Sub(left=int() | float() as left, right=Var()):
            return left - equation.rhs
        case Mul(left=Var(), right=int() | float() as right):
            return equation.rhs / right
        case Mul(left=int() | float() as left, right=Var()):
            return equation.rhs / left
        case Div(left=Var(), right=int() | float() as right):
            return equation.rhs * right
        case Div(left=int() | float() as left, right=Var()):
            return left / equation.rhs
        case _:
            raise NotImplementedError(f"Cannot solve {equation}")


if __name__ == "__main__":
    equation = Mul(Var("x"), 2) == 4
    print(solve(equation))

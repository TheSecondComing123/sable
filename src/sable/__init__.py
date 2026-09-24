class Var:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Variable({self.name})"


class Number:
    def __init__(self, value: float) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"Number({self.value})"


class Equation:
    def __init__(self, lhs: BinaryOp, rhs: Number) -> None:
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

    def __eq__(self, other: Number) -> Equation:
        return Equation(self, other)


class Add(BinaryOp):
    def __init__(self, left: Var | Number, right: Var | Number) -> None:
        super().__init__("Add")
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Add({self.left}, {self.right})"


class Sub(BinaryOp):
    def __init__(self, left: Var | Number, right: Var | Number) -> None:
        super().__init__("Sub")
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Sub({self.left}, {self.right})"


class Mul(BinaryOp):
    def __init__(self, left: Var | Number, right: Var | Number) -> None:
        super().__init__("Mul")
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Mul({self.left}, {self.right})"


class Div(BinaryOp):
    def __init__(self, left: Var | Number, right: Var | Number) -> None:
        super().__init__("Div")
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Div({self.left}, {self.right})"


def solve(equation: Equation) -> float:
    rhs = equation.rhs.value
    match equation.lhs:
        case Add(left=Var(), right=Number(value=right)):
            return rhs - right
        case Add(left=Number(value=left), right=Var()):
            return rhs - left
        case Sub(left=Var(), right=Number(value=right)):
            return rhs + right
        case Sub(left=Number(value=left), right=Var()):
            return left - rhs
        case Mul(left=Var(), right=Number(value=right)):
            return rhs / right
        case Mul(left=Number(value=left), right=Var()):
            return rhs / left
        case Div(left=Var(), right=Number(value=right)):
            return rhs * right
        case Div(left=Number(value=left), right=Var()):
            return left / rhs
        case _:
            raise NotImplementedError(f"Cannot solve {equation}")


if __name__ == "__main__":
    equation = Mul(Var("x"), Number(2)) == Number(4)
    print(solve(equation))

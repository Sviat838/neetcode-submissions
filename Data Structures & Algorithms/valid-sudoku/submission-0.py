class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x = 0
        y = 0

        if not self.is_unique(board):
            return False

        while y < 9 and x < 9:
            new_part = list()

            while y % 3 != 0 or y == 0:
                new_part.extend(board[y][x:x + 3])
                y += 1
                if y % 3 == 0:
                    if not self.is_unique_list(new_part):
                        return False

            if x > 8 and y < 8:
                y += 3
                x = 0
            elif x < 8:
                x += 3
                y = 0

        return True

    def is_unique(self, part: List[List[str]]):

        for y in range(len(part)):
            x_temp = set()
            x_dots = 0
            y_temp = set()
            y_dots = 0

            for x in range(len(part[0])):
                if part[y][x] == '.':
                    x_dots += 1
                else:
                    x_temp.add(int(part[y][x]))

                if part[x][y] == '.':
                    y_dots += 1
                else:
                    y_temp.add(int(part[x][y]))

            if len(x_temp) + x_dots != len(part[0]) or len(y_temp) + y_dots != len(part):
                return False

        return True

    def is_unique_list(self, s):
        dots = 0
        res = set()

        for e in s:
            if e == '.':
                dots += 1
            else:
                res.add(e)

        return len(s) == dots + len(res)



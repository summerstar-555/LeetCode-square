# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        思路：
        先检查横的下一个字符是否为1，再检查纵向的字符是否为1，如果不是，不计算那个多出的字符，count = count + 1
        那么设置循环，循环条件 =
        """
        count = 0
        # 遍历所有元素查找字符‘1’，如果没有返回0
        for i in matrix:
            for j in range(i.count()):
                if i[j] == '1':        # 发现元素“1”
                    # 找横向“1”
                    if i[j + 1] == '1' and i + 1[j] == '1':
                        count = count + 1
        return count


s = Solution()
nums = s.maximalSquare(
    [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]])
print(nums)



def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

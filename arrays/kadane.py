class Kadane:
    def run(self, array):
        max_sum = float('-inf')
        current_sum = 0

        for num in array:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum
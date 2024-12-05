class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_length = len(start)
        
        start_index, target_index = 0, 0

        while start_index < start_length or target_index < start_length:
            
            # Skip underscores in the start string
            while start_index < start_length and start[start_index] == '_':
                start_index += 1
            
            # Skip underscores in the target string
            while target_index < start_length and target[target_index] == '_':
                target_index += 1

            # If either index reaches the end, both must reach at the same time
            if start_index == start_length or target_index == start_length:
                return start_index == start_length and target_index == start_length

            # Check conditions for 'L' and 'R' constraints or mismatched characters
            if (
                (start[start_index] == 'L' and start_index < target_index) or
                (start[start_index] != target[target_index]) or
                (start[start_index] == 'R' and start_index > target_index)
            ):
                return False

            # Move both indices forward
            start_index += 1
            target_index += 1

        return True

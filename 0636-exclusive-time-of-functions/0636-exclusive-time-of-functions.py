class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        time_tracker = [0] * n
        execution_stack = []
        checkpoint = 0
        
        for log_entry in logs:
            func_id, log_type, timestamp = map(str, log_entry.split(':'))
            func_id = int(func_id)
            timestamp = int(timestamp)
            
            if log_type == 'start':
                if execution_stack:
                    time_tracker[execution_stack[-1]] += timestamp - checkpoint
                execution_stack.append(func_id)
                checkpoint = timestamp
            else:
                time_tracker[execution_stack[-1]] += timestamp - checkpoint + 1
                execution_stack.pop()
                checkpoint = timestamp + 1
        
        return time_tracker
class Feedback:
    \"""
    Template for feedback mechanism to adjust strategies.
    Copy this file and modify for your feedback logic.
    \"""
    def record_trade(self, trade_result):
        \"""
        Record trade outcome and update internal state if needed.
        \"""
        raise NotImplementedError

    def adjust_strategy(self, strategy):
        \"""
        Adjust strategy parameters based on past performance.
        \"""
        raise NotImplementedError

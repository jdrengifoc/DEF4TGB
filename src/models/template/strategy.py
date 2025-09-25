class Strategy:
    \"""
    Template for a trading strategy.
    Copy this file and modify it for your own strategies.
    \"""
    def decide(self, market_data):
        \"""
        Implement your decision logic here.
        Return a dictionary with at least {'action': 'buy'/'sell', ...}
        \"""
        raise NotImplementedError

# src/interfaces/broker_interface.py
from abc import ABC, abstractmethod
from typing import Dict, Any, List


class BrokerInterface(ABC):
    """
    Abstract base class (ABC) for broker operations.
    All broker implementations must inherit from this interface.
    """

    @abstractmethod
    def connect(self, demo: bool = True) -> None:
        """Establish connection to the broker (demo or real)."""
        pass

    @abstractmethod
    def disconnect(self) -> None:
        """Close connection to the broker."""
        pass

    @abstractmethod
    def get_available_assets(self) -> List[str]:
        """Return list of tradable assets."""
        pass

    @abstractmethod
    def get_asset_info(self, asset: str) -> Dict[str, Any]:
        """
        Retrieve asset information such as:
        rollover, swap, margin, margin_level, commission,
        contract_value, pip, schedule, spread
        """
        pass

    @abstractmethod
    def get_data(self, asset: str, timeframe: str, window: int) -> Any:
        """Download initial or historical market data."""
        pass

    @abstractmethod
    def open_trade(self, asset: str, volume: float, trade_type: str,
                   tp: float = None, sl: float = None) -> str:
        """Open a new trade with optional TP/SL. Returns trade ID."""
        pass

    @abstractmethod
    def update_trade(self, trade_id: str, tp: float = None, sl: float = None) -> None:
        """Update TP/SL of an existing trade."""
        pass

    @abstractmethod
    def close_trade(self, trade_id: str) -> None:
        """Close an open trade."""
        pass

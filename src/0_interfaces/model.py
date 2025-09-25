# src/interfaces/model_interface.py
from abc import ABC, abstractmethod
from typing import Any, Dict


class ModelInterface(ABC):
    """
    Abstract base class (ABC) for trading models.
    Defines the structure for training, prediction, and decision-making.
    """

    @abstractmethod
    def train(self, data: Any, hyperparams: Dict[str, Any]) -> None:
        """
        Train or fit the model using historical data.
        - data: input dataset (e.g., price series, features)
        - hyperparams: configuration such as window_size, timeframe
        """
        pass

    @abstractmethod
    def predict(self, data: Any) -> Dict[str, Any]:
        """
        Make a prediction/forecast given input data.
        Returns:
            {
                "forecast": float | list,
                "confidence": float,
            }
        """
        pass

    @abstractmethod
    def decide(self, forecast: Dict[str, Any], asset_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert forecast into a trading decision.
        Returns:
            {
                "action": "buy" | "sell" | "hold",
                "price": float,
                "volume": float,
                "tp": float,
                "sl": float
            }
        """
        pass

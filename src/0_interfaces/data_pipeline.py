# src/interfaces/data_pipeline_interface.py
from abc import ABC, abstractmethod
from typing import Any, Dict


class DataPipelineInterface(ABC):
    """
    Abstract base class (ABC) for data lifecycle in trading systems.
    Defines the structure for downloading, updating, cleaning, and serving data.
    """

    @abstractmethod
    def download(self, window_size: int, timeframe: str) -> Any:
        """
        Download initial historical data.
        Args:
            window_size: number of data points (lookback period)
            timeframe: candle frequency (e.g., '1m', '1h', '1d')
        Returns:
            Historical dataset (e.g., DataFrame or list of dicts).
        """
        pass

    @abstractmethod
    def update(self, frequency: str, timeframe: str) -> Any:
        """
        Update the dataset with new incoming candles/ticks.
        Args:
            frequency: how often updates happen (e.g., every minute, hourly)
            timeframe: candle frequency
        Returns:
            Updated dataset.
        """
        pass

    @abstractmethod
    def clean(self, raw_data: Any) -> Any:
        """
        Clean raw data (e.g., handle NaNs, duplicates, formatting).
        Args:
            raw_data: unprocessed dataset
        Returns:
            Clean dataset ready for analysis.
        """
        pass

    @abstractmethod
    def get_data(self) -> Any:
        """
        Get the most recent cleaned dataset.
        Returns:
            Processed dataset ready for model input.
        """
        pass

    @abstractmethod
    def get_metadata(self) -> Dict[str, Any]:
        """
        Retrieve information about the dataset (e.g., timeframe, last update).
        Returns:
            Dictionary with dataset metadata.
        """
        pass

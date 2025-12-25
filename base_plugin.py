from abc import ABC, abstractmethod
from schema import DataEnvelope
from typing import List

class BaseInputPlugin(ABC):
    @abstractmethod
    def fetch_new_items(self, **kwargs) -> List[DataEnvelope]:
        """Scan a source and return new envelopes."""
        pass

class BaseTransformPlugin(ABC):
    @abstractmethod
    def process(self, envelope: DataEnvelope, **kwargs) -> DataEnvelope:
        """Modify the envelope content or metadata."""
        pass

class BaseOutputPlugin(ABC):
    @abstractmethod
    def deliver(self, envelope: DataEnvelope, **kwargs) -> bool:
        """Send the final data to its destination."""
        pass
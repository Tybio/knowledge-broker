from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class DataEnvelope:
    """The standard container for data moving through the Knowledge Broker."""
    source_path: str                 # Original file location
    filename: str                    # Base name without extension
    content: str = ""                # The primary text/md payload
    artifacts: List[str] = field(default_factory=list) # Supporting files (e.g., mp3s)
    metadata: Dict[str, Any] = field(default_factory=dict) # Flexible store for plugin-specific data
    pipeline_name: Optional[str] = None
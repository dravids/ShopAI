from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseLLMProvider(ABC):
    """Base interface for LLM providers.
    
    This class defines the contract that all LLM providers must implement.
    
    Attributes:
        model_name (str): Name of the LLM model being used
        temperature (float): Sampling temperature for generation
    """
    
    def __init__(self, model_name: str, temperature: float = 0.7):
        self.model_name = model_name
        self.temperature = temperature
    
    @abstractmethod
    async def generate(self, prompt: str) -> str:
        """Generate LLM response for a prompt.
        
        Args:
            prompt: Input text prompt
            
        Returns:
            Generated text response
        """
        pass
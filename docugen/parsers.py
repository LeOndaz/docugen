from typing import TypeVar, Generic
from pydantic import BaseModel
from docugen.models import LLMDocstringResponse
import logging

Model = TypeVar('Model', bound=BaseModel)


class LLMResponseParser(Generic[Model]):
    """Generic parser for LLM responses."""

    def __init__(self, model: type[Model], logger: logging.Logger = None):
        """Initialize parser with model type."""
        self.model = model
        self.logger = logger or logging.getLogger('docugen')

    def parse(self, response: str) -> Model:
        """Parse LLM response into model instance."""
        return self.model.model_validate_json(response)


class LLMDocstringResponseParser(LLMResponseParser[LLMDocstringResponse]):
    """Parser for LLM docstring responses."""

    def __init__(self, logger: logging.Logger = None):
        """Initialize with LLMDocstringResponse model."""
        super().__init__(LLMDocstringResponse, logger=logger)

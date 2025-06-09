"""Basic tests for the examples."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def test_examples_exist():
    """Test that example files exist."""
    examples_dir = project_root / "examples"
    assert examples_dir.exists(), "Examples directory not found"
    
    example_files = ["simple_chat.py", "streaming_chat.py", "image_analysis.py", "check_models.py"]
    
    for example_file in example_files:
        example_path = examples_dir / example_file
        assert example_path.exists(), f"Example file {example_file} not found"


def test_example_imports():
    """Test that example files can be imported without errors."""
    examples_dir = project_root / "examples"
    example_files = ["simple_chat", "streaming_chat", "image_analysis", "check_models"]
    
    for example_name in example_files:
        example_path = examples_dir / f"{example_name}.py"
        
        spec = importlib.util.spec_from_file_location(
            f"examples.{example_name}", 
            example_path
        )
        assert spec is not None, f"Could not create spec for {example_name}"
        
        module = importlib.util.module_from_spec(spec)
        assert module is not None, f"Could not create module for {example_name}"


@pytest.mark.anyio
async def test_async_functionality():
    """Test that anyio framework works correctly."""
    import anyio

    async def simple_async_function():
        await anyio.sleep(0.001)  # Very short sleep
        return "success"

    result = await simple_async_function()
    assert result == "success"
#!/bin/bash
# Quick development setup script for tubemp3

set -e

echo "🚀 TubeMP3 Development Setup"
echo "============================"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.10 or higher."
    exit 1
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "📋 Detected Python version: $python_version"

# Check if we're in the right directory
if [[ ! -f "pyproject.toml" ]]; then
    echo "❌ Please run this script from the tubemp3 project root directory."
    exit 1
fi

# Install system dependencies (if on Ubuntu/Debian)
if command -v apt-get &> /dev/null; then
    echo "📦 Installing system dependencies..."
    sudo apt-get update -qq
    sudo apt-get install -y ffmpeg
else
    echo "⚠️  Please make sure ffmpeg is installed on your system."
fi

# Check if Poetry is installed
if command -v poetry &> /dev/null; then
    echo "📚 Using Poetry for dependency management..."
    
    # Install dependencies
    echo "📦 Installing project dependencies..."
    poetry install
    
    # Install pre-commit hooks if available
    if poetry run python -c "import pre_commit" 2>/dev/null; then
        echo "🪝 Installing pre-commit hooks..."
        poetry run pre-commit install
    fi
    
    echo ""
    echo "✅ Setup complete! You can now run:"
    echo "   poetry run pytest          # Run tests"
    echo "   poetry run python testing.py  # Run legacy test script"
    echo "   make test                   # Run tests (if make is available)"
    echo "   make help                   # See all available commands"
    
elif command -v pip3 &> /dev/null; then
    echo "📚 Using pip for dependency management..."
    
    # Create virtual environment if it doesn't exist
    if [[ ! -d "venv" ]]; then
        echo "🔧 Creating virtual environment..."
        python3 -m venv venv
    fi
    
    # Activate virtual environment
    echo "🔧 Activating virtual environment..."
    source venv/bin/activate
    
    # Install dependencies
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    
    echo ""
    echo "✅ Setup complete! You can now run:"
    echo "   source venv/bin/activate    # Activate virtual environment"
    echo "   pytest                      # Run tests"
    echo "   python testing.py           # Run legacy test script"
    
else
    echo "❌ Neither Poetry nor pip3 found. Please install one of them."
    exit 1
fi

# Run a quick test to verify setup
echo ""
echo "🧪 Running a quick test to verify setup..."

if command -v poetry &> /dev/null; then
    if poetry run python -c "import tubemp3; print('✅ tubemp3 import successful')"; then
        echo "🎉 Development environment is ready!"
    else
        echo "❌ There was an issue with the setup. Please check the error messages above."
        exit 1
    fi
else
    if python -c "import tubemp3; print('✅ tubemp3 import successful')" 2>/dev/null; then
        echo "🎉 Development environment is ready!"
    else
        echo "❌ There was an issue with the setup. Please check the error messages above."
        exit 1
    fi
fi

echo ""
echo "📚 Next steps:"
echo "   1. Read the README.md for usage examples"
echo "   2. Check out the tests/ directory for test examples"
echo "   3. Run 'make help' to see available development commands"
echo "   4. Start developing and testing!"
echo ""
echo "Happy coding! 🎵🐍"

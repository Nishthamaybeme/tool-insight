#!/bin/bash

# Install Rust
curl https://sh.rustup.rs -sSf | sh -s -- -y
source "$HOME/.cargo/env"  # Ensure Rust is available

# Install Python dependencies
pip install -r requirements.txt

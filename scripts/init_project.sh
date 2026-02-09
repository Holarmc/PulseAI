#!/bin/bash

# --- Project Initialization Script: init_project.sh ---
#
# This script automates the creation of the robust GenAI/ADK
# project structure discussed.
#
# Usage:
# 1. Save this content to a file named 'scripts/init_project.sh'.
# 2. Make the script executable: chmod +x scripts/init_project.sh
# 3. Run it from your project root: ./scripts/init_project.sh
# ----------------------------------------------------

echo "🏗️ Starting project structure creation..."

# 1. Create top-level directories
mkdir -p data/{raw,processed,embeddings,vector_db,cache,outputs}
mkdir -p prompts/{system_instructions,few_shot_examples}
mkdir -p models/{trained,adapters,checkpoints,logs}
mkdir -p notebooks
mkdir -p src/{agents,tools,services,utils,evaluation,retrieval,chains,llm,prompt_engineering}
mkdir -p configs
mkdir -p tests
mkdir -p scripts # Ensures this folder exists if running externally

echo "📁 Top-level and sub-directories created."

# 2. Create placeholder files for structure visibility and initial setup

# Top Level
touch README.md
touch .Dockerfile
touch .env
touch .gitignore
touch pyproject.toml
touch run_agent.py

# Configs
touch configs/agent_config.yaml
touch configs/model_config.yaml
touch configs/tool_config.yaml
touch configs/rag_config.yaml

# src/__init__.py files to make them Python modules
touch src/__init__.py
touch src/agents/__init__.py
touch src/tools/__init__.py
touch src/services/__init__.py
touch src/utils/__init__.py
touch src/evaluation/__init__.py
touch src/retrieval/__init__.py
touch src/chains/__init__.py
touch src/llm/__init__.py
touch src/prompt_engineering/__init__.py

# Example src files (basic placeholders)
touch src/agents/coordinator_agent.py
touch src/tools/search_tool.py
touch src/utils/yaml_loader.py

# Scripts folder (this file is already here)
# touch scripts/deploy_cloud_run.sh # Can add this later

echo "📄 Initial placeholder files created."
echo "✅ Project structure generation complete."


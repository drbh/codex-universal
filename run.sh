#!/bin/bash
set -euo pipefail

echo "Starting run.sh as $(whoami) in $(pwd)"

# Clone repository
cd /tmp
REPO_NAME=$(basename "${REPO_URL}" .git)
echo "Cloning ${REPO_URL}..."
git clone "${REPO_URL}" 2>/dev/null || { echo "Clone failed"; exit 1; }

# Enter repo directory
cd "${REPO_NAME}"
echo "Repository cloned successfully"

# Install dependencies and run MCP client
pip install -q langchain-openai mcp-use
export OPENAI_API_KEY="${OPENAI_API_KEY}"
python /opt/mcpclient.py "${PROMPT}"

# Generate and display patch
git diff > /tmp/patch.diff
echo "================================================================================"
cat /tmp/patch.diff
echo "================================================================================"
# 🧪 Catalyst Project Makefile

# Set the default shell
SHELL := /bin/bash

# Define colors for output
GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
BLUE   := $(shell tput -Txterm setaf 4)
RESET  := $(shell tput -Txterm sgr0)

.DEFAULT_GOAL := help

# Phony targets don't represent files
.PHONY: help install setup-dev test lint format check run clean

help: ## ❓ Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  $(BLUE)%-15s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## 📦 Install project dependencies with Poetry
	@echo "$(GREEN)Installing dependencies using Poetry...$(RESET)"
	@poetry install --no-root

setup-dev: ## 🛠️  Add development tools like pytest and ruff
	@echo "$(GREEN)Adding development dependencies (pytest, ruff)...$(RESET)"
	@poetry add pytest ruff --group dev
	@echo "$(GREEN)Development tools added. Please commit the pyproject.toml and poetry.lock files.$(RESET)"

run: ## 🧪 Run the main application
	@echo "$(GREEN)Running the application...$(RESET)"
	@poetry run python src/cli/index.py

test: ## 🚦 Run tests with pytest
	@echo "$(GREEN)Running tests...$(RESET)"
	@poetry run pytest

lint: ## 🔍 Lint code with ruff
	@echo "$(GREEN)Linting code...$(RESET)"
	@poetry run ruff check src tests

format: ## ✨ Format code with ruff
	@echo "$(GREEN)Formatting code...$(RESET)"
	@poetry run ruff format src tests

check: lint ## ✅ Run all checks (linting)
	@echo "$(GREEN)All checks passed!$(RESET)"

clean: ## 🧹 Clean up temporary files
	@echo "$(YELLOW)Cleaning up temporary files...$(RESET)"
	@rm -f .coverage
	@rm -rf .pytest_cache
	@rm -rf .ruff_cache
	@rm -rf src/.ruff_cache
	@rm -rf tests/.ruff_cache
	@find . -type d -name "__pycache__" -exec rm -r {} +
	@echo "$(GREEN)Clean up complete.$(RESET)"

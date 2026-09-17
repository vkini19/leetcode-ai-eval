# LeetCode AI Eval

An evaluation framework for measuring how well AI models generate correct Python solutions to LeetCode-style coding problems.

The project is designed to evaluate coding models systematically rather than relying on a small number of manually inspected examples.

## Project Goal

The goal of this project is to answer:

> **How well can an AI model solve the LeetCode 75 problem set?**

The benchmark evaluates generated solutions against hidden test cases and records metrics such as:

- Test-case accuracy
- Whether the entire problem was solved
- Runtime
- Error type
- Error message

The framework is designed to eventually support multiple models and prompting strategies, allowing their coding performance to be compared under the same evaluation setup.

## Evaluation Methodology

Each problem follows this pipeline:

```text
Problem Dataset
      ↓
Problem Prompt
      ↓
AI Model Generates Code
      ↓
Isolated Code Execution
      ↓
Hidden Test Cases
      ↓
Evaluation Metrics
      ↓
Results JSON
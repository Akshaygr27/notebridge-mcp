# NoteBridge MCP

A simple **Model Context Protocol (MCP)** server built with Python and `fastmcp` that gives AI assistants basic note-taking, math calculation, and note-reading capabilities.

## Features

- **Tools (Actions)**
  - `add_note(note)`: Saves a short text note in memory.
  - `calculate(a, b, operation)`: Performs `add`, `subtract`, `multiply`, or `divide`.
- **Resources (Data)**
  - `notes://all`: Returns all saved notes.

## Project Structure

```text
notebridge-mcp/
├── server.py
└── README.md
import os
from fastmcp import FastMCP


mcp = FastMCP("QuickNotes")

NOTES_FILE = "my_notes.txt"

@mcp.tool()
def add_note(note: str) -> str:
    """Save a new note to the local text file."""
    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(f"- {note}\n")
    return f"Note saved: '{note}'"

@mcp.tool()
def get_notes() -> str:
    """Read all saved notes from the local text file."""
    if not os.path.exists(NOTES_FILE):
        return "No notes found yet."
    
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        content = f.read().strip()
        
    return content if content else "The notes file is empty."

@mcp.tool()
def clear_notes() -> str:
    """Delete all saved notes."""
    if os.path.exists(NOTES_FILE):
        os.remove(NOTES_FILE)
        return "All notes cleared."
    return "No notes file to clear."

if __name__ == "__main__":
    
    mcp.run()
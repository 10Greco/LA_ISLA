#!/usr/bin/env python3
"""
LA ISLA - Project Generator
Genera la estructura completa del proyecto

Uso: python3 generate_project.py
"""

import os
import sys
from pathlib import Path

def create_file(path: str, content: str):
    """Crea un archivo con contenido"""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding='utf-8')
    print(f"✓ {path}")

def main():
    base = Path("LA_ISLA")
    
    print("Generando estructura de LA ISLA...\n")
    
    # Crear carpetas base
    folders = [
        "Core/src/World",
        "Core/src/Simulation",
        "Core/src/Events",
        "Core/src/Validation",
        "Core/src/SaveSystem",
        "Core/src/Debug",
        "Core/src/Generation",
        "Core/src/People",
        "Core/src/Society",
        "Core/src/Economy",
        "Core/src/Health",
        "Core/src/Survival",
        "Core/src/Technology",
        "Core/src/Culture",
        "Core/src/Education",
        "Core/src/Generations",
        "Core/src/Ecology",
        "Core/src/Demographics",
        "Core/src/Disease",
        "Core/src/Gameplay",
        "Core/src/Narrative",
        "Core/src/AI",
        "Core/src/Time",
        "Tools/WorldSimulator",
        "Tests/Core",
        "Docs",
        ".github/workflows"
    ]
    
    for folder in folders:
        (base / folder).mkdir(parents=True, exist_ok=True)
    
    print("✓ Carpetas creadas\n")

if __name__ == "__main__":
    main()
    print("\nEstructura de carpetas lista.")
    print("Ahora copia los archivos de código en cada carpeta.")

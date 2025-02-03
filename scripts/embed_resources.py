#!/usr/bin/env python3

import argparse
from pathlib import Path

embedded_suffixes = {'.html', '.css', '.js'}

def process_directory(input_dir: Path, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    for file_path in input_dir.iterdir():
        if file_path.suffix in embedded_suffixes:
            var_name = file_path.name.replace('.', '_')
            header_file = output_dir / f"{file_path.stem}{file_path.suffix.replace('.', '_')}.h"
            generate_header(file_path, header_file, var_name)

def generate_header(file_path: Path, output_path: Path, var_name: str):
    if file_path.stat().st_mtime < output_path.stat().st_mtime:
        return

    with file_path.open('r', encoding="utf-8") as f:
        content = f.read()
    
    header_content = f"""#ifndef {var_name.upper()}_H
#define {var_name.upper()}_H

const char {var_name}[] = R"rawliteral({content})rawliteral";

#endif // {var_name.upper()}_H
"""
    
    with output_path.open("w", encoding="utf-8") as f:
        f.write(header_content)
        print(f"Generated: {output_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Embed text resources into C++ headers as string literals.")
    parser.add_argument('input_dir', type=Path, help="Input directory")
    parser.add_argument('output_dir', type=Path, help="Output directory for generated files")
    
    args = parser.parse_args()
    process_directory(args.input_dir, args.output_dir)

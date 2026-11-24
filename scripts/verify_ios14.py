#!/usr/bin/env python3
"""Check declared and binary deployment targets; not a device compatibility test."""
import pathlib, plistlib, sys, subprocess, re
for item in sys.argv[1:]:
    root = pathlib.Path(item)
    for bundle in [root, *root.glob("PlugIns/*.appex")]:
        p = plistlib.loads((bundle / "Info.plist").read_bytes())
        assert tuple(map(int, str(p.get("MinimumOSVersion", "0")).split("."))) <= (14, 0), (bundle, p.get("MinimumOSVersion"))
        assert p["CFBundleIdentifier"].startswith("com.551uk.chatgptios14"), bundle
        binaries = [bundle / p["CFBundleExecutable"]]
        if bundle == root and (bundle / "Frameworks/ChatGPTShell.dylib").exists():
            binaries.append(bundle / "Frameworks/ChatGPTShell.dylib")
        for binary in binaries:
            output = subprocess.check_output(["xcrun", "otool", "-l", str(binary)], text=True)
            versions = re.findall(r"^\s*minos\s+([\d.]+)", output, re.M)
            versions += re.findall(r"cmd LC_VERSION_MIN_IPHONEOS\s+cmdsize \d+\s+version ([\d.]+)", output)
            assert versions, f"No deployment target in {binary}"
            assert all(tuple(map(int, v.split("."))) <= (14, 0) for v in versions), (binary, versions)
            print(binary.name, versions)
print("Declared app/helper and native Mach-O deployment targets verified")

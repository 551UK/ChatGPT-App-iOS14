"""Static packaging and feature wiring regression checks, not device tests."""
from pathlib import Path
import plistlib
root = Path(__file__).resolve().parents[1]
def read(p): return (root / p).read_text()
pkg = read("scripts/package.sh")
assert "-miphoneos-version-min=14.0" in pkg
assert "Architecture: iphoneos-arm\n" in pkg
assert "firmware (>= 14.0)" in pkg and "/var/jb/" not in pkg
assert 'uicache -p /Applications/ChatGPT.app' in pkg
for file in ("ChatGPTShell.m","ChatGPTContextMenu.m","ChatGPTDataMaintenance.m","ChatGPTDownloadOverlay.m","ChatGPTExternalLinks.m","ChatGPTRemoteRegistration.m"):
    assert f"/src/{file}" in pkg, file
    assert "com.551uk.chatgptios14" in read("src/"+file), file
for file in ("prefs/ChatGPTPrefs.m","prefs/CGPClearDataController.m","src/ChatGPTDataMaintenance.m"):
    assert "com.551uk.chatgptios14.settings" in read(file), file
assert "CGHasPrivateAppContainer()" in read("src/ChatGPTShell.m")
assert "CGPathIsWithinAppContainer" in read("src/ChatGPTDataMaintenance.m")
assert "THEOS_PACKAGE_SCHEME = rootless" not in read("prefs/Makefile")
assert plistlib.loads((root/"prefs/Resources/Info.plist").read_bytes())["MinimumOSVersion"] == "14.0"
assert "Reynard-Jailbroken.ipa" in pkg and "Reynard-TrollStore.tipa" in pkg
assert "CGHomeRouteTitleMarker" in read("src/ChatGPTShell.m")
assert "chatgpt-app-shell.js" in pkg
print("PASS: iOS 14 packaging and feature wiring")

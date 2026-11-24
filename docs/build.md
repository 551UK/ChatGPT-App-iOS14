# iOS 14 experimental port build

Use macOS, Xcode 16.4 or another iOS-14-capable toolchain, ldid, dpkg, Python with Pillow and LIEF, and Theos with its iPhoneOS16.5 SDK. Set THEOS to the checkout.

```sh
python3 -m pip install pillow lief
FLAVOR=jailbroken bash scripts/package.sh
FLAVOR=trollstore bash scripts/package.sh
```

The first builds the rootful DEB and standalone IPA from Reynard-Jailbroken. The second builds the alternative TrollStore IPA/TIPA only. Keep the Gecko helper extension. Do not install both variants at once; use the rootful DEB or an IPA, not both. Only the DEB includes the jailbreak Settings bundle.

The build enforces availability warnings for the native Objective-C target, checks actual app/helper/shell Mach-O targets, and checks both the downloaded archive and untouched XUL against the user-supplied official Reynard 0.22.1 hashes. The old v1.28 Gecko 158 binary patch is archived, not applied to Gecko 160; its original crash signature needs fresh investigation if it recurs. Private API behavior, JIT, audio, gestures, photo picker, Settings and stability require testing on real iOS 14.3 hardware. The original iOS 16 published package is not a valid release of this port.

GitHub Actions provides independent build jobs and uploads artifacts if successful. Start with the rootful DEB or primary IPA; if one fails, report the installation error and app crash log, and identify the variant.

Each successful variant publishes independently to GitHub Releases. The native shell and cleanup code refuse to operate if the app HOME is not an isolated app data container; Settings also validates the container and supports the legacy LaunchServices containerURL selector. iOS 14 settings use a separate preference domain. The rootful DEB uses targeted uicache registration. These protections are intentional and need device validation.

The public release workflow uses `IPA_ONLY=1` for both variants, skips Theos/DEB and duplicate TIPA packaging, and publishes one release containing exactly the two verified IPA files. Older iOS 14 project releases are deleted only after the replacement release is public and both assets are confirmed uploaded. Local DEB build source remains available but is not used by the public workflow.

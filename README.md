# ChatGPT App for iOS 14 (experimental)

Independent port of [551UK/ChatGPT-App-iOS16](https://github.com/551UK/ChatGPT-App-iOS16), v1.30 source commit `32cd00ca879081d61fd7342825239e949ed26618`. Uses Reynard 0.22.1 / Gecko 160.0 (v1.31). Target: iOS 14.0+, ARM64, rootful jailbreak; for my 14.3 device

- Rootful DEB: /Applications, /Library/PreferenceBundles, iphoneos-arm.
- Alternative TrollStore IPA/TIPA: built separately from upstream TrollStore flavor.
- Retains the v1.30 native shell, appearance, download handling, gestures, data controls and web UI. Runtime testing is pending.
- Separate bundle identifier com.551uk.chatgptios14 and DEB package identifier. Do not install both variants of this port simultaneously.

The upstream archives are pinned to the SHA-256 hashes of the user's working iOS 14.3 uploads. The logged-out homepage uses native ChatGPT header styling; signed-in custom styling is retained. The old Gecko 158 binary patch is not applied to Gecko 160.

[Releases](https://github.com/551UK/ChatGPT-App-iOS14/releases)

Release policy: only the two current IPA variants are published together. No DEB or TIPA release assets. Older project releases are removed after both new IPAs have been verified and published. Source tags are retained.

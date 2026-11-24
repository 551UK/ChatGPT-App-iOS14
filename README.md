# ChatGPT App for iOS 14 (experimental)

Independent port of [551UK/ChatGPT-App-iOS16](https://github.com/551UK/ChatGPT-App-iOS16), v1.30 source commit `32cd00ca879081d61fd7342825239e949ed26618`. Uses Reynard 0.19.0. Target: iOS 14.0+, ARM64, rootful jailbreak; for my 14.3 device

- Rootful DEB: /Applications, /Library/PreferenceBundles, iphoneos-arm.
- Alternative TrollStore IPA/TIPA: built separately from upstream TrollStore flavor.
- Retains the v1.30 native shell, appearance, download handling, gestures, data controls and web UI. Runtime testing is pending.
- Separate bundle identifier com.551uk.chatgptios14 and DEB package identifier. Do not install both variants of this port simultaneously.

# iOS 14.3 compatibility audit

Source baseline: iOS 16 v1.30, Reynard 0.19.0. Upstream explicitly recommends the Jailbroken build for jailbroken iOS 14. The TrollStore build uses a different Gecko allocator and JIT helper; do not transplant the old XUL patch to it.

| Feature | Source retained | iOS 14 consideration |
|---|---|---|
| Full-screen native app, startup spinner, restore last chat | ChatGPTShell.m | UIKit lifecycle, gestures and view transforms use iOS 14 or older public APIs; private Swift classes still require device test. |
| Left edge back, right edge refresh, keyboard clearance | ChatGPTShell.m | Native recognizers and existing animation paths preserved. |
| Header/sidebar, appearance and Share fixes | web/chatgpt-app-shell.js | Gecko handles web APIs rather than the iOS system WebKit. Existing browser regression test preserved. |
| Microphone and voice | ChatGPTShell.m, ChatGPTRemoteRegistration.m | iOS permission request and Gecko permission store kept; MediaPlayer hooks retained; real audio session testing required. |
| Camera/photo uploads | upstream Reynard file picker | Upstream supports iOS 14 PHPicker and legacy UIImagePicker. Device Photos library must itself be functional. |
| Download overlay, share sheet, external browser links | ChatGPTDownloadOverlay.m, ChatGPTExternalLinks.m | UIKit symbols, activity controller, URL handoff retained. |
| Conversation context menu filtering | ChatGPTContextMenu.m | UIContextMenuConfiguration exists on iOS 13+. |
| Settings appearance shortcut, history toggle, selective data clearing | prefs and ChatGPTDataMaintenance.m | Rootful locations, iOS 14 target, separate preference domain, isolated data container guard and older LaunchServices selector fallback. DEB only. |
| JIT stability patch | scripts/patch_xul_active_stub.py | Exact-hash gate, jailbroken variant only. Alternative TrollStore engine is unpatched. |

Build gate: fail on unguarded public SDK availability issues; inspect main executable, helper, shell and Settings executable Mach-O deployment targets; validate archives before publishing. No device hardware or simulator result is implied by successful compilation. First TrollStore build (run 45493249951) verified main and helper 13.0, shell 14.0, before this additional audit commit. New builds supersede that result.

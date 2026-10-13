# Android-only distribution

- 用户于 2026-10-13 明确停止维护网页版。只分发 Android APK、累计 PCK、不可变差分基线、签名清单与公钥。
- 不构建、测试、发布或宣传网页版；不要依赖 ChatGPT Sites 传输发布资产。
- 已发布的 android-63001 Release 和 channels/android-63001.json 保持可用。APK、基线和签名私钥不重新生成身份。
- 新 PCK 必须先上传不可变 Release，再发布签名版本清单；不先推进清单，不覆盖旧基线，不把源码或私钥公开。

# 自动农场更新下载

**平台约定：自 2026-10-13 起仅维护 Android APK 和游戏内增量补丁；网页版已停止维护并关闭公开访问。后续下载与发布均不依赖试玩站。**

当前基座：**v0.63.0（Android 63001，ARM64）**。

- [下载 APK（约 90 MB）](https://github.com/liuqinh2s/auto-farm-updates/releases/download/android-63001/auto-farm-v0.63.0-android-arm64.apk)
- [发布说明与校验信息](https://github.com/liuqinh2s/auto-farm-updates/releases/tag/android-63001)

先覆盖安装这版 APK 一次，沿用原试玩签名和包名。保留 v0.62 的四页菜单、固定场景与现有存档。此后在「设置 → 游戏更新」确认下载兼容的内容补丁，下载并校验完成后，下次启动生效。没有补丁时会显示当前已是最新版本；网络失败时仍可继续游玩。

本仓库只分发安装包、编译后的资源包、签名版本信息和校验公钥，不存放游戏源代码或签名私钥。

`channels/android-63001.json` 是该基座的独立签名更新源。每次补丁相对于对应基座累计构建，验证签名、SHA256、长度和兼容性后才使用；首次启动失败会回退。引擎、启动器、原生权限等变动仍需新 APK。

开发者：Release 内的 `android-base.zip` 为不可变差分基线，不是给玩家安装的文件，勿覆盖。自动构建/发布 CI 的签名和跨仓库凭据需要另行配置；客户端与当前公开下载不需要 GitHub 登录或 token。

已验证原签名、包结构、编译资源启动、更新入口和自动回归；尚未进行 Android 手机真机安装与切后台验证。

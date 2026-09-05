<p align="center">
  <img src="https://komarev.com/ghpvc/?username=KrishBharadwaj5678&label=Profile%20Views&color=brightgreen&style=for-the-badge" />
  <img src="https://hits.sh/github.com/KrishBharadwaj5678/VirtualMouse.svg?style=for-the-badge&label=Repo%20Views&color=blue" />
  <img src="https://img.shields.io/github/stars/KrishBharadwaj5678/VirtualMouse?style=for-the-badge&color=yellow" />
  <img src="https://img.shields.io/github/last-commit/KrishBharadwaj5678/VirtualMouse?style=for-the-badge&color=orange" />
  <img src="https://img.shields.io/github/repo-size/KrishBharadwaj5678/VirtualMouse?style=for-the-badge&color=blue" />
</p>

<p align="center">
  <a href="README.md">English</a> |
  <a href="README.pt.md">Português</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.ru.md">Русский</a>
</p>

<h1 align="center"><img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/icons/virtualMouse.png" width="35"/> バーチャルマウス</h1>

<p align="center">
   バーチャルマウスは、Webカメラで検出した手のジェスチャーを使ってコンピューターを操作できる、タッチフリーな操作システムです。
</p>

<p align="center">
  <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/demos/virtualMouse.gif" width="100%" />
</p>

<img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/divider.gif" width="100%"/>

## <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/features.gif" width="35"/> 機能

| 機能 | 説明 |
| ----------------------------- | ------------------------------------------------------------------------------------ |
| 🖐️ ハンドジェスチャー操作 | 手の動きを使ってリアルタイムでマウスポインターを操作できます。 |
| 👆 クリック操作 | **左クリック**、**右クリック**、**ダブルクリック**を指のジェスチャーで実行できます。 |
| ↕️ 上下スクロール | 指の動きを使ってページを上下にスクロールできます。 |
| 🖱️ カーソル移動 | 手の位置に基づいてマウスカーソルを滑らかに移動できます。 |
| ⚡ リアルタイムトラッキング | **OpenCV** と **MediaPipe** を使用した高速で応答性の高いトラッキングを実現します。 |
| 🤟 ジェスチャー認識 | 特定の指の形状を認識し、それぞれ異なるコマンドを実行できます。 |

<img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/divider.gif" width="100%"/>

## <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/techStack.gif" width="35"/> 技術スタック

| 技術 | 用途 |
| ---------- | ------- |
| <img src="https://skillicons.dev/icons?i=python" width="25"/> **Python3** | メインプログラミング言語 |
| <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/icons/opencv.png" width="25"/> **OpenCV** | ビデオキャプチャと画像処理 |
| <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/icons/mediapipe.png" width="25"/> **MediaPipe** | ハンドトラッキングとジェスチャー検出 |
| <img src="https://skillicons.dev/icons?i=python" width="25"/> **PyAutoGUI** | マウス操作のシミュレーション |
| <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/icons/numpy.png" width="25"/> **NumPy** | 効率的な数値計算 |

<img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/divider.gif" width="100%"/>

## <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/gettingStarted.gif" width="35"/> はじめに

### 1️⃣ リポジトリをクローン

```bash
git clone https://github.com/KrishBharadwaj5678/VirtualMouse.git
````

### 2️⃣ プロジェクトへ移動

```
cd VirtualMouse
```

### 3️⃣ 依存関係をインストール

```
pip install -r requirements.txt
```

### 4️⃣ アプリを実行

```
python app.py
```

<img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/divider.gif" width="100%"/> 

## <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/howItWorks.gif" width="35"/> ジェスチャー操作

<p align="center">
  <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/demos/fingerNames.png"/> 
</p> 

| 操作 | 指の位置 | 距離のしきい値 |
| --- | --- | --- |
| **左クリック** | 人差し指 🔼、中指 🔼 | 人差し指 ↔️ 中指 < 25px |
| **右クリック** | 人差し指 🔼、中指 🔼、小指 🔼 | 人差し指 ↔️ 中指 < 25px |
| **下スクロール** | 人差し指 🔼、中指 🔼、親指 🔼 | 人差し指 ↔️ 中指 < 25px |
| **上スクロール** | 人差し指 🔼、中指 🔼、小指 🔼、親指 🔼 | 人差し指 ↔️ 中指 < 25px |
| **ダブルクリック** | 人差し指 🔼、親指 🔼 | 不要 |

- 🔼 = 指を上げる
- ↔️ = 指先同士の距離

<img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/divider.gif" width="100%"/>

## <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/license.gif" width="35"/> ライセンス

このプロジェクトは **MIT License** のもとでライセンスされています。

詳細については [LICENSE](LICENSE) ファイルをご覧ください。

<p align="center"> 
  <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/footer.gif" width="320px"/>
</p>


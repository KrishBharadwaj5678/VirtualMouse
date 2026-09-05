<p align="center">
  <img src="https://komarev.com/ghpvc/?username=KrishBharadwaj5678&label=Profile%20Views&color=brightgreen&style=for-the-badge" />
  <img src="https://hits.sh/github.com/KrishBharadwaj5678/VirtualMouse.svg?style=for-the-badge&label=Repo%20Views&color=blue" />
  <img src="https://img.shields.io/github/stars/KrishBharadwaj5678/VirtualMouse?style=for-the-badge&color=yellow" />
  <img src="https://img.shields.io/github/last-commit/KrishBharadwaj5678/VirtualMouse?style=for-the-badge&color=orange" />
  <img src="https://img.shields.io/github/repo-size/KrishBharadwaj5678/VirtualMouse?style=for-the-badge&color=blue" />
</p>

<p align="center"> 
  <a href="README.md">English</a> | <a href="README.pt.md">Português</a> | <a href="README.ja.md">日本語</a> | <a href="README.ru.md">Русский</a> 
</p>

<h1 align="center"> 
  <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/icons/virtualMouse.png" width="35"/> Виртуальная мышь 
</h1> 

<p align="center">
  Virtual Mouse позволяет управлять компьютером с помощью жестов рук, распознаваемых через веб-камеру, обеспечивая удобный способ взаимодействия с экраном без использования физической мыши.
</p> 

<p align="center"> 
  <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/demos/virtualMouse.gif" width="100%" /> 
</p> 

<img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/divider.gif" width="100%"/>

## <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/features.gif" width="35"/> Возможности

| Возможность | Описание |
|-------------|----------|
| 🖐️ **Управление жестами** | Используйте руку для перемещения указателя мыши в реальном времени. |
| 👆 **Действия с кликами** | Выполняйте **левый**, **правый** и **двойной** клик с помощью жестов пальцев. |
| ↕️ **Прокрутка вверх / вниз** | Прокручивайте страницы с помощью движений пальцев. |
| 🖱️ **Перемещение курсора** | Плавно перемещайте курсор мыши в зависимости от положения руки. |
| ⚡ **Отслеживание в реальном времени** | Быстрое и отзывчивое отслеживание с использованием **OpenCV** и **MediaPipe**. |
| 🤟 **Распознавание жестов** | Определяйте различные положения пальцев для выполнения разных команд. |

<img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/divider.gif" width="100%"/>

## <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/techStack.gif" width="35"/> Технологический стек

| Технология | Назначение |
|------------|------------|
| <img src="https://skillicons.dev/icons?i=python" width="25"/>  **Python3** | Основной язык программирования |
| <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/icons/opencv.png" width="25"/> **OpenCV** | Захват видео и обработка изображений |
| <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/icons/mediapipe.png" width="25"/> **MediaPipe** | Отслеживание рук и распознавание жестов |
| <img src="https://skillicons.dev/icons?i=python" width="25"/> **PyAutoGUI** | Имитация действий мыши |
| <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/icons/numpy.png" width="25"/> **NumPy** | Эффективные числовые вычисления |

<img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/divider.gif" width="100%"/>

## <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/gettingStarted.gif" width="35"/> Начало работы

### 1️⃣ Клонирование репозитория

```bash
 git clone https://github.com/KrishBharadwaj5678/VirtualMouse.git
```

### 2️⃣ Переход в папку проекта

```bash
 cd VirtualMouse
```

### 3️⃣ Установка зависимостей

```bash
 pip install -r requirements.txt
```

### 4️⃣ Запуск приложения

```bash
 python app.py
```

<img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/divider.gif" width="100%"/>

## <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/howItWorks.gif" width="35"/> Инструкция по жестам

<p align="center">
  <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/demos/fingerNames.png"/> 
</p>

| Действие | Положение пальцев | Порог расстояния |
|----------|-------------------|------------------|
| **Левый клик** | Указательный 🔼, средний 🔼 | Указательный ↔️ средний < 25px |
| **Правый клик** | Указательный 🔼, средний 🔼, мизинец 🔼 | Указательный ↔️ средний < 25px |
| **Прокрутка вниз** | Указательный 🔼, средний 🔼, большой 🔼 | Указательный ↔️ средний < 25px |
| **Прокрутка вверх** | Указательный 🔼, средний 🔼, мизинец 🔼, большой 🔼 | Указательный ↔️ средний < 25px |
| **Двойной клик** | Указательный 🔼, большой 🔼 | Не требуется |

- 🔼 = Палец поднят
- ↔️ = Расстояние между кончиками пальцев
  
<img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/divider.gif" width="100%"/>

## <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/license.gif" width="35"/> Лицензия

Этот проект распространяется под лицензией MIT License.

Подробнее см. в файле [LICENSE](LICENSE).

<p align="center"> 
  <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/footer.gif" width="320px"/> 
</p>

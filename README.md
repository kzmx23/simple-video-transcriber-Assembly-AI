# Video Transcriber

Python-скрипт для транскрибации видеофайлов через AssemblyAI API. Результат сохраняется в Markdown-файл с метками спикеров и таймкодами.

## Возможности

- Загрузка видео/аудио на AssemblyAI с прогресс-баром.
- Транскрибация с разделением по спикерам.
- Поддержка русского языка.
- Результат сохраняется в `.md` файл рядом с исходным видео.
- Drag & Drop на Windows через `.bat` файл.

## Требования

- Python 3.7+
- API-ключ AssemblyAI (получить на [assemblyai.com](https://www.assemblyai.com/))

## Установка (Windows)

### 1. Установить пакеты в системный Python

Открыть `cmd` или `PowerShell` и выполнить:

```
pip install requests python-dotenv tqdm
```

### 2. Настроить API-ключ

Скопировать `.env-example` в `.env`:

```
copy .env-example .env
```

Открыть `.env` в любом текстовом редакторе и заменить `your_mock_api_key_here` на свой ключ.

### 3. Использование

Перетащить видеофайл на `transcribe.bat` — транскрипт сохранится в `.md` рядом с видео.

Или из командной строки:

```
transcribe.bat "путь\к\видео.mp4"
```

## Структура проекта

- `assemblyai_transcriber.py` — основной скрипт.
- `transcribe.bat` — запуск через drag & drop.
- `requirements.txt` — зависимости Python.
- `.env` — API-ключ (не коммитится в git).
- `.env-example` — шаблон для `.env`.

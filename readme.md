# Data Mining Project - 3rd Year (Part 3)

<div dir="rtl">

**תקציר:** חלק ג' של פרויקט כריית נתונים (שנה ג'). אתר אינטרנט קטן ב-Flask שמגיש את המודל המאומן: המשתמש מזין נתוני סרט (שנה, אורך, תקציב, שפה, מדינה, שחקנים, כותבים וז'אנרים) ומקבל חיזוי של דירוג IMDb. הקלט עובר את אותו עיבוד נתונים מחלק ב' לפני החיזוי.

</div>

---

> **Project series:** [Part 1 – Data collection](https://github.com/roeiraz12/Data-minning-project---3rd-year) → [Part 2 – Rating prediction](https://github.com/roeiraz12/Data-minning-project---3rd-year-part_2) → **Part 3 – Prediction web app (this repo)**

## Overview

Part 3 of a third-year Data Mining course project turns the Part 2 model into a working web app. A Flask server loads a saved scikit-learn pipeline, a one-page Hebrew (RTL) form collects the details of a movie, and a `/predict` endpoint returns the predicted IMDb rating rounded to one decimal. The same `prepare_data()` logic used in training (`assets_data_prep.py`) is applied to each request, with a special path for single "live" movies so that it does not need the IMDb crew file.

## What was done

- **REST API (`api.py`)**
  - `GET /` serves the form.
  - `POST /predict` takes JSON input and returns `{"predicted_rating": …}` or a clear error with HTTP 400/500.
- **Input validation** – required fields; numeric year, runtime and budget; year 1900–2026 (Part 2 treats years before 1900 as missing); runtime 1–300 minutes; English-only language and country; actors (up to 5) and writers (up to 2) as IMDb person IDs (`nm` + 7–8 digits), genres (up to 3) in English. List fields accept a JSON list (`["nm0000138","nm0000701"]`) or comma-separated text (`nm0000138, nm0000701`), with duplicate and format checks.
- **Feature pipeline at inference** – builds the same 20 Boruta-selected features as in Part 2 (including the five custom features) and fills any missing ones before calling `model.predict`.
- **Front end (`index.html`)** – a small form with a loading spinner that shows the predicted rating out of 10.
- **Model** – `model.pkl` is a scikit-learn `Pipeline` (preprocessing + `HistGradientBoostingRegressor`), the same file as in Part 2.

## Tech stack

Python · Flask · scikit-learn · pandas · NumPy · joblib · HTML/CSS/JavaScript (fetch API)

## Results

This part is a deployment step. It does not include new evaluation numbers; see [Part 2](https://github.com/roeiraz12/Data-minning-project---3rd-year-part_2) for the model comparison.

## Repository structure

| File | Description |
|---|---|
| `api.py` | Flask app: routes, input validation, feature building, prediction |
| `assets_data_prep.py` | `prepare_data()` – cleaning and feature engineering shared with training |
| `index.html` | Web form (Hebrew, RTL) |
| `model.pkl` | Trained scikit-learn pipeline |
| `requirements.txt` | Python dependencies |

## How to run

Tested with Python 3.12 on Windows using the pinned `requirements.txt` (scikit-learn must stay at 1.7.2, the version the model was saved with).

```bash
python -m venv venv
venv\Scripts\activate          # Windows; on macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
python api.py
```

Then open <http://127.0.0.1:5000>. `api.py` loads `model.pkl` and serves `index.html` from its own folder, so no extra setup is needed.

**Example request:**

```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" \
  -d '{"startYear":"2024","runtimeMinutes":"120","budget":"5000000","Language":"English","Country":"USA","actor_1":"[\"nm0000138\",\"nm0000701\"]","writer_1":"[\"nm0000116\"]","genre_1":"[\"Action\",\"Drama\"]"}'
```

Response: `{"predicted_rating": 6.2}`. In the web form the same values can be typed as comma-separated text, e.g. actors `nm0000138, nm0000701` and genres `Action, Drama`.

---

<div dir="rtl">

## פרטים נוספים

## חברי הפרויקט

* **שם:** רועי ראז

---

## מבנה תיקיית העבודה

כל הקבצים הדרושים להרצה נמצאים בתיקייה הראשית של המאגר:

* `model.pkl` - המודל המאומן.
* `assets_data_prep.py` - סקריפט הכנת הנתונים.
* `api.py` - קובץ ה-API הראשי להרצת האתר.
* `index.html` - ממשק המשתמש.
* `requirements.txt` - רשימת הספריות הנדרשות.

---

## הוראות הרצה

פתח חלון `cmd` (שורת פקודה), נווט לתיקיית המאגר ובצע את הפקודות הבאות לפי הסדר:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python api.py
```

לאחר הרצת הפקודה האחרונה, האתר יהיה זמין בקישור הבא:
**[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## קלט נדרש למשתמש

בעת השימוש באתר, יש להזין את הנתונים לפי ההנחיות הבאות:

1. **שנה:** מספר שלם בין 1900 ל-2026.
2. **שפה:** מחרוזת טקסט.
3. **זמן סרט (בדקות):** מספר שלם בין 1 ל-300.
4. **תקציב:** מספר חיובי (ללא הגבלה עליונה).
5. **ז'אנר:** עד 3 ז'אנרים באנגלית, מופרדים בפסיקים (`Action, Drama`) או כרשימת JSON.
6. **שחקנים:** עד 5 מזהי IMDb (`nm` + 7-8 ספרות), מופרדים בפסיקים או כרשימת JSON.
7. **כותבים:** עד 2 מזהי IMDb (`nm` + 7-8 ספרות), מופרדים בפסיקים או כרשימת JSON.
8. **ארץ:** מחרוזת טקסט.

</div>

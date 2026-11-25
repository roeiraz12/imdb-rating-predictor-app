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
- **Input validation** – required fields; year 1900–2026; runtime 1–300 minutes; English-only language and country; actors (up to 5), writers (up to 2) and genres (up to 3) given as JSON lists, with duplicate and format checks.
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

`api.py` expects the model file to be named `trained_model.pkl` and the page to be in a `templates/` folder, so two files need to be arranged locally first:

```bash
python -m venv venv
venv\Scripts\activate          # Windows; on macOS/Linux: source venv/bin/activate
pip install -r requirements.txt

copy model.pkl trained_model.pkl        # macOS/Linux: cp model.pkl trained_model.pkl
mkdir templates
copy index.html templates\index.html    # macOS/Linux: cp index.html templates/

python api.py
```

Then open <http://127.0.0.1:5000>.

**Example input:** year `2024`, runtime `120`, budget `5000000`, language `English`, country `USA`, genres `["Action","Drama"]`, actors and writers as JSON lists of IDs.

**Known limitation:** the API checks actor and writer IDs against the pattern `mn` + 7 digits, while IMDb person IDs start with `nm`, so the IDs entered in the form will not match the actors and writers the model was trained on.

---

<div dir="rtl">

## פרטים נוספים

## חברי הפרויקט

* **שם:** רועי ראז

---

## מבנה תיקיית העבודה

על מנת להריץ את הפרויקט בצורה תקינה, וודא כי כל הקבצים הבאים נמצאים בתיקיית שולחן העבודה שלך:

* `trained_model.pkl` - המודל המאומן.
* `assets_data_prep.py` - סקריפט הכנת הנתונים.
* `api.py` - קובץ ה-API הראשי להרצת האתר.
* `title.crew.tsv.gz` - קובץ נתוני צוות הסרט.
* `requirements.txt` - רשימת הספריות הנדרשות.
* `templates/` (תיקייה):
* `index.html` - קובץ עיצוב ממשק המשתמש.

---

## הוראות הרצה

כדי להפעיל את האתר, פתח חלון `cmd` (שורת פקודה), נווט לתיקיית העבודה ובצע את הפקודות הבאות לפי הסדר:

```bash
cd Desktop
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

1. **שנה:** מספר שלם בין 1990 ל-2026.
2. **שפה:** מחרוזת טקסט.
3. **זמן סרט (בדקות):** מספר שלם בין 1 ל-300.
4. **תקציב:** מספר חיובי (ללא הגבלה עליונה).
5. **ז'אנר:** מחרוזת בתבנית ספציפית.
6. **שחקנים:** מחרוזת בתבנית ספציפית.
7. **כותבים:** מחרוזת בתבנית ספציפית.
8. **ארץ:** מחרוזת טקסט.

</div>

# Pixels to Predictions 🎨📊🤖

A free, colourful learning website for **image processing, data analysis, machine learning, deep learning and computer vision**. Pure HTML, CSS and JavaScript: no build step, no server.

**Live site:** `https://<your-username>.github.io/pixels-to-predictions/`

## Courses

| Track | Course | Status |
|---|---|---|
| Data Analysis | Time Series Analysis and Forecasting (16 modules + 4 appendices) | ✅ Available |
| Image Processing | — | Coming soon |
| Machine Learning | — | Coming soon |
| Deep Learning | — | Coming soon |
| Computer Vision | — | Coming soon |

## Host it on GitHub Pages

1. Create a new public repository named `pixels-to-predictions` and upload all files from this folder (keep the folder structure).
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**, select branch `main` and folder `/ (root)`, then **Save**.
4. After a minute the site is live at the address shown on that page.

## Add a new course

1. Put the course page in `courses/`, for example `courses/intro-to-opencv.html`. You can copy `courses/time-series.html` as a template, or regenerate a page with `build_site.py` (it takes any HTML export of your course as input):
   ```bash
   pip install beautifulsoup4 lxml
   python build_site.py path/to/your_course.html courses/intro-to-opencv.html
   ```
2. Open `assets/courses.js` and add one entry to `COURSES`:
   ```js
   {title:"Intro to OpenCV", track:"computer-vision", level:"Beginner", time:"4 weeks",
    modules:"8 modules", url:"courses/intro-to-opencv.html", blurb:"One-sentence summary."}
   ```
   Valid track ids: `image-processing`, `data-analysis`, `machine-learning`, `deep-learning`, `computer-vision`.
3. Commit and push. The home page shows the new course and updates the track counts automatically.

## Structure

```text
pixels-to-predictions/
├── index.html            # home page (tracks and courses)
├── courses/
│   └── time-series.html  # one page per course
├── assets/
│   ├── site.css          # shared styles
│   ├── course.css        # course reading page styles
│   ├── course.js         # progress bar, contents menu, copy buttons, highlighting
│   └── courses.js        # the course catalog: edit this to add courses
├── build_site.py         # turns an HTML course export into a styled course page
├── .nojekyll
└── README.md
```

## Notes

- Fonts (Google Fonts) and code highlighting (highlight.js) load from CDNs. The site still works without them, with plainer fonts and uncoloured code.
- The course text is copied unchanged by `build_site.py`; only styling and navigation are added.
- Add a licence for your course content before sharing it widely.

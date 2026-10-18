<div align="center">

# 🛍️ MallIQ

**Smart customer insights for malls, powered by machine learning.**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-black?logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Model-orange?logo=scikitlearn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📖 About

MallIQ is a lightweight web app that connects a trained machine learning model
to a clean browser interface. Flask serves the frontend and the model API, so
everything runs locally with a single command.
<img width="1816" height="881" alt="image" src="https://github.com/user-attachments/assets/796d7fda-c846-46df-aee4-063da91016f0" />

<img width="844" height="419" alt="image" src="https://github.com/user-attachments/assets/fc982e48-9225-4486-b964-fb0864f1088a" />

## ✨ Features

- 🧠 Pre-trained scikit-learn model loaded with `joblib`
- 🌐 Flask backend with CORS enabled
- 🖥️ Simple web interface served from `templates/index.html`
- ⚡ Runs locally in under a minute

## 🗂️ Project Structure

```
malliq_simplified/
├── app.py                # Flask server and model API
├── customer_model.pkl    # Trained ML model
└── templates/
    └── index.html        # Frontend UI
```

## 🚀 Quick Start

**1. Clone the repository**

```bash
git clone https://github.com/<your-username>/malliq.git
cd malliq
```

**2. Install dependencies**

```bash
python -m pip install flask flask-cors pandas joblib scikit-learn
```

**3. Run the app**

```bash
python app.py
```

**4. Open in your browser**

```
http://127.0.0.1:5000/
```

> ⚠️ **Important:** Open the app through Flask (the link above). Do not
> double-click `index.html`, or the frontend will not connect to the backend.

## 🧰 Tech Stack

| Layer     | Technology                |
| --------- | ------------------------- |
| Backend   | Python, Flask, Flask-CORS |
| ML        | scikit-learn, joblib      |
| Data      | pandas                    |
| Frontend  | HTML (Flask templates)    |

## 🛠️ Troubleshooting

| Problem                       | Fix                                                      |
| ----------------------------- | -------------------------------------------------------- |
| Page loads but nothing works  | Open via `http://127.0.0.1:5000/`, not the HTML file     |
| `ModuleNotFoundError`         | Re-run the `pip install` command above                   |
| Model fails to load           | Use the same scikit-learn version the model was saved with |
| Port 5000 already in use      | Stop the other app or change the port in `app.py`        |

## 🗺️ Roadmap

- [ ] 
- [ ] Add input validation and error messages
- [ ] Add `requirements.txt`
- [ ] Deploy online (Render / Railway)

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to
discuss what you would like to change.

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.

---

<div align="center">
Made with ❤️ by <b>&lt;Your Name&gt;</b>
</div>

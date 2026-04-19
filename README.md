🎬 CineMatch – Movie Recommendation System

CineMatch is a modern movie recommendation system that suggests movies based on similarity using content-based filtering. It integrates with the TMDB API to fetch real-time posters, ratings, and movie details.

---

## 🚀 Features

* 🎥 Content-based movie recommendation
* 🖼️ Real-time movie posters using TMDB API
* ⭐ Ratings and vote count display
* 🧠 Smart similarity-based suggestions
* ⚡ Fast and interactive UI built with Streamlit
* 🎨 Modern dark-themed UI design

---

## 🛠️ Tech Stack

* **Frontend/UI**: Streamlit, HTML, CSS
* **Backend**: Python
* **ML Logic**: Content-Based Filtering
* **API**: TMDB API
* **Libraries**: pandas, numpy, scikit-learn, requests

---

## 📂 Project Structure

```
CineMatch/
│
├── app.py
├── movie_dict.pkl
├── similarity.pkl
├── requirements.txt
├── Procfile
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/abu-said-mondal/CineMatch.git
cd CineMatch
```

### 2️⃣ Create virtual environment

```
python -m venv myenv
source myenv/bin/activate   # Mac/Linux
myenv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Set up environment variable

Create a `.env` file and add:

```
API_KEY=469a1cb08eaa2e88c74b11a1b173c2c4
```

---

## ▶️ Run the App

```
streamlit run app.py
```

---

## 🌐 Deployment

This project is deployed using **Render**.

* Build Command:

```
pip install -r requirements.txt
```

* Start Command:

```
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

---

## 💡 Future Improvements

* 🔍 Search-based recommendations
* 🎭 Genre filtering
* ❤️ Save favorite movies
* 📊 Hybrid recommendation system

---

## 👨‍💻 Author

Abu Said Anowar Mondal

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!

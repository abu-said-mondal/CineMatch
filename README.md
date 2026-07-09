🎬 CineMatch – Movie Recommendation System

CineMatch is a modern movie recommendation system that suggests movies based on similarity using content-based filtering. It integrates with the TMDB API to fetch real-time posters, ratings, and movie details.

🔗 **Live demo:** https://cinematch-7mzi.onrender.com

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
* **Libraries**: pandas, numpy, scikit-learn, requests, python-dotenv

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
├── .gitattributes
├── .gitignore
└── README.md
```

> **Note:** `movie_dict.pkl` and `similarity.pkl` are tracked with **Git LFS** (see `.gitattributes`). You must have Git LFS installed *before* cloning, or you'll end up with tiny placeholder files instead of the real data — see setup steps below.

---

## ⚙️ Installation & Setup

### 1️⃣ Install Git LFS (one-time, before cloning)

```
git lfs install
```

If you don't have Git LFS yet, install it first: https://git-lfs.com

### 2️⃣ Clone the repository

```
git clone https://github.com/abu-said-mondal/CineMatch.git
cd CineMatch
```

This pulls the real `movie_dict.pkl` and `similarity.pkl` files via LFS. If you already cloned the repo *before* installing Git LFS, run this instead to fetch the real files:

```
git lfs pull
```

### 3️⃣ Create virtual environment

```
python -m venv myenv
source myenv/bin/activate   # Mac/Linux
myenv\Scripts\activate      # Windows
```

### 4️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 5️⃣ Set up your TMDB API key

Get a free API key from [TMDB](https://www.themoviedb.org/settings/api), then create a `.env` file in the project root:

```
API_KEY=your_tmdb_api_key_here
```

---

## ▶️ Run the App

```
streamlit run app.py
```

---

## 🌐 Deployment

This project is deployed on **Render**: https://cinematch-7mzi.onrender.com

* **Build Command:**

```
pip install -r requirements.txt
```

* **Start Command:**

```
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

* Set the `API_KEY` environment variable in Render's dashboard (Environment → Environment Variables) rather than committing it anywhere in the repo.
* Make sure Git LFS is enabled for the Render build so the real `.pkl` files are pulled during deployment.

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

# 🎬 Movie Recommendation System

A content-based movie recommendation system built using **Machine Learning and NLP techniques**.
The app suggests similar movies based on user selection and displays movie posters using the **TMDB API**.

🚀 **Live Demo:**
https://movie-recommender-system-00.streamlit.app/

---

## 📌 Features

* 🎯 Recommends top 5 similar movies
* 🧠 Uses **cosine similarity** for recommendations
* 🎥 Fetches movie posters using TMDB API
* 🌐 Interactive web app built with Streamlit
* ⚡ Fast and lightweight (no large model files required)

---

## 🛠️ Tech Stack

* **Python**
* **Pandas & NumPy**
* **Scikit-learn**
* **NLTK**
* **Streamlit**
* **TMDB API**

---

## ⚙️ How It Works

1. Movie data is preprocessed using NLP techniques
2. Important features (genres, keywords, cast, crew) are combined into tags
3. Text data is vectorized using **CountVectorizer**
4. Similarity between movies is calculated using **cosine similarity**
5. Top similar movies are recommended to the user

---

## 📂 Project Structure

```
Movie-Recommender-System/
│
├── app.py
├── artifacts/
│   └── movie_list.pkl
├── data/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔑 Environment Variables

This project uses TMDB API. Add your API key in Streamlit Secrets:

```toml
TMDB_API_KEY = "your_api_key_here"
```

---

## ▶️ Run Locally

```bash
git clone https://github.com/your-username/Movie-Recommender-System.git
cd Movie-Recommender-System

pip install -r requirements.txt
streamlit run app.py
```

---

## 🚀 Deployment

This project is deployed using **Streamlit Cloud**.

---

## 💡 Key Highlights

* Avoided uploading large `.pkl` files by dynamically computing similarity
* Integrated external API for real-time movie posters
* Built an end-to-end ML project from scratch to deployment

---

## 📈 Future Improvements

* Add movie ratings and overview
* Improve UI (cards, animations)
* Add search-based recommendations
* Build hybrid recommendation system

---

## 👩‍💻 Author

**Somya Singhal**

---

⭐ If you like this project, don’t forget to **star the repository!**

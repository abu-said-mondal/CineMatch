import streamlit as st
import pickle
import pandas as pd
import requests
import os

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CineMatch",
    page_icon="🎬",
    layout="wide",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

/* ── Base ── */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #0c0c0f;
    color: #e8e6e1;
    font-family: 'DM Sans', sans-serif;
}
[data-testid="stHeader"] { background: transparent; }

/* ── Hero ── */
.hero {
    text-align: center;
    padding: 3rem 0 1.5rem;
}
.hero h1 {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(3rem, 8vw, 6rem);
    letter-spacing: 0.06em;
    line-height: 1;
    background: linear-gradient(135deg, #f5c518 0%, #ff6b35 60%, #e63946 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
}
.hero p {
    color: #888;
    font-size: 1rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-top: 0.4rem;
}

/* ── Selectbox label ── */
label[data-testid="stWidgetLabel"] > div {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.85rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #888 !important;
}

/* ── Selectbox ── */
[data-testid="stSelectbox"] > div > div {
    background: #1a1a22 !important;
    border: 1px solid #2e2e3a !important;
    border-radius: 8px !important;
    color: #e8e6e1 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1rem !important;
}
[data-testid="stSelectbox"] > div > div:hover {
    border-color: #f5c518 !important;
}

/* ── Button ── */
[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #f5c518, #ff6b35);
    color: #0c0c0f;
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.1rem;
    letter-spacing: 0.15em;
    border: none;
    border-radius: 8px;
    padding: 0.6rem 2.5rem;
    width: 100%;
    cursor: pointer;
    transition: opacity 0.2s, transform 0.15s;
}
[data-testid="stButton"] > button:hover {
    opacity: 0.88;
    transform: translateY(-2px);
}

/* ── Section heading ── */
.section-heading {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.5rem;
    letter-spacing: 0.1em;
    color: #f5c518;
    margin: 2.5rem 0 1rem;
    border-left: 3px solid #f5c518;
    padding-left: 0.75rem;
}

/* ── Movie card ── */
.movie-card {
    background: #16161e;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid #2e2e3a;
    transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
    margin-bottom: 1rem;
}
.movie-card:hover {
    transform: translateY(-6px);
    border-color: #f5c518;
    box-shadow: 0 12px 32px rgba(245, 197, 24, 0.15);
}
.movie-info {
    background: #1a1a22;
    padding: 0.55rem 0.5rem 0.65rem;
}
.movie-rank {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 0.65rem;
    color: #f5c518;
    letter-spacing: 0.12em;
    margin-bottom: 0.2rem;
}
.movie-title {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.78rem;
    font-weight: 500;
    color: #e8e6e1;
    line-height: 1.3;
    margin-bottom: 0.35rem;
}
.movie-meta {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    margin-bottom: 0.4rem;
}
.movie-rating {
    display: inline-flex;
    align-items: center;
    gap: 0.2rem;
    background: rgba(245,197,24,0.12);
    border: 1px solid rgba(245,197,24,0.3);
    border-radius: 4px;
    padding: 0.1rem 0.35rem;
    font-size: 0.72rem;
    font-weight: 600;
    color: #f5c518;
    letter-spacing: 0.03em;
}
.movie-votes {
    font-size: 0.62rem;
    color: #555;
    letter-spacing: 0.02em;
}
.movie-tagline {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.68rem;
    font-style: italic;
    font-weight: 300;
    color: #888;
    line-height: 1.4;
    border-top: 1px solid #2e2e3a;
    padding-top: 0.35rem;
    margin-top: 0.1rem;
}

/* ── Skeleton shimmer ── */
@keyframes shimmer {
    0%   { background-position: -800px 0; }
    100% { background-position:  800px 0; }
}
.skeleton-wrap {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    margin-top: 1.5rem;
}
.skeleton-row {
    display: flex;
    gap: 1rem;
}
.skeleton-card {
    flex: 1;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid #2e2e3a;
    background: #16161e;
}
.skeleton-poster {
    width: 100%;
    aspect-ratio: 2/3;
    background: linear-gradient(90deg, #1a1a22 25%, #252530 50%, #1a1a22 75%);
    background-size: 800px 100%;
    animation: shimmer 1.4s infinite linear;
}
.skeleton-text-block {
    padding: 0.6rem 0.5rem;
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
    background: #1a1a22;
}
.skeleton-line {
    border-radius: 4px;
    background: linear-gradient(90deg, #252530 25%, #2e2e3a 50%, #252530 75%);
    background-size: 800px 100%;
    animation: shimmer 1.4s infinite linear;
}

/* ── Divider ── */
hr { border-color: #2e2e3a; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0c0c0f; }
::-webkit-scrollbar-thumb { background: #2e2e3a; border-radius: 3px; }
</style>
""", unsafe_allow_html=True)


# ── Skeleton HTML helper ──────────────────────────────────────────────────────
def render_skeleton(n_rows=2, n_cols=5):
    rows_html = ""
    for _ in range(n_rows):
        cards_html = ""
        for _ in range(n_cols):
            cards_html += """
            <div class="skeleton-card">
                <div class="skeleton-poster"></div>
                <div class="skeleton-text-block">
                    <div class="skeleton-line" style="height:9px; width:40%;"></div>
                    <div class="skeleton-line" style="height:11px; width:85%;"></div>
                    <div class="skeleton-line" style="height:9px; width:55%;"></div>
                    <div class="skeleton-line" style="height:9px; width:70%;"></div>
                </div>
            </div>"""
        rows_html += f'<div class="skeleton-row">{cards_html}</div>'
    return f'<div class="skeleton-wrap">{rows_html}</div>'


# ── Functions ─────────────────────────────────────────────────────────────────
def fetch_movie_details(movie_id):

    api_key = os.getenv("API_KEY")
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=4{api_key}'
    )
    data = response.json()
    poster     = "https://image.tmdb.org/t/p/w500/" + data.get('poster_path', '')
    rating     = round(data.get('vote_average', 0), 1)   # 7.5 not 7.55
    vote_count = data.get('vote_count', 0)
    overview   = data.get('overview', '').strip()
    blurb = overview[:100] + '…'
    return poster, rating, vote_count, blurb

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances   = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies  = []
    recommended_posters = []
    recommended_ratings = []
    recommended_votes   = []
    recommended_blurbs  = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        poster, rating, vote_count, blurb = fetch_movie_details(movie_id)
        recommended_posters.append(poster)
        recommended_ratings.append(rating)
        recommended_votes.append(vote_count)
        recommended_blurbs.append(blurb)

    return recommended_movies, recommended_posters, recommended_ratings, recommended_votes, recommended_blurbs


# ── Data ──────────────────────────────────────────────────────────────────────
movies_list = pickle.load(open('movie_dict.pkl', 'rb'))
movies      = pd.DataFrame(movies_list)
similarity  = pickle.load(open('similarity.pkl', 'rb'))


# ── UI ────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>🎬 CineMatch</h1>
    <p>Discover your next favourite film</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

col_select, col_btn = st.columns([4, 1], vertical_alignment="bottom")

with col_select:
    selected_movie_name = st.selectbox(
        "Pick a movie you love",
        (movies['title'].values),
    )

with col_btn:
    recommend_clicked = st.button("✦ Recommend")

# ── Results ───────────────────────────────────────────────────────────────────
if recommend_clicked:

    st.markdown('<div class="section-heading">Top Picks For You</div>', unsafe_allow_html=True)

    # Skeleton cards while API calls are in flight
    skeleton_placeholder = st.empty()
    skeleton_placeholder.markdown(render_skeleton(2, 5), unsafe_allow_html=True)

    names, posters, ratings, votes, blurbs = recommend(selected_movie_name)

    skeleton_placeholder.empty()   # swap skeleton → real cards

    for i in range(0, len(posters), 5):
        cols = st.columns(5, gap="small")

        for j in range(5):
            if i + j < len(posters):
                with cols[j]:
                    rank   = i + j + 1
                    rating = ratings[i + j]
                    vote_k = f"{votes[i + j] // 1000}k" if votes[i + j] >= 1000 else str(votes[i + j])
                    blurb  = blurbs[i + j]

                    st.markdown('<div class="movie-card">', unsafe_allow_html=True)
                    st.image(posters[i + j], use_container_width=True)
                    st.markdown(f"""
                        <div class="movie-info">
                            <div class="movie-rank">#{rank}</div>
                            <div class="movie-title">{names[i + j]}</div>
                            <div class="movie-meta">
                                <span class="movie-rating">⭐ {rating}</span>
                                <span class="movie-votes">{vote_k} votes</span>
                            </div>
                            {'<div class="movie-tagline">' + blurb + '</div>' if blurb else ''}
                        </div>
                    </div>""", unsafe_allow_html=True)
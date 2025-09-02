<template>
  <div class="app">
    <!-- Header -->
    <header class="header">
      <h1 class="logo">🎬 TMDB</h1>
      <nav>
        <ul>
          <li>Movies</li>
          <li>TV Shows</li>
          <li>People</li>
          <li>More</li>
        </ul>
      </nav>
      <div class="auth-buttons">
        <button class="btn login">Login</button>
        <button class="btn signup">Sign Up</button>
      </div>
    </header>

    <!-- Hero Section with Backdrop -->
    <section v-if="movie" class="hero" :style="{ backgroundImage: 'url(' + movie.Poster + ')' }">
      <div class="overlay"></div>
      <div class="hero-content">
        <h2>{{ movie.Title }}</h2>
        <p>{{ movie.Plot }}</p>
      </div>
    </section>

    <!-- Movie Section -->
    <main v-if="movie" class="movie-container">
      <!-- Left: Poster -->
      <div class="poster">
        <img :src="movie.Poster" :alt="movie.Title" />
      </div>

      <!-- Right: Movie Info -->
      <div class="movie-info">
        <h2>{{ movie.Title }} <span class="year">({{ movie.Year }})</span></h2>
        <p class="meta">
          {{ movie.Released }} | {{ movie.Genre }} | {{ movie.Runtime }}
        </p>

        <!-- User Score Circle -->
        <div class="user-score">
          <svg viewBox="0 0 36 36" class="circular-chart green">
            <path
              class="circle-bg"
              d="M18 2.0845
                a 15.9155 15.9155 0 0 1 0 31.831
                a 15.9155 15.9155 0 0 1 0 -31.831"
            />
            <path
              class="circle"
              :stroke-dasharray="userScore + ', 100'"
              d="M18 2.0845
                a 15.9155 15.9155 0 0 1 0 31.831
                a 15.9155 15.9155 0 0 1 0 -31.831"
            />
            <text x="18" y="20.35" class="percentage">{{ userScore }}%</text>
          </svg>
          <span>User Score</span>
        </div>

        <!-- Overview -->
        <section class="overview">
          <h3>Overview</h3>
          <p>{{ movie.Plot }}</p>
        </section>

        <!-- Fancy Buttons -->
        <div class="actions">
          <button class="btn like">❤️ Like</button>
          <button class="btn save">🔖 Save</button>
          <button class="btn rate">⭐ Rate</button>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      movie: null,
    };
  },
  computed: {
    userScore() {
      if (!this.movie || !this.movie.Ratings) return 0;
      const rt = this.movie.Ratings.find((r) => r.Source === "Rotten Tomatoes");
      return rt ? parseInt(rt.Value) : 75;
    },
  },
  mounted() {
    fetch("http://www.omdbapi.com/?i=tt3896198&apikey=d2132124")
      .then((res) => res.json())
      .then((data) => {
        this.movie = data;
      });
  },
};
</script>

<style>
/* Global */
body {
  margin: 0;
  font-family: "Poppins", sans-serif;
  background: linear-gradient(135deg, #0d253f, #1e3c72, #2a5298);
  color: #fff;
}

/* --- Updated Navbar --- */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background: linear-gradient(90deg, #032541, #01b4e4, #01d277);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
  position: sticky;
  top: 0;
  z-index: 20;
  border-bottom: 2px solid rgba(255, 255, 255, 0.2);
}

.header .logo {
  color: #fff;
  font-weight: bold;
  font-size: 1.6rem;
  text-shadow: 0 0 8px rgba(1, 210, 119, 0.8);
  cursor: pointer;
  transition: transform 0.3s;
}

.header .logo:hover {
  transform: scale(1.1);
}

.header nav ul {
  list-style: none;
  display: flex;
  gap: 2rem;
  margin: 0;
  padding: 0;
}

.header nav li {
  position: relative;
  cursor: pointer;
  font-weight: 500;
  transition: color 0.3s;
}

.header nav li::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: -6px;
  width: 0;
  height: 2px;
  background: #fff;
  transition: width 0.3s ease;
}

.header nav li:hover {
  color: #ffeb3b;
}

.header nav li:hover::after {
  width: 100%;
}

/* Auth Buttons */
.auth-buttons {
  display: flex;
  gap: 1rem;
}

.auth-buttons .btn {
  padding: 0.4rem 1.2rem;
  border-radius: 25px;
  border: none;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.95rem;
  transition: all 0.3s ease;
}

.login {
  background: transparent;
  color: #fff;
  border: 2px solid #fff;
}

.login:hover {
  background: #fff;
  color: #032541;
  box-shadow: 0 0 10px #fff;
}

.signup {
  background: #ffeb3b;
  color: #032541;
  box-shadow: 0 4px 12px rgba(255, 235, 59, 0.6);
}

.signup:hover {
  background: #ffc107;
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(255, 193, 7, 0.7);
}

/* Hero Section */
.hero {
  position: relative;
  height: 400px;
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero .overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.3));
  backdrop-filter: blur(4px);
}

.hero-content {
  position: relative;
  text-align: center;
  max-width: 800px;
  padding: 2rem;
}

.hero-content h2 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.hero-content p {
  font-size: 1.1rem;
  color: #ddd;
}

/* Layout */
.movie-container {
  display: flex;
  padding: 2rem;
  gap: 3rem;
  align-items: flex-start;
}

.poster img {
  width: 300px;
  border-radius: 12px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.6);
  transition: transform 0.3s;
}

.poster img:hover {
  transform: scale(1.05);
}

.movie-info {
  flex: 1;
}

.year {
  color: #bbb;
  font-weight: 400;
}

.meta {
  color: #ccc;
  font-size: 0.95rem;
  margin-bottom: 1rem;
}

/* Overview */
.overview h3 {
  margin-top: 1.5rem;
  font-size: 1.3rem;
  border-bottom: 2px solid #01d277;
  display: inline-block;
  padding-bottom: 0.2rem;
}

.overview p {
  margin-top: 0.5rem;
  line-height: 1.5;
}

/* Buttons */
.actions {
  margin-top: 2rem;
}

.btn.like,
.btn.save,
.btn.rate {
  margin-right: 1rem;
  padding: 0.6rem 1.2rem;
  border: none;
  border-radius: 25px;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s;
}

.like {
  background: #ff4c4c;
  color: #fff;
}

.like:hover {
  background: #d63b3b;
}

.save {
  background: #2d89ef;
  color: #fff;
}

.save:hover {
  background: #1b5dbb;
}

.rate {
  background: #f5a623;
  color: #fff;
}

.rate:hover {
  background: #d48806;
}

/* User Score */
.user-score {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.circular-chart {
  max-width: 80px;
  max-height: 80px;
}

.circle-bg {
  fill: none;
  stroke: #eee;
  stroke-width: 3.8;
}

.circle {
  fill: none;
  stroke-width: 2.8;
  stroke-linecap: round;
  stroke: #01d277;
  animation: progress 1s ease-out forwards;
}

.percentage {
  fill: white;
  font-size: 0.5em;
  text-anchor: middle;
}

@keyframes progress {
  0% {
    stroke-dasharray: 0 100;
  }
}

/* Responsive */
@media (max-width: 768px) {
  .movie-container {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  .poster img {
    width: 220px;
  }
  .auth-buttons {
    flex-direction: column;
    gap: 0.5rem;
  }
}
</style>

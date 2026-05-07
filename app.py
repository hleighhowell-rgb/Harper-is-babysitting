# =========================
# FILE: app.py
# =========================
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


# =========================
# FILE: requirements.txt (copy separately)
# =========================
flask


# =========================
# FILE: templates/index.html
# =========================
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>AI in X-Rays</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>

<header class="fade">
  <h1>AI in X-Rays</h1>
  <p>How Artificial Intelligence is Changing Medicine</p>
</header>

<nav class="fade">
  <a href="#about">About</a>
  <a href="#xray">X-Rays</a>
  <a href="#ai">AI</a>
  <a href="#future">Future</a>
</nav>

<section id="about" class="fade">
  <h2>What Are X-Rays?</h2>
  <p>X-rays allow doctors to see inside the human body using radiation. They are commonly used to detect broken bones and diseases.</p>
</section>

<section id="xray" class="fade">
  <h2>How X-Rays Work</h2>
  <p>X-rays pass through the body. Dense materials like bones appear white, while soft tissue appears darker.</p>
</section>

<section id="ai" class="fade">
  <h2>How AI Helps</h2>
  <p>AI analyzes X-ray images to detect problems like fractures, pneumonia, and tumors faster than traditional methods.</p>
</section>

<section id="future" class="fade">
  <h2>The Future</h2>
  <p>AI will support doctors by improving diagnosis speed and accuracy, but will not replace human medical professionals.</p>
</section>

<footer class="fade">
  <p>Digital Literacy & AI Project</p>
</footer>

<script>
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if(entry.isIntersecting){
      entry.target.classList.add('show');
    }
  });
});

document.querySelectorAll('.fade').forEach(el => observer.observe(el));
</script>

</body>
</html>


# =========================
# FILE: static/styles.css
# =========================
body {
  font-family: Arial, sans-serif;
  margin: 0;
  background: #0f172a;
  color: #e2e8f0;
}

header {
  background: #1e3a8a;
  padding: 40px;
  text-align: center;
}

nav {
  background: #020617;
  padding: 15px;
  text-align: center;
}

nav a {
  color: #38bdf8;
  margin: 0 15px;
  text-decoration: none;
  font-weight: bold;
}

section {
  padding: 50px;
  max-width: 800px;
  margin: auto;
}

footer {
  text-align: center;
  padding: 20px;
  background: #020617;
}

/* FADE ANIMATION */
.fade {
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.8s ease;
}

.fade.show {
  opacity: 1;
  transform: translateY(0);
}

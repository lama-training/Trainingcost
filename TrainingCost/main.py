from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/training-cost")
def training_cost():
    return render_template("training-cost.html")


@app.route("/news")
def news():
    return render_template("news.html")


@app.route("/internal-audit")
def internal_audit():
    return render_template("internal-audit.html")


@app.route("/risk-analysis")
def risk_analysis():
    return render_template("risk-analysis.html")


@app.route("/sector-details")
def sector_details():
    return render_template("sector-details.html")


@app.route("/hajj-safety")
def hajj_safety():
    return render_template("hajj-safety.html")


@app.route("/human-support")
def human_support():
    return render_template("human-support.html")
@app.route("/government-details")
def government_details():
    return render_template("government-details.html")

@app.route("/citizens-details")
def citizens_details():
    return render_template("citizens-details.html")
@app.route("/course")
def course():
    return render_template("course.html")
@app.route("/details-promotion")
def details_promotion():
    return render_template("details.html")
@app.route("/details")
def details():
    return render_template("details.html")

@app.route('/quiz-flood')
def quiz_flood():
    return render_template('quiz-flood.html')
@app.route('/quiz-risk')
def quiz_risk():
    return render_template('quiz-risk.html')
@app.route('/quiz-hajj')
def quiz_hajj():
    return render_template('quiz-hajj.html')
@app.route('/quiz-internal-audit')
def quiz_internal_audit():
    return render_template('quiz-internal-audit.html')
@app.route('/quiz-human-support')
def quiz_human_support():
    return render_template('quiz-human-support.html')

if __name__ == "__main__":
    app.run(debug=True)



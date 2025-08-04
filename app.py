from flask import Flask, render_template, request, redirect
from models import db, QueryLog
from scraper import fetch_case_data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        filing_year = request.form['filing_year']

        try:
            data, raw_html = fetch_case_data(case_type, case_number, filing_year)

            log = QueryLog(case_type=case_type, case_number=case_number,
                           filing_year=filing_year, raw_response=raw_html)
            db.session.add(log)
            db.session.commit()
            print("Data fetched:", data)

            return render_template('result.html', data=data)
        except Exception as e:
            return render_template('index.html', error=str(e))

    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

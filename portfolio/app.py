from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', 
                           name="Balgani Venkat Naveen Kumar",
                           role="Information Technology Student | Aspiring Full-Stack Developer",
                           about="""Hi, I'm Naveen, a passionate learner in coding, web development, and AI. 
                           Currently pursuing B.Tech in Information Technology at Andhra University (Expected 2027). 
                           I love solving coding challenges, building real-world projects, and leading technical events.""",
                           skills=["Python", "Django", "React", "HTML", "CSS", "JavaScript", "DSA", "Flask"],
                           projects=[
                               {"title": "Bottle Buddy", "desc": "Reverse vending machine startup project that accepts PET bottles and gives rewards via an app."},
                               {"title": "FreshMart", "desc": "Real-time inventory tracking system with multi-language support."},
                               {"title": "HireVision", "desc": "AI-powered video resume screening platform for companies."},
                               {"title": "CO-PO Calculator", "desc": "Django-based system for academic outcome mapping."}
                           ],
                           email="naveenrishi32@gmail.com",
                           phone="99951518580"
                           )

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"Message from {name} ({email}): {message}")
        return "Thank you! Your message has been received."
    return render_template('contact.html', name="Balgani Venkat Naveen Kumar")

if __name__ == '__main__':
    app.run(debug=True)

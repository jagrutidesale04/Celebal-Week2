
# ⭐ Week 2: Singly Linked List Web App using Python & Flask

This project is part of **Week 2** of the **Celebal Summer Internship** program.

The assignment was to implement a **Singly Linked List** using **Object-Oriented Programming (OOP)** in Python. The solution is extended with a **Flask web interface** that provides a clean and interactive GUI.

---

## 📌 Features

- 🔹 `Node` class to represent each node
- 🔹 `LinkedList` class with methods to:
  - Add a node to the end
  - Delete the **nth node** (1-based index)
  - Delete the **center node**
  - Display current linked list
- 🔹 Exception handling for:
  - Deleting from an empty list
  - Index out of range errors
- 🔹 Modern and responsive **GUI using Flask**
  - Input for values
  - Buttons for actions
  - Dynamic display of current list
  - Stylish fonts, header, and footer

---

## 🧾 File Structure

```
Celebal-Week2/
├── app.py               # Flask application logic
├── requirements.txt     # Required Python packages
├── templates/
│   └── index.html       # HTML GUI with Bootstrap and CSS
└── README.md            # Project documentation
```

---

## 🚀 How to Run the Project

### 1. 📥 Clone the Repository

```bash
git clone https://github.com/jagrutidesale04/Celebal-Week2.git
cd Celebal-Week2
```

### 2. 🐍 Create Virtual Environment (Optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate       # On Windows
# OR
source venv/bin/activate    # On macOS/Linux
```

### 3. 📦 Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. ▶️ Run the Flask App

```bash
python app.py
```

> The app will start on [http://127.0.0.1:5000](http://127.0.0.1:5000)

---


## 📚 Sample Use Cases

- Add values like `10`, `20`, `30`, etc.
- Click "Delete Nth Node" and provide index like `2`
- Try deleting center when list is even or odd in size
- Observe how the list dynamically updates

---

## 📎 Requirements

```txt
Flask==2.3.2
```

No external or complex dependencies are required.

---

## 👩‍💻 Author

**Jagruti Desale**  
B.Tech – Data Science and Engineering (3rd Year)  
Summer Intern @ Celebal Technologies  

🔗 [GitHub](https://github.com/jagrutidesale04)  
💼 [LinkedIn](https://www.linkedin.com/in/jagruti-desale-jd04)

---

## 📜 License

This project is for academic and educational use as part of Celebal's internship assignment. You are welcome to fork and learn from it!

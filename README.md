# 🥜 Batony Proteinowe – Aplikacja Flask

Prosta aplikacja webowa stworzona przy użyciu frameworka **Flask**, która prezentuje informacje o batonach proteinowych.

## 📦 Funkcje

- Przegląd batonów proteinowych z opisem i obrazkiem  
- Prosty i responsywny interfejs  
- Łatwa do rozbudowy o dodatkowe funkcje (np. baza danych, formularze)

---

## 🚀 Uruchamianie lokalne

### ✅ Wymagania

- Python 3.7+
- pip

### 📥 Instalacja

1. Sklonuj repozytorium lub pobierz pliki:

    ```bash
    git clone https://github.com/kazachstanski-baton-proteinowy/batony-proteinowe.git
    cd batony-proteinowe
    ```

2. Zainstaluj Flask:

    ```bash
    pip install flask
    ```

3. Uruchom aplikację:

    ```bash
    python app.py
    ```

4. Otwórz przeglądarkę i przejdź do:  
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🗂 Struktura projektu

```
batony_app/
├── app.py                # Główna aplikacja Flask
├── static/
│   └── images/           # Obrazy batonów
│       ├── baton1.jpg
│       └── baton2.jpg
└── templates/
    └── index.html        # Szablon HTML strony głównej
```

---

## ✏️ Przykładowe dane

```python
produkty = [
    {
        'nazwa': 'Baton Proteinowy XYZ',
        'opis': 'Baton XYZ zawiera 20g białka i idealnie nadaje się po treningu.',
        'obraz': 'images/baton1.jpg'
    },
    {
        'nazwa': 'Baton Proteinowy ABC',
        'opis': 'Baton ABC to zdrowa przekąska z dodatkiem orzechów i kakao.',
        'obraz': 'images/baton2.jpg'
    }
]
```
---
## Nowe funkcje

Strona główna pokazuje liczbę odwiedzin użytkownika w sesji.

---

## 🔧 Pomysły na rozwój

- Dodanie formularza do wprowadzania nowych batonów  
- Zintegrowanie z bazą danych (np. SQLite)  
- Możliwość oceniania batonów  
- Dodanie panelu administracyjnego  

---

## 📄 Licencja

Projekt dostępny na licencji MIT.  
Możesz go dowolnie używać, modyfikować i udostępniać.

---

## 👨‍💻 Autor

Stworzono z pasji do zdrowego odżywiania i nauki web developmentu.  
Jeśli masz pytania lub sugestie — zapraszam do kontaktu!

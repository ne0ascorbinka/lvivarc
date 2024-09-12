# lvivarc

To install:
1. Download python
2. Set up virtual enviroment using
   ```bash
   python -m venv env
   ```
   and then activate it using
   ```bash
   env\Scripts\activate
   ```
   or smth, just activate it
3. Install packages using
   ```bash
   pip install -r requirements.txt
   ```
4. Go to `lvivarc` dir:
   ```bash
   cd lvivarc
   ```
   and run next set of commands:
   ```bash
   python manage.py migrate
   python manage.py collectstatic
   python manage.py runserver
   ```
5. Enjoy.

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

# First fake the admin migrations since that's what's causing the error
python manage.py migrate admin --fake

# Then run the rest of the migrations with fake-initial
python manage.py migrate --fake-initial

# Run regular migrate to catch anything that actually needs to be migrated
python manage.py migrate
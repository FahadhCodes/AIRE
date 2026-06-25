from AIRE import app, db

if __name__ == "__main__":
    with app.app_context():
        # IMPORTANT: Import your models here so SQLAlchemy registers them!
        # Replace 'models' with the actual filename where your requirements/ba_outputs classes live.
        from AIRE import models  # noqa

        print("Attempting to create database...")
        db.create_all()
        print("Database creation complete.")

    app.run(debug=True, host="0.0.0.0", port=5000)

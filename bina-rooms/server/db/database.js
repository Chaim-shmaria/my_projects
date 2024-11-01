const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('./db/counter.db'); // Using an in-memory database for now

db.serialize(() => {
    db.run("CREATE TABLE IF NOT EXISTS counter (id INTEGER PRIMARY KEY, value INTEGER)");
    db.get("SELECT * FROM counter WHERE id = 1", (err, row) => {
        if (!row) {
            db.run("INSERT INTO counter (id, value) VALUES (1, 0)");
        }
    });
});

module.exports = db;

//TODO: replace temporary name 'counter' to real name.

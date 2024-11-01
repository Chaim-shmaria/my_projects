const db = require('../db/database');

exports.getCounter = () => {
    return new Promise((resolve, reject) => {
        db.get("SELECT value FROM counter WHERE id = 1", (err, row) => {
            if (err) return reject(err);
            resolve(row ? row.value : 0);
        });
    });
};

exports.incrementCounter = () => {
    return new Promise((resolve, reject) => {
        db.run("UPDATE counter SET value = value + 1 WHERE id = 1", function (err) {
            if (err) return reject(err);
            db.get("SELECT value FROM counter WHERE id = 1", (err, row) => {
                if (err) return reject(err);
                resolve(row.value);
            });
        });
    });
};

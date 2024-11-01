const express = require('express');
const router = express.Router();
const counterRoutes = require('./tempRoutes');

// Use the counter routes
router.use('/counter', counterRoutes);

module.exports = router;
